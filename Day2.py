def preprocess_input(input):
    return [_ for _ in input.split('\n')]

def read_input():
    with open("Day2.input") as file:
        input = file.read()
    return input

def one(input):
    print("First star: ")
    ans = 0
    for present in input:
        p = [int(_) for _ in present.split('x')]
        p.sort()
        l,w,h = p
        ans += 3*l*w+2*l*h+2*w*h
    print(ans)
    
def two(input):
    print("Second star: ")
    ans = 0
    for present in input:
        p = [int(_) for _ in present.split('x')]
        p.sort()
        l,w,h = p
        ans += 2*l+2*w + l*w*h
    print(ans)

if __name__ == "__main__":
    input = read_input()
    input = preprocess_input(input)
    one(input)
    two(input)