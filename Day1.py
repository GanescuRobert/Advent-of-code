def read_input():
    with open("Day1.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [int(_) for _ in input.split("\n")]


def get_ans(input):
    return sum(
        [
            input[fst] < input[snd]
            for fst, snd in zip(range(0, len(input)), range(1, len(input)))
        ]
    )


def one(input):
    print("First star: ")
    print(get_ans(input))


def two(input):
    print("Second star: ")

    print(
        get_ans(
            [
                input[fst] + input[snd] + input[trd]
                for fst, snd, trd in zip(
                    range(0, len(input)), range(1, len(input)), range(2, len(input))
                )
            ]
        )
    )


if __name__ == "__main__":
    input = preprocess_input(read_input())
    one(input)
    two(input)
