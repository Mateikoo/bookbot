def get_book_text(path):
    # Funkcja otwierająca plik ze ścieżki i zwracająca tekst jako string.

    with open(path) as f:
        text = f.read()

    return text


def words_count(book_text):
    # Funkcja licząca ilość słów w książce.

    words_count = book_text.split()
    num_words = len(words_count)

    return f"Found {num_words} total words"


def main():

    book_text = get_book_text("/home/mateusz/workspace/github.com/mateusz/bookbot/books/frankenstein.txt")
    
    print(words_count(book_text))


main()
