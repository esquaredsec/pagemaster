from stats import word_counter, char_counter, chars_dict_to_sorted_list

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    total_words = word_counter(text)
    char_dict_count = char_counter(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict_count)
    print(f"Found {total_words} total words")
    print(char_dict_count)
    print(char_sorted_list)

def get_book_text(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()