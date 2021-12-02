from utils import timing


def read_input():
    with open("Day2.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [_ for _ in input.split("\n")]


sub_pos = [0, 0]
aim = 0


def forward(dist):
    global aim
    sub_pos[0] += dist
    aim += dist * sub_pos[1]


def up(dist):
    sub_pos[1] -= dist
    if sub_pos[1] < 0:
        sub_pos[1] = 0


def down(dist):
    sub_pos[1] += dist


@timing
def main(input):
    functions = {
        "forward": forward,
        "up": up,
        "down": down,
    }

    for action in input:
        strr_words = action.split(" ")
        dir, dist = strr_words[0], int(strr_words[1])
        functions[dir](dist)

    one()
    two()


def one():
    print("First star: ")
    print(sub_pos[0] * sub_pos[1])


def two():
    print("Second star: ")
    print(aim * sub_pos[0])


if __name__ == "__main__":
    input = preprocess_input(read_input())
    main(input)
