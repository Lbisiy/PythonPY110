INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
     # TODO перезаписать содержимое одного файла в другой
    with open(INPUT_FILE, 'r') as read_file:
        with open(OUTPUT_FILE, 'w') as write_file:
            for line in map(lambda x: x.upper(), read_file):
                write_file.write(line)

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
