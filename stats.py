def words_count(book_text):
    # Funkcja licząca ilość słów w książce.

    words_count = book_text.split()
    num_words = len(words_count)

    return f"Found {num_words} total words"


def symbols_count(book_text):

    symbols_dict = {}
    symbols_list = []
    lower_book_text = book_text.lower()

    for char in lower_book_text:
        symbols_list.append(char)

    for char in symbols_list:
        
        if char not in symbols_dict:
            symbols_dict[char] = 0

        symbols_dict[char] += 1

    return symbols_dict


