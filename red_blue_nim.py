import sys
import random
import time

player_marbles = []
player_score = 0
computer_marbles = []
computer_score = 0

class GameState:
    def __init__(self, pile, player_marbles, computer_marbles, is_max_turn):
        self.pile = pile.copy()
        self.player_marbles = player_marbles.copy()
        self.computer_marbles = computer_marbles.copy()
        self.is_max_turn = is_max_turn # if True, than computer's turn
    
    def get_score(self): # for minimax algo
        score = 0
        for marble in self.player_marbles: # less is better for player
            if marble == 'red':
                score -= 2
            elif marble == 'blue':
                score -= 3
        for marble in self.computer_marbles:
            if marble == 'red':
                score += 2
            elif marble == 'blue':
                score += 3
        return score;

    def is_terminal(self): # returns True is pile is empty         
        return len(self.pile) == 0 
        
def try_move(state, amount, color):
    new_pile = state.pile.copy()
    new_player = state.player_marbles.copy()
    new_computer = state.computer_marbles.copy()

    try:
        if amount == '2':
            if new_pile.count(color) >= 2:
                new_pile.remove(color)
                new_pile.remove(color)
                if state.is_max_turn:
                    new_computer += [color, color]
                else:
                    new_player += [color, color]
            else:
                return None
        elif amount == '1':
            if color in new_pile:
                new_pile.remove(color)
                if state.is_max_turn:
                    new_computer.append(color)
                else:
                    new_player.append(color)
            else:
                return None
        return GameState(new_pile, new_player, new_computer, not state.is_max_turn)
    except:
        return None

def generate_moves(state):
    moves = []
    pile = state.pile

    move_order = [
        ('2', 'red'),   # 2 red
        ('2', 'blue'),  # 2 blue
        ('1', 'red'),   # 1 red
        ('1', 'blue')   # 1 blue
    ]

    for amount, color in move_order:
        new_state = try_move(state, amount, color)
        if new_state:
            moves.append((amount, color, new_state))
    return moves


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

def player_choosing_marbles(pile, choice, pile_name):
    if choice == '1':
        if (remove_two_marbles(pile, 'red', player_marbles) != -1):
            computer_turn(pile, pile_name)
    elif choice == '2':
        if (remove_two_marbles(pile, 'blue', player_marbles) != -1):
            computer_turn(pile, pile_name)
    elif choice == '3':
        if (remove_one_marble(pile, 'red', player_marbles) != -1 ):
            computer_turn(pile, pile_name)
    elif choice == '4':
        if (remove_one_marble(pile, 'blue', player_marbles) != -1):
            computer_turn(pile, pile_name)
    elif choice == 'q':
        return 'quit'
    else:
        print("Invalid choice.")


def calculate_standard_score(marbles, score):
    for marble in marbles:
        if marble == 'red':
            # print("red is in")
            score -= 2
        elif marble == 'blue':
            # print("blue is in")
            score -= 1
    return score

def computer_turn(pile_contents, pile_name):
    print("COM is thinking...")
    # time.sleep(2); #will be removed in final version
    state = GameState(pile_contents, player_marbles, computer_marbles, True)
    _, best_move = minimax(state, depth=4, alpha=-float('inf'), beta=float('inf'))

    if best_move is None:
        print("COM cannot make a move.")
        return

    amount, color = best_move
    print(f"COM chooses to pick {amount} {color} marble(s) from {pile_name}" ) #HERE

    if amount == '2':
        remove_two_marbles(pile_contents, color, computer_marbles)
    elif amount == '1':
        remove_one_marble(pile_contents, color, computer_marbles)
    print("COM has chosen")

#REMINDER: beta should be pos infinity , and alpha should be neg infinity for worst possible options
def minimax(state, depth, alpha, beta):
    if depth == 0 or state.is_terminal():
        return state.get_score(), None

    if state.is_max_turn:
        max_eval = -float('inf')
        best_move = None
        for amount, color, new_state in generate_moves(state):
            eval_score, _ = minimax(new_state, depth - 1, alpha, beta)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (amount, color)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for amount, color, new_state in generate_moves(state):
            eval_score, _ = minimax(new_state, depth - 1, alpha, beta)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (amount, color)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

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

def remove_two_marbles(pile, color, player):
    # scan = print("You've picked 2", color ,"marbles")
    if (has_duplicates(pile, color)):
        player.append(color)
        player.append(color)
        pile.remove(color)
        pile.remove(color)
        print("Pile now has:", len(pile), "rocks left")
        return;
    else:
        print("Not enough", color ,"marbles. Try Again!")
        return -1;

def remove_one_marble(pile, color, player):
    # print("You've picked 1 red marble")
    if (color in pile):
        player.append(color)
        pile.remove(color)
        print("Pile now has:", len(pile), "rocks left")
        return
    else:
        print("Not enough", color, "marbles")
        return -1;

def standard(pile_1, pile_2):
    print("This will be Standard")
    global player_score
    while True:

        if (len(pile_1) == 0 or len(pile_2) == 0): #lose behavior
            player_score = calculate_standard_score(player_marbles, player_score)
            print("Pile is empty");
            print("You lose!")
            print("Player score is", player_score )
            break

        print("Player 1: Your Turn")
        print("1. Choose Pile 1")
        print("2. Choose Pile 2")
        print("3. Look at Pile")
        print("4. Number of Points")
        scan = input("Enter q to exit\n")


        if scan == 'q':
            break
        if scan == '1': # choose pile 1
            print("You've chosen Pile 1:")
            display_player_choice()
            choice = input("\n")
            if player_choosing_marbles(pile_1, choice, "Pile 1") == 'quit':
                break
        elif scan == '2': # choose pile 2
            print("You've chosen Pile 2:\n")
            display_player_choice()
            choice = input("\n")
            if player_choosing_marbles(pile_2, choice, "Pile 2") == 'quit':
                break
        elif scan == '3': # display pile
            print("Pile 1: ", pile_1)
            print("Pile 2: ", pile_2)
        elif scan == '4': # display score
            print("Player Marbles:\n",player_marbles)
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
