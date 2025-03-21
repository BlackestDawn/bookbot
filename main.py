from stats import count_words, character_count


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


main()
