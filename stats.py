def words_count(book_text):
    # Funkcja licząca ilość słów w książce.

    words_count = book_text.split()
    num_words = len(words_count)

    return f"Found {num_words} total words"


def symbols_count(book_text):
    # Funkcja tworząca dziennik, gdzie klucz to symbol, a wartość to ilość wystąpień.

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


def symbols_sort(symbols_dict):
    # Funkcja tworząca listę słowników w formacie {"char":a, "num":123}, a następnie sortująca tę listę malejąco.

    list_of_symbols_dicts = []

    for char in symbols_dict:

        symbol_dict = {}
        symbol_dict["char"] = char
        symbol_dict["num"] = symbols_dict[char]

        list_of_symbols_dicts.append(symbol_dict)

    def sort_on(symbol_dict):
        return symbol_dict["num"]

    list_of_symbols_dicts.sort(reverse=True, key=sort_on)

    return list_of_symbols_dicts