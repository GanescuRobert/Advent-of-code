from utils import timing


import numpy as np

grid = np.array([])


def read_input():
    with open("Day6.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [_ for _ in input.split("\n")]


def get_coords(from_point, to_point):
    x0, x1 = from_point[0], to_point[0] + 1
    y0, y1 = from_point[1], to_point[1] + 1
    return [x0, x1, y0, y1]


def toggle(x0x1y0y1):
    x0, x1, y0, y1 = x0x1y0y1
    grid[x0:x1, y0:y1] = np.invert(grid[x0:x1, y0:y1])


def turn_on(x0x1y0y1):
    x0, x1, y0, y1 = x0x1y0y1
    grid[x0:x1, y0:y1] = True


def turn_off(x0x1y0y1):
    x0, x1, y0, y1 = x0x1y0y1
    grid[x0:x1, y0:y1] = False


def add_one(x0x1y0y1):
    x0, x1, y0, y1 = x0x1y0y1
    grid[x0:x1, y0:y1] += 1


def substract_one(x0x1y0y1):
    x0, x1, y0, y1 = x0x1y0y1
    grid[x0:x1, y0:y1] -= 1
    grid[grid < 0] = 0


def add_two(x0x1y0y1):
    add_one(x0x1y0y1)
    add_one(x0x1y0y1)


@timing
def one(input):
    print("First star: ")
    global grid
    grid = np.zeros((1000, 1000), dtype=bool)
    functions = {
        "on": turn_on,
        "off": turn_off,
        "toggle": toggle,
    }

    lights(functions)


@timing
def two(input):
    print("Second star: ")
    global grid
    grid = np.zeros((1000, 1000), dtype=int)
    functions = {
        "on": add_one,
        "off": substract_one,
        "toggle": add_two,
    }
    lights(functions)


def lights(functions):
    for action in input:
        strr_words = action.split(" ")

        if strr_words[0] == "toggle":
            strr_words.insert(0, None)

        from_point = tuple((map(int, strr_words[2].split(","))))
        to_point = tuple((map(int, strr_words[4].split(","))))

        x0x1y0y1 = get_coords(from_point, to_point)
        functions[strr_words[1]](x0x1y0y1)

    print(grid.sum())


if __name__ == "__main__":
    input = preprocess_input(read_input())

    one(input)
    two(input)
