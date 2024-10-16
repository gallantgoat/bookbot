def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    

    def word_count(book):
        words = book.split()
        print(len(words))
    
    word_count(file_contents)        


if __name__=="__main__":
    main()