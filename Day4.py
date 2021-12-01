import hashlib
from utils import timing


def read_input():
    with open("Day4.input") as file:
        input = file.read()
    return input


@timing
def one(input):
    print("First star: ")
    integer = 0
    while True:
        ans = hashlib.md5((input + str(integer)).encode()).hexdigest()
        if ans[:5] == "0" * 5:
            print(integer, ans)
            break
        integer += 1


@timing
def two(input):
    print("Second star: ")
    integer = 0
    while True:
        ans = hashlib.md5((input + str(integer)).encode()).hexdigest()
        if ans[:6] == "0" * 6:
            print(integer, ans)
            break
        integer += 1


if __name__ == "__main__":
    input = read_input()
    one(input)
    two(input)
