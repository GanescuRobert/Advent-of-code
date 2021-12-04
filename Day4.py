import numpy as np
from utils import timing


def read_input():
    with open("Day4.input") as file:
        input = file.read()
    return input


def get_bingo_numbers(input):
    bingo_numbers = input.split("\n")[0]
    bingo_numbers = [int(_) for _ in bingo_numbers.split(",")]
    
    return bingo_numbers


def get_bingo_boards(input):
    bingo_boards = input.split("\n\n")[1:]
    bingo_boards = [_.replace("\n", " ").replace("  ", " ") for _ in bingo_boards]
    bingo_boards = [_[1:] if _[0] == " " else _ for _ in bingo_boards]

    bingo_boards = [
        np.array(list(map(int, _.split(" ")))).reshape((5, 5)) for _ in bingo_boards
    ]

    return bingo_boards


def is_winner(out_bingo_numbers, board):
    rows_cols = np.array(
        [board[i, :] for i in range(5)] + [board[:, i] for i in range(5)]
    )
    return any([all([_ in out_bingo_numbers for _ in rc]) for rc in rows_cols])


def unmarked_numbers(out_bingo_numbers, board):
    return [_ for _ in board.ravel().tolist() if _ not in out_bingo_numbers]


def get_winners(bingo_numbers, bingo_boards):
    winners = []
    idx_winners = []
    out_bingo_numbers = bingo_numbers[:4]
    bingo_numbers = bingo_numbers[4:]
    found = False
    for bingo_number in bingo_numbers:
        out_bingo_numbers.append(bingo_number)
        for idx, board in enumerate(bingo_boards):
            if idx not in idx_winners:
                if is_winner(out_bingo_numbers, board):
                    sou = sum(unmarked_numbers(out_bingo_numbers, board))
                    winners.append(sou * bingo_number)
                    idx_winners.append(idx)
    return winners


@timing
def one(winners):
    print("First star: ")
    print(winners[0])


@timing
def two(winners):
    print("Second star: ")
    print(winners[-1])

if __name__ == "__main__":
    input = read_input()

    bingo_numbers = get_bingo_numbers(input)
    bingo_boards = get_bingo_boards(input)
    winners = get_winners(bingo_numbers, bingo_boards)
    
    one(winners)
    two(winners)
