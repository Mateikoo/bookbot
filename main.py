import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import words_count, symbols_count, symbols_sort


def get_book_text(path):
    # Funkcja otwierająca plik ze ścieżki i zwracająca tekst jako string.

    with open(path) as f:
        text = f.read()

    return text


def main():

    book_text = get_book_text(sys.argv[1])
    symbols_dict = symbols_count(book_text)
    sorted_list = symbols_sort(symbols_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(words_count(book_text))
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()
