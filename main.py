from stats import get_num_words, get_num_char, print_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
        return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    words = get_num_words(book_text)
    chars = get_num_char(book_text)
    print_report(words, chars, filepath)

main()
