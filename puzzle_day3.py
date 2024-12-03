import re


def extract_numbers_from_file():
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    result = 0

    with open("input/day3.txt", 'r') as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                result = result + (int(match[0])* int(match[1]))

    return result


def calculate_enabled_multiplications():
    with open("input/day3.txt", "r") as file:
        input_data = file.read()

    # Define regex patterns to capture `mul`, `do()`, and `don't()` instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    # Initialize variables
    is_mul_enabled = True  # mul instructions start enabled by default
    total_sum = 0

    # Scan through the input and process instructions
    for match in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_data):
        instruction = match.group(0)
        if mul_pattern.match(instruction):  # If it's a valid mul instruction
            if is_mul_enabled:
                x, y = map(int, mul_pattern.match(instruction).groups())
                total_sum += x * y
        elif do_pattern.match(instruction):  # Enable mul instructions
            is_mul_enabled = True
        elif dont_pattern.match(instruction):  # Disable mul instructions
            is_mul_enabled = False

    return total_sum
