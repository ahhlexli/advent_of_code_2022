def part_one():

    file_name = "day06_input.txt"

    with open(file_name, "r") as f:
        puzzle_input = f.read()

    for i in range(3, len(puzzle_input)):

        previous_four = puzzle_input[i - 3 : i + 1]
        previous_four_set = set(previous_four)

        if len(previous_four_set) == 4:

            return i + 1


def part_two():

    file_name = "day06_input.txt"

    with open(file_name, "r") as f:
        puzzle_input = f.read()

    for i in range(13, len(puzzle_input)):

        previous_characters = puzzle_input[i - 13 : i + 1]
        previous_characters_set = set(previous_characters)

        if len(previous_characters_set) == 14:

            return i + 1


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
