
def read_input():
    with open("Day1.input") as file:
        input = file.read()
    return input
    
def one(input):
    print("First star: ")
    print(input.count('(')-input.count(')'))

def two(input):
    print("Second star: ")
    flor = 0
    for pos, _ in enumerate(input):
        flor += 1 if _ == '(' else -1 
        if flor < 0:
            print(pos + 1)
            break
    

if __name__ == "__main__":
    input = read_input()
    one(input)
    two(input)