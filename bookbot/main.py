from stats import get_words, get_num_of_chars, get_sorted_num_of_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    res = get_book_text(f"{file_path}")
    dict = get_num_of_chars(res)
    sorted_list = get_sorted_num_of_chars(dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_words(res)} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()

