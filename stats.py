def get_num_words(text):
    words = text.split()
    return words

def get_num_char(text):
    chars = {}

    words = text.split()

    for word in words:
        for char in word:
            if(char.lower() in chars):
                chars[char.lower()] += 1
            else:
                chars[char.lower()] = 1

    return chars

def print_report(words, chars, filepath):
    sorted_chars = sorted(chars, key=lambda char: chars[char], reverse=True)    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath[1:]}...")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        print(f"{char}: {chars[char]}")

    print("============= END ===============")
