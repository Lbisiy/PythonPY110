import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"####\s+(?P<position>\d+)\.\s+\[(?P<book>([-\w:'\s])+)\]\((?P<book_url>https:\/\/a\w+\.\w+\/\w+)\)\s+by\s+(?P<author>([\s]?[&]?[\s+]?[A-Z]['.]?\w*[.]?){2,})\s+\((?P<recommended>\d+\.\d+%)\s+\w+\)\n+!\[\]\((?P<cover_url>https:\/\/\w\w\w\.\w+\.\w+\/\w+\/\w+\/\d+\.\w+[#]\w+)\)\s+\"(?P<description>(\w+[-—:()&'`’“”,!;?.\s]*)*)"


# reg_group(position) = (?P<position>\d+)
# reg_group(book) = (?P<book>([-\w:'\s])
# reg_group(book_url) = (?P<book_url>https:\/\/a\w+\.\w+\/\w+)
# reg_group(author) = (?P<author>([\s]?[&]?[\s+]?[A-Z]['.]?\w*[.]?){2,})
# reg_group(recommended) = (?P<recommended>\d+\.\d+%)
# reg_group(cover_url) = (?P<cover_url>https:\/\/\w\w\w\.\w+\.\w+\/\w+\/\w+\/\d+\.\w+[#]\w+)
# reg_group(description) = (?P<description>(\w+[-—:()&'`’“”,!;?.\s]*)*)


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
