from stats import count_words

def get_book_text (book_file_path):
    Book_text = "";
    with open(book_file_path) as f:
        Book_text = f.read();
    return Book_text;

def main ():
    #print(get_book_text("./books/frankenstein.txt"))
    #num_words = count_words(get_book_text("./books/frankenstein.txt"))
    #print(f"{num_words} words found in the document")
    print(f"{count_words(get_book_text("./books/frankenstein.txt"))} words found in the document")

main()