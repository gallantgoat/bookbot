def main():
    # "user" inputs
    book_path = "books/frankenstein.txt"
    book = book_text(book_path)
    word_num = word_count(book)
    print(word_num)

# takes file location of book and reads it back as one giant string
def book_text(path):
    with open(path) as f:
        return f.read()

# takes string and breaks it down into individual strings in a list and then counts the strings
def word_count(book):
    words = book.split()
    return(len(words))
           


if __name__=="__main__":
    main()