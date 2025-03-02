def count_words(text):
    """
    Count the number of books in a text.
    """
    text = text.split()
    count = 0
    for word in text:
        #if len(word) < 1: continue
        count += 1

    total_count = f"{count} words found in the document"
    return total_count


def let_count(text):
    """
    Count the number of books in a text.
    """
    text = text.split()
    letter_count = {}
    for word in text:
        for letter in word:
            letter = letter.lower()
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count