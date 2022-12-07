from itertools import count
def pow_gen(base: int):
    ...  # TODO записать функцию-генератор
    gen = (base ** i for i in count(0, 1))
    return gen


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
