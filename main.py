# main.py
from stats import get_num_words

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
