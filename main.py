def Boyer_Moore(_text: str, _pattern: str) -> list[str]:
    pass


def string2list(_string: str) -> list[str]:
    char_list = []
    for char in _string:
        char_list.append(str(char))
    return char_list


def index_in_list(_char: str, _list: list[str]) -> int:
    return _list.index(_char)


if __name__ == "__main__":
    print("Main")
    text: str = "Hoola-Hoola girls like Hooligans"
    pattern: str = "Hooligans"

    text_list: list[str] = string2list(text)
    pattern_list: list[str] = string2list(pattern)

        

