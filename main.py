from stats import count_words, character_count, sort_counts
import sys


def main(bookPath):
    with open(bookPath) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print("--- Begin report of book/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        char_count = sort_counts(character_count(file_contents))
        for val in char_count:
            if val["char"].isalpha():
                print(f"{val["char"]}: {val["count"]}")


if len(sys.argv) >= 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
