def count_words(words):
    split_words = words.split()
    total_words = len(split_words)
    return total_words



def count_characters(words):
    char_count = {}
    for char in words:
        low_case_char = char.lower()
        if low_case_char not in char_count:
            char_count[low_case_char] = 1
        else:
            char_count[low_case_char] += 1
    return char_count


def sort_chars(char_counts):
    count_items = char_counts.items()
    arr = []
    for item in count_items:
        char, count = item
        arr.append({"char": char, "num": count})
    return arr