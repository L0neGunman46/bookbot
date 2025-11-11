from stats import count_words
from stats import count_characters
from stats import sort_chars
import sys

def get_book_text(path: str):
    # getting the book data
    file_contents = ""
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def on_sort(chars):
    return chars["num"]

def main():
    sys_arg = sys.argv
    if len(sys_arg) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path: str = sys_arg[1]
        words = get_book_text(path)
        num_words = count_words(words)
        char_counts = count_characters(words)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        form_chars = sort_chars(char_counts)
        form_chars.sort(reverse=True,key=on_sort)
        for item in form_chars:
            print(f"{item["char"]}: {item["num"]}\n")
        print("============= END ===============")


if __name__ == "__main__":
    main()
