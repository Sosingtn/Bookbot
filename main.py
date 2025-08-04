from stats import get_num_words,get_num_chars,turn_dict_into_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


arg = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_content = get_book_text(arg)
    word_count = get_num_words(book_content)
    char_dict = get_num_chars(book_content)
    sorted_list = turn_dict_into_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arg}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        char = entry["char"]
        count = entry["num"]
        print(f"{char}: {count}")
    print("============= END ===============")
main()