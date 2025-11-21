def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = count_words(text)
    print(f"found {num_words} total words")

if __name__ == "__main__":
    main()
