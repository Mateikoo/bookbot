from stats import words_count, symbols_count


def get_book_text(path):
    # Funkcja otwierająca plik ze ścieżki i zwracająca tekst jako string.

    with open(path) as f:
        text = f.read()

    return text


def main():

    book_text = get_book_text("/home/mateusz/workspace/github.com/mateusz/bookbot/books/frankenstein.txt")
    
    print(symbols_count(book_text))


main()
