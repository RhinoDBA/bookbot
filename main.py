# main.py
from stats import get_num_words, get_char_counts, get_sorted_char_list

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    #print(f"Found {num_words} total words")
    char_counts = get_char_counts(text)
    #print(char_counts)
    sorted_chars = get_sorted_char_list(char_counts)
 
 # print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============ END ===============")
    
if __name__ == "__main__":
    main()
