import sys
from stats import word_counter, char_counter, chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main.py = sys.argv[0]
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    total_words = word_counter(text)
    char_dict_count = char_counter(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict_count)
    print_report(char_sorted_list, file_path, total_words)

def print_report(char_sorted_list: list[tuple[str, int]], file_path: str, total_words: int):
    print("============ PAGEMASTER v 1.0 ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char, count in char_sorted_list:
        if not char.isalpha():
            continue
        else:
            print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()
