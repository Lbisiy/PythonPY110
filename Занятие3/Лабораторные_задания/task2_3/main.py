import json


def task():
    filename = "input.json"
    with open(filename) as f:
        data = json.load(f)
    return max(data, key=lambda x: x['score'])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
