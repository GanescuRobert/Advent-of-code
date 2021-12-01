from utils import timing


def read_input():
    with open("Day5.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [_ for _ in input.split("\n")]


def least_three_vowels(strr):
    return sum([strr.count(v) for v in "aeiou"]) > 2


def least_one_letter_twice(strr):
    for _ in range(1, len(strr)):
        if strr[_ - 1] == strr[_]:
            return True
    return False


def not_contain(strr):
    return all([_ not in strr for _ in ["ab", "cd", "pq", "xy"]])


def pair_of_any_two_letters(strr):
    for _ in range(1, len(strr)):
        pair = strr[_ - 1 : _ + 1]
        if pair in strr[_ + 1 :]:
            return True
    return False


def one_letter_between(strr):
    for _ in range(1, len(strr) - 1):
        if strr[_ - 1] == strr[_ + 1]:
            return True
    return False


@timing
def one(input):
    print("First star: ")
    ans = sum(
        map(
            lambda strr: all(
                [
                    least_three_vowels(strr),
                    least_one_letter_twice(strr),
                    not_contain(strr),
                ]
            ),
            input,
        )
    )
    print(ans)


@timing
def two(input):
    print("Second star: ")
    ans = sum(
        map(
            lambda strr: all(
                [
                    pair_of_any_two_letters(strr),
                    one_letter_between(strr),
                ]
            ),
            input,
        )
    )
    print(ans)


if __name__ == "__main__":
    input = preprocess_input(read_input())
    one(input)
    two(input)
