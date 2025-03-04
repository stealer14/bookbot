def count_words(text):
    """
    Count the number of books in a text.
    Returns a string with the total count.
    """
    text = text.split()
    count = 0
    for word in text:
        #if len(word) < 1: continue
        count += 1

    #total_count = f"{count} words found in the document"
    total_count = count
    return total_count


def let_count(text):
    """
    Count the number of books in a text.
    Returns a dictiona`ry of letter counts.
    """
    text = text.split()
    letter_count = {}
    for word in text:
        for letter in word:
            letter = letter.lower()
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def generate_report(dict, path, word_count):
    """
    Generate a report from a dictionary.
    """
    #Preparing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {path[2:]}...")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    kv_dict = []
    for ky, val in dict.items():
        if not ky.isalpha(): continue
        kv_dict.append(f"{ky}: {val}")
    
    for item in sorted(kv_dict, key = lambda item: item[val], reverse= True):
        print(item)

    print("============= END ===============")
    return None