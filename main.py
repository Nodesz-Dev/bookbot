from stats import count_words
from stats import count_characters
from stats import sort_character_list
import sys

def get_book_text (book_file_path):
    Book_text = "";
    with open(book_file_path) as f:
        Book_text = f.read();
    return Book_text;

def print_list_by_line(list):
    for each in list:
        print(f"{each["char"]}: {each["num"]}")
    return 

def print_report(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(book))} total words")
    print("--------- Character Count -------")
    print_list_by_line(sort_character_list(count_characters(get_book_text(book))))
    print("============= END ===============")
    return



def main ():
    if len(sys.argv) > 1:
        print_report(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()