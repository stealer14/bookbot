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