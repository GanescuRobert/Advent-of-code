from utils import timing
import numpy as np

field = np.zeros((1000, 1000), dtype=np.int8)
print(field)


def read_input():
    with open("Day5.input") as file:
        input = file.read()
    return input


def preprocess_input(input):
    return [
        list(map(int, point.split(",")))
        for _ in input.split("\n")
        for point in _.split(" -> ")
    ]

def move(a0,a1):
    sign = 1 if a0>a1 else -1
    
    a0 = (-1)*sign + a0
    a1 = (-1)*(-sign) + a1
    return a0,a1
        
@timing
def one(input):
    print("First star: ")
    for _ in range(1, len(input), 2):
        xy0, xy1 = input[_ - 1], input[_]

        if xy0[0] == xy1[0]:
            x = xy0[0]

            y0, y1 = xy0[1], xy1[1]
            if y0 > y1:
                y0, y1 = y1, y0

            field[x, y0 : y1 + 1] += 1

        elif xy0[1] == xy1[1]:
            y = xy0[1]

            x0, x1 = xy0[0], xy1[0]
            if x0 > x1:
                x0, x1 = x1, x0

            field[x0 : x1 + 1, y] += 1
        else:
            x0, y0 = xy0
            x1, y1 = xy1
            while x0!=x1:
                     
                field[x0,y0]+=1
                field[x1,y1]+=1
                # print(x0,y0,x1,y1)  
                if abs(x0-x1)==1:
                    break                                
                x0,x1 = move(x0,x1)
                y0,y1 = move(y0,y1)
            if x0==x1:
                 field[x0,y0]+=1
                
            
    # print(field)
    print(len(field[field >= 2]))


@timing
def two(input):
    print("Second star: ")


if __name__ == "__main__":
    input = preprocess_input(read_input())

    one(input)
    two(input)
