def part_one():
    file_name = "day01_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read()
        puzzle_input = puzzle_input.split("\n\n")

    individual_lists = [group.split("\n") for group in puzzle_input]

    grouped_calories = []

    for calories in individual_lists:

        cleaned_list = [int(i) for i in calories]
        grouped_calories.append(sum(cleaned_list))

    return max(grouped_calories)


def part_two():

    file_name = "day01_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read()
        puzzle_input = puzzle_input.split("\n\n")

    individual_lists = [group.split("\n") for group in puzzle_input]

    grouped_calories = []

    for calories in individual_lists:

        cleaned_list = [int(i) for i in calories]
        grouped_calories.append(sum(cleaned_list))

    grouped_calories = sorted(grouped_calories)

    top_3 = grouped_calories[-3:]

    return sum(top_3)


#####

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
