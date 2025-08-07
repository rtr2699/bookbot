import sys
from stats import get_num_words
from stats import character_count
from stats import get_sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])

    text = book.split()

    word_count = get_num_words(text)
    count = character_count(book)
    sorted_chars = get_sorted_characters(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_data in sorted_chars:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")

    print("============= END ===============")

main()
