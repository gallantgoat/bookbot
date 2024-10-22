def main():
    # "user" inputs
    book_path = "books/frankenstein.txt"
    book = book_text(book_path)
    word_num = word_count(book)
    print(word_num)
    #tests
    characters = char_count(book)
    print(characters)

# takes file location of book and reads it back as one giant string
def book_text(path):
    with open(path) as f:
        return f.read()

# takes string and breaks it down into individual strings in a list and then counts the strings (A word count one might say)
def word_count(book):
    words = book.split()
    return(len(words))

# counts the individual time a character appears in the string
def char_count(book):
    char_dict = {}
    chars_lower = book.lower()
    characters = list(chars_lower)
    for char in characters:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
    



if __name__=="__main__":
    main()