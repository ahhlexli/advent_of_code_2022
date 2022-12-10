import numpy as np


def part_one():

    file_name = "day05_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().split("\n\n")

    original_arrangement = puzzle_input[0]
    instructions = puzzle_input[1]

    original_arrangement_list = original_arrangement.split("\n")

    full_arrangement = []

    for row in original_arrangement_list[:-1]:

        filled_row = row.replace("    ", " [-]")
        filled_row = filled_row.split(" ")
        filled_row = [
            i.replace("[", "").replace("]", "").replace("-", "") for i in filled_row
        ]

        full_arrangement.append(filled_row)

    full_arrangement = np.array(full_arrangement).T.tolist()
    [row.reverse() for row in full_arrangement]

    starting_arrangement = []
    for row in full_arrangement:

        row = [element for element in row if element != ""]
        starting_arrangement.append(row)

    instruction_list = instructions.split("\n")

    for instruction in instruction_list:

        instructions = (
            instruction.replace("move", "").replace("from", "").replace("to", "")
        )

        instructions = [int(i.strip()) for i in instructions.split(" ") if i != ""]

        number_of_crates = instructions[0]
        starting_column_index = instructions[1] - 1
        finishing_column_index = instructions[2] - 1

        for i in range(number_of_crates):

            crate_to_move = starting_arrangement[starting_column_index].pop()
            starting_arrangement[finishing_column_index].append(crate_to_move)

    final_arrangement = [row[-1] for row in starting_arrangement]

    return "".join(final_arrangement)


def part_two():

    file_name = "day05_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().split("\n\n")

    original_arrangement = puzzle_input[0]
    instructions = puzzle_input[1]

    original_arrangement_list = original_arrangement.split("\n")

    full_arrangement = []

    for row in original_arrangement_list[:-1]:

        filled_row = row.replace("    ", " [-]")
        filled_row = filled_row.split(" ")
        filled_row = [
            i.replace("[", "").replace("]", "").replace("-", "") for i in filled_row
        ]

        full_arrangement.append(filled_row)

    full_arrangement = np.array(full_arrangement).T.tolist()
    [row.reverse() for row in full_arrangement]

    starting_arrangement = []
    for row in full_arrangement:

        row = [element for element in row if element != ""]
        starting_arrangement.append(row)

    instruction_list = instructions.split("\n")

    for instruction in instruction_list:

        instructions = (
            instruction.replace("move", "").replace("from", "").replace("to", "")
        )

        instructions = [int(i.strip()) for i in instructions.split(" ") if i != ""]

        number_of_crates = instructions[0]
        starting_column_index = instructions[1] - 1
        finishing_column_index = instructions[2] - 1

        crates_to_move = starting_arrangement[starting_column_index][-number_of_crates:]

        del starting_arrangement[starting_column_index][
            len(starting_arrangement[starting_column_index]) - number_of_crates :
        ]

        for crate in crates_to_move:
            starting_arrangement[finishing_column_index].append(crate)

    final_arrangement = [row[-1] for row in starting_arrangement]

    return "".join(final_arrangement)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
