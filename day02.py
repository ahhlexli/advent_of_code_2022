def part_one():
    """
    A = Rock, B = Paper, C = Scissors
    X = Rock, Y = Paper, Z = Scissors
    Points Rock = 1, Paper = 2, Scissors = 3
    Points Win = 6, Draw = 3, Lose = 0
    """

    file_name = "day02_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().splitlines()

    match_points = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }

    total_points = sum([match_points[pair] for pair in puzzle_input])

    return total_points


def part_two():
    """
    A = Rock, B = Paper, C = Scissors
    X = Lose, Y = Draw, Z = Win
    Points Rock = 1, Paper = 2, Scissors = 3
    Points Win = 6, Draw = 3, Lose = 0
    """

    file_name = "day02_input.txt"

    with open(file_name, "r") as f:

        puzzle_input = f.read().splitlines()

    points = {"A": 1, "B": 2, "C": 3}
    win_state = {"Z": 6, "Y": 3, "X": 0}

    win_dict = {"A": "B", "B": "C", "C": "A"}
    lose_dict = {"A": "C", "B": "A", "C": "B"}

    total_points = 0

    for pair in puzzle_input:

        other_player = pair[0]
        desired_state = pair[-1]

        if desired_state == "X":

            my_play = lose_dict[other_player]

        elif desired_state == "Y":

            my_play = other_player

        elif desired_state == "Z":

            my_play = win_dict[other_player]

        my_play_points = points[my_play]
        my_state_points = win_state[desired_state]

        points_this_round = my_play_points + my_state_points

        total_points += points_this_round

    return total_points


#####

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
