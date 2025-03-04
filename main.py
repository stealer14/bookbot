# Add the /books directory to your .gitignore file. Its typically best practice to only 
# commit code to your repository, not data. We don't want to save the entire book in our 
# Git repository. Generally speaking, Git is for code, not for data.

# gitignore file created at root of directory.

# Write a new function called get_book_test that takes a 
# filepath as input and returns the contents of the 
# file as a string
import sys
from stats import count_words, let_count, generate_report

def main():
    """
    Test the get_book_text function.
    """
    if len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    text = get_book_text(path)
    word_count = count_words(text)
    word_dict = let_count(text)
    generate_report(word_dict, path, word_count)

def get_book_text(path_to_file):
    """
    Read the contents of a file and return it as a string.
    """
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

main()