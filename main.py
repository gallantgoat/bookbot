def main():
    # "user" inputs
    book_path = "books/frankenstein.txt"
    book_string = book_text(book_path)
    word_num = word_count(book_string)
    characters = char_count(book_string)
    characters_sorted = characters_to_sort(characters)
    print(f"--- Starting book report of {book_path}---")
    print(f"The book containes {word_num} words")
    print()

    for char in characters_sorted:
        if not char["char"].isalpha():
            continue
        print(f"The '{char['char']}' character was found {char['num']} times")

    print("--- Report Ending ---")
    


# takes file location of book and reads it back as one giant string
def book_text(path):
    with open(path) as f:
        return f.read()

# takes string and breaks it down into individual strings in a list and then counts the strings (A word count one might say)
def word_count(book):
    words = book.split()
    return(len(words))

# counts the individual time a character appears in the string, returns a dictionary
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

def sort_on(dict):
    return dict["num"]
# take dictionary of characters and return it as a sorted list
def characters_to_sort(characters):
    sorted_list = []
    for char in characters:
        sorted_list.append({"char": char, "num": characters[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        



if __name__=="__main__":
    main()