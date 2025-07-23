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


def computer_turn():
    # Simulate computer's turn
    # For simplicity, the computer will always pick the pile with the most rocks of the same color
    print("COM is thinking...")

def has_duplicates(data, color):
    new_list = []
    for d in data:
        # print(d)
        if d == color:
            new_list.append(d)
    # print("New List:", new_list)
    # print("Counts:", len(new_list) )
    # print("Counts:", len(counts.values()), "\n")
    # print(any(count >= 2 for count in counts.values()))
    if (len(new_list) > 1):
        return True
    else: 
        return False
    
    # return any(count >= 2 for count in counts.values())

def remove_two_marbles(pile, color):
    scan = print("You've picked 2", color ,"marbles")
    if (has_duplicates(pile, color)):
        pile.remove(color)
        pile.remove(color)
        print("Pile now has:", len(pile), "rocks left")
    else:
        print("Not enough", color ,"marbles")

def remove_one_marble(pile, color):
    scan = print("You've picked 1 red marble")
    if (color in pile):
        pile.remove(color)
        print("Pile now has:", len(pile), "rocks left")
    else:
        print("Not enough", color, "marbles")

def standard(pile_1, pile_2):
    print("This will be Standard")

    while True:

        if (len(pile_1) == 0 or len(pile_2) == 0): #lose behavior
            print("Pile is empty");
            print("You lose!")
            break
        print("Player 1: Your Turn")
        print("1. Choose Pile 1")
        print("2. Choose Pile 2")
        print("3. Look at Pile")
        scan = input("Enter q to exit\n")


        if scan == 'q':
            break
        if scan == '1':
            print("You've chosen Pile 1:")
            display_player_choice()
            scan = input("\n")

            if scan == '1':
                remove_two_marbles(pile_1, 'red')
            elif scan == '2':
                remove_two_marbles(pile_1, 'blue')
            elif scan == '3':
                remove_one_marble(pile_1, 'red')
            elif scan == '4':
                remove_one_marble(pile_1, 'blue')
            elif scan == 'q':
                break

        elif scan == '2':
            print("You've chosen Pile 2:\n")
            display_player_choice()
            scan = input("\n")

            if scan == '1':
                remove_two_marbles(pile_2, 'red')
            elif scan == '2':
                remove_two_marbles(pile_2, 'blue')
            elif scan == '3':
                remove_one_marble(pile_2, 'red')
            elif scan == '4':
                remove_one_marble(pile_2, 'blue')
            elif scan == 'q':
                break
        elif scan == '3':
            print("Pile 1: ", pile_1)
            print("Pile 2: ", pile_2)
        else:
            scan = print("Invalid choice. Please choose 1 or 2\n")

def display_player_choice():
    print("Select your choice")
    print("1. Pick 2 red marbles")
    print("2. Pick 2 blue marbles")
    print("3. Pick 1 red marble")
    print("4. Pick 1 blue marble")

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
        standard(pile_1, pile_2)
    elif scan == "2":
        print("You are playing Misere Red Blue Nim.")
        misere()
if __name__ == "__main__":
    main()
