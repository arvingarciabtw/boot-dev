import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(20):
        done = generate_content(client, messages, args.verbose)
        if done:
            break
    else:
        print("too many calls, exiting...")
        sys.exit(1)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return True


    func_results = []
    for function_call in response.function_calls:
        result = call_function(function_call, verbose)
        if len(result.parts) == 0:
            raise Exception("whoops")

        func_res = result.parts[0].function_response
        if func_res is None:
            raise Exception("whoops, nothing in function response")

        res = func_res.response
        if res is None:
            raise Exception("whoops, nothing in response")

        func_results.append(result.parts[0])

        if verbose:
            print(f"-> {res}")

    messages.append(types.Content(role="user", parts=func_results))



if __name__ == "__main__":
    main()
