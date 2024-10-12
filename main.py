def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print("--- Begin report of book/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print
        char_count = character_count(file_contents)
        for key in char_count:
            print(f"The \'{key}\' character was found {char_count[key]} times")


def count_words(in_string):
    words_list = in_string.split()
    return len(words_list)


def character_count(in_string):
    char_count = {}
    for char in in_string.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


main()
