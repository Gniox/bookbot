def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
        return file_contents

def get_num_words(text):
    words = text.split()
    return f"{len(words)} words found in the document"

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(get_num_words(book_text))

main()
