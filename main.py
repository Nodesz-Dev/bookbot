def get_book_text (book_file_path):
    Book_text = "";
    with open(book_file_path) as f:
        Book_text = f.read();
    return Book_text;

def main ():
    print(get_book_text("./books/frankenstein.txt"))

main()