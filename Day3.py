def read_input():
    with open("Day3.input") as file:
        input = file.read()
    return input

directions = {
        '>':(1,0),
        '<':(-1,0),
        '^':(0,1),
        'v':(0,-1)
    }

def one(input):
    print("First star: ")
    houses =[]
    start = (0,0)

    houses.append(start)
    
    for move in input:
        next_house_pos = tuple([sum(x) for x in zip(houses[-1], directions[move])])
        houses.append(next_house_pos)
        
    print(len(list(set(houses))))
        
def two(input):
    print("Second star: ")
    houses =[]
    start = (0,0)

    houses.append(start)
    houses.append(start)
    for _,move in enumerate(input):
        house = tuple([sum(x) for x in zip(houses[_], directions[move])])
        houses.append(house)
            
    print(len(list(set(houses))))
   

if __name__ == "__main__":
    input = read_input()
    one(input)
    two(input)