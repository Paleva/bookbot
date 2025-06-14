from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        book_text = file.read()
    return book_text

def main():
    sys.argv = sys.argv[1:]  # Get command line arguments
    file_path = None

    if len(sys.argv) > 0:
        file_path = sys.argv[0]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(file_path)
    sorted = sort_dict(count_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()