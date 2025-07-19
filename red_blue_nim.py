import sys
import random

def assign_rocks(num_red, num_blue):

    #total_rocks is a list of 'red' and 'blue' strings
    total_rocks = (['red'] * num_red) + (['blue'] * num_blue) 
    random.shuffle(total_rocks)

    # Randomly divide into two piles
    group_pile_size = random.randint(8, 20)
    pile_1 = total_rocks[:group_pile_size]
    print("Pile 1:", pile_1)
    pile_2 = total_rocks[group_pile_size:]
    print("Pile 2:", pile_2)

    return pile_1, pile_2

def standard():
    print("This will be Standard")
    scan = input("Enter q to exit\n")

    while True:
        scan = input("How about now\n")
        if scan == 'q':
            break
def misere():
    print("This will be Misere")
    scan = input("Enter q to exit\n")

    while True:
        scan = input("How about now\n")
        if scan == 'q':
            break

def main():
    if len(sys.argv) != 3:
        print("Usage: python red_blue_nim.py <num-red> <num-blue>")
        sys.exit(1)
    try:
        num_red = int(sys.argv[1])      #string that represents command land argument
        num_blue = int(sys.argv[2])     #string that represents command land argument
    except:
        print("Error: num-red and num-blue must be integers.")
        sys.exit(1)

    total_rocks = num_red + num_blue
    if total_rocks < 16:
        print("Warning: Total number of rocks should be at least 16 for both piles to have a minimum of 8.")
        sys.exit(1)

    pile_1, pile_2 = assign_rocks(num_red, num_blue)

    print("Pile 1 has", len(pile_1), "rocks:", pile_1)
    print("Pile 2 has", len(pile_2), "rocks:", pile_2)

    print("Welcome to Red Blue Nim. Select your Gamemode")
    print("1. Classic")
    print("2. Misere")
    scan = input()
    if scan == "1":
        print("You are playing Classic Red Blue Nim.")
        standard()
    elif scan == "2":
        print("You are playing Misere Red Blue Nim.")
        misere()
if __name__ == "__main__":
    main()
