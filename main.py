with open('books/frankenstein.txt') as f:
    book = f.read()

def count_words(string):
    return len(string.split())

def count_letters(string):
    letter_count = {}
    words = string.lower().split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1
    return letter_count

# letter to list -> sort letters -> back to dict/object
letter_list = list(count_letters(book).items())
letter_list.sort(key=lambda x:x[0])
letter_dict = dict(letter_list)

#Alternative for sorting list back into an object
# for letter in letter_dict:
#     print(letter)
# letterList = {k : v for k, v in sorted(letter_count.items())}

def report(string):
    print(f"--- Begin report of book ---")
    print(f"{count_words(string)} words found in the document")

    for letter in letter_dict:
        print(f"The '{letter}' character was found {letter_dict[letter]} times")
    print("--- End report ---")

report(book)