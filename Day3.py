from utils import timing
import pandas as pd
import numpy as np
import operator


def read_input():
    with open("Day3.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [list(map(int, list(_.strip(" ")))) for _ in input.split("\n")]


def binaryToInt(binaryList):
    return int("".join(str(i) for i in binaryList), 2)


def ogr_csr(df, op):
    _ = 0
    while len(df.index) != 1:
        no_rows = len(df.index)
        
        total =  df.sum(axis=0)
        
        rule = op(total[_] / no_rows, 0.5)
        df = df[df[_] == rule].reset_index(drop=True)

        _ += 1
    return df.loc[0].values.astype(int)

@timing
def one(input):
    print("First star: ")

    no_cols = len(input[0])
    no_rows = len(input)

    df = pd.DataFrame(data=np.array(input), columns=range(no_cols))
    total =  df.sum(axis=0)

    gamma_bin = list(map(int, (total / no_rows > 0.5).values))

    eps = binaryToInt([0 if _ else 1 for _ in gamma_bin])
    gamma = binaryToInt(gamma_bin)

    print("gamma\teps\tans\n{}  *\t{}  =\t{}".format(gamma, eps, gamma * eps))

@timing
def two(input):
    print("Second star: ")
    no_cols = len(input[0])

    df = pd.DataFrame(data=np.array(input), columns=range(no_cols))

    ogr = binaryToInt(ogr_csr(df.copy(), operator.ge))
    csr = binaryToInt(ogr_csr(df.copy(), operator.lt))

    print("ogr\tcsr\tans\n{}  *\t{}  =\t{}".format(ogr, csr, ogr * csr))


if __name__ == "__main__":
    input = preprocess_input(read_input())

    one(input)
    two(input)
