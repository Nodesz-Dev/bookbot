from stats import count_words
from stats import count_characters
from stats import sort_character_list

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
    #print(get_book_text("./books/frankenstein.txt"))
    #num_words = count_words(get_book_text("./books/frankenstein.txt"))
    #print(f"{num_words} words found in the document")
    #print(f"{count_words(get_book_text("./books/frankenstein.txt"))} words found in the document")

    #print(f"{count_characters(get_book_text("./books/frankenstein.txt"))}")

    #print(f"{sort_character_list(count_characters(get_book_text("./books/frankenstein.txt")))}")
    #print_list_by_line(sort_character_list(count_characters(get_book_text("./books/frankenstein.txt"))))
    print_report("./books/frankenstein.txt")
    return

main()