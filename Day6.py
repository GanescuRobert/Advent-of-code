from utils import timing
import numpy as np


def read_input():
    with open("Day6.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [int(_) for _ in input.split(",")]


def main(_input, days):
    fishes = np.zeros(9, dtype=np.int64)

    for _ in _input:
        fishes[_] += 1

    for _ in range(days):
        no_borned = fishes[0]

        fishes[:-1] = fishes[1:]
        fishes[8] = no_borned  # new fishes
        fishes[6] += no_borned  # old fishes

    return sum(fishes)


@timing
def one(_input):
    print("First star: ")
    ans = main(_input, 80)
    print(ans)


@timing
def two(_input):
    print("Second star: ")
    ans = main(_input, 256)
    print(ans)


if __name__ == "__main__":
    _input = np.array(preprocess_input(read_input()))

    one(_input)
    two(_input)
