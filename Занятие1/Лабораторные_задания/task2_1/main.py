def task(camel_case_str: str) -> str:
    return "".join(filter(lambda x: x.islower(), camel_case_str))


if __name__ == "__main__":
    camel_case_str = "AbCdEfGh"
    print(task(camel_case_str))
