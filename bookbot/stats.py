def get_words(text):
    num_of_words = len(text.split())
    return num_of_words

def get_num_of_chars(text):
    dict = {}

    for char in text:
        char = char.lower()
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    return dict

def get_sorted_num_of_chars(dict):
    def sort_on(items):
        return items["num"]

    sorted_list = []

    for key in dict:
        sorted_list.append({ "char": key, "num": dict[key] })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

