import json


def task(input_filename: str, output_filename: str) -> None:

    with open(input_filename, 'r') as r_f:
        output = json.load(r_f)
    with open(output_filename, 'w') as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    input_filename = "input.json"
    output_filename = "output.json"

    task(input_filename, output_filename)

    with open(output_filename) as output_f:
        for line in output_f:
            print(line, end="")
