def list_comprehension(words: list) -> list:
    return [word.capitalize() for word in words]


def list_map(words: list) -> list:
    return list(map(lambda x: x.capitalize(), words))


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]
    return list_words



if __name__ == "__main__":
    list_words = task()
    print(list_comprehension(list_words))
    print(list_map(list_words))
