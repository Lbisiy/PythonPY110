from itertools import count

def count_(start_number: float = 1, step: float = 1):
    # TODO написать функцию-генератор возвращающую целые числа
    gen = (num for num in count(start_number, step))
    return gen

if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
