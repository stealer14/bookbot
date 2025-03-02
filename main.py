# Add the /books directory to your .gitignore file. Its typically best practice to only 
# commit code to your repository, not data. We don't want to save the entire book in our 
# Git repository. Generally speaking, Git is for code, not for data.

# gitignore file created at root of directory.

# Write a new function called get_book_test that takes a 
# filepath as input and returns the contents of the 
# file as a string

def main():
    """
    Test the get_book_text function.
    """
    path = './books/frankenstein.txt'
    text = get_book_text(path)
    word_count = count_words(text)
    print(word_count)

def get_book_text(path_to_file):
    """
    Read the contents of a file and return it as a string.
    """
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

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

main()