import string


def part_one():

    file_name = "day03_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().splitlines()

    lower_cases = dict(
        (letter, index + 1) for index, letter in enumerate(list(string.ascii_lowercase))
    )
    upper_cases = dict(
        (letter, index + 27)
        for index, letter in enumerate(list(string.ascii_uppercase))
    )
    all_priorities = {**lower_cases, **upper_cases}

    priority_sum = 0
    
    for rucksack in puzzle_input:

        total_num_items = len(rucksack)
        items_per_compartment = int(total_num_items / 2)

        first_compartment = rucksack[:items_per_compartment]
        second_compartment = rucksack[items_per_compartment:]

        overlap = [item for item in first_compartment if item in second_compartment][0]

        priority_sum += all_priorities[overlap]


    return priority_sum


def part_two():

    file_name = "day03_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().splitlines()

    lower_cases = dict(
        (letter, index + 1) for index, letter in enumerate(list(string.ascii_lowercase))
    )
    upper_cases = dict(
        (letter, index + 27)
        for index, letter in enumerate(list(string.ascii_uppercase))
    )
    all_priorities = {**lower_cases, **upper_cases}

    priority_sum = 0

    for i in range(0, len(puzzle_input), 3):

        rucksack_1 = puzzle_input[i]
        rucksack_2 = puzzle_input[i + 1]
        rucksack_3 = puzzle_input[i + 2]

        overlap = [
            item for item in rucksack_1 if item in rucksack_2 and item in rucksack_3
        ][0]

        priority_sum += all_priorities[overlap]

    return priority_sum


#####

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
