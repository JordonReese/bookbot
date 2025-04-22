# Imports
from stats import num_words_func, char_count, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    count = num_words_func(book_text)
    character_count = char_count(book_text)
    sorted_list = sort_dict(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")

    print("============= END ===============")

main()