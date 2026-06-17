def word_counter(text: str):
    word_list: str = text
    words: int = len(word_list.split())
    return words

def char_counter(text: str) -> dict:
    char_dict: dict = {}
    char_counts: str = text.lower()

    for char in char_counts:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(char_dict: tuple[str, int]) -> int:
    return char_dict[1]

def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []
    for k, v in char_dict.items():
        sorted_list.append((k,v))
    proper_sorted_list = sorted(sorted_list, reverse=True, key=sort_on)
    return proper_sorted_list
