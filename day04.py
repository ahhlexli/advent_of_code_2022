def part_one():

    file_name = "day04_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().splitlines()

    overlap_count = 0

    for pair in puzzle_input:

        pairs = pair.split(",")

        first_pair_split = [int(num) for num in pairs[0].split("-")]
        second_pair_split = [int(num) for num in pairs[1].split("-")]

        first_pair_lower = first_pair_split[0]
        first_pair_upper = first_pair_split[1]

        second_pair_lower = second_pair_split[0]
        second_pair_upper = second_pair_split[1]

        if (
            first_pair_lower >= second_pair_lower
            and first_pair_upper <= second_pair_upper
        ) or (
            second_pair_lower >= first_pair_lower
            and second_pair_upper <= first_pair_upper
        ):

            overlap_count += 1

    return overlap_count


def part_two():

    file_name = "day04_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().splitlines()

    overlap_count = 0

    for pair in puzzle_input:

        pairs = pair.split(",")

        first_pair_split = [int(num) for num in pairs[0].split("-")]
        second_pair_split = [int(num) for num in pairs[1].split("-")]

        first_pair_lower = first_pair_split[0]
        first_pair_upper = first_pair_split[1]

        second_pair_lower = second_pair_split[0]
        second_pair_upper = second_pair_split[1]

        first_set = set(range(first_pair_lower, first_pair_upper + 1))
        second_set = set(range(second_pair_lower, second_pair_upper + 1))

        if not set(first_set).isdisjoint(second_set):

            overlap_count += 1

    return overlap_count


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
