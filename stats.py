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


def sort_counts(counts):
    sorted_list = []
    for key in counts:
        sorted_list.append({"char": key, "count": counts[key]})

    sorted_list.sort(key=lambda count: count["count"], reverse=True)
    return sorted_list
