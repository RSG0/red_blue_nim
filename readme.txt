Name: Abubakar Kassim
UTA ID: 1002158809

Programming Language: 
    Python
Python Version: 
    Python3 (3.13.5)

How the code is structured:
The script implements a version of the two-player turn-based game called Red Blue Nim. Where you as the player complete against a computer that utilizes the Minimax algorithm with alpha-beta pruning to make decisisions. Below is a breakdown of the structure and flow of the program:

1. Global Variables
player_marbles = []
player_score = 0
computer_marbles = []
computer_score = 0

Stores the current state of each player's marbles and scores

2. GameState
class GameState
Captures an instance of the game state to be used primarily by the against
pile: list of marbles
player_marbles: list of marbles that the player has taken from the pile
computer_marbles: list of marbles that the computer has taken from the pile
is_max_turn: is it the computer turn?

3. Move Simulation Functions
try_move(state, amount, color)
Simulates a move and returns the new state of the game, if possible

generate_moves(state, misere=False)
Calls try_move for each possible move and returns a list of new states in priority order given by assignment.
Possible moves are dictated by whether or not the game is in misere mode.

4. Marble Assignment
assign_rocks(num_red, num_blue)
Randomly splits the red and blue marbles into two piles, and returns two lists

5. Player Move Handling
player_choosing_marbles(pile, choice, pile_name)
Calls remove_two_marbles() or remove_one_marble() depending on the player's choice and whether or not game is in misere mode, then triggers computer_turn()

6. Computer AI (Minimax)
computer_turn(pile_contents, pile_name, misere)
Uses the Minimax algorithm with alpha-beta pruning to determine the best move for the computer by constructing a GameState, depending on the game mode

minimax(state, depth, alpha, beta, misere)
Minimax algorithm with alpha-beta pruning. Returns the best move for the computer depending on the game mode
*Try to implement depth limited MinMax search* *INCOMPLETE*

7. Scoring
calculate_standard_score(marbles, score)
subtracts score for each marble taken from the piles
    Red: -2     Blue: -1
    Lower score is worse
calculate_misere_score(marbles, score)
adds score for each marble taken from the piles
    Red: +2     Blue: +1
    Lower score is better

8. Game Modes
standard(pile_1, pile_2)
The main gameplay loop for the classic version of Red Blue Nim
misere(pile_1, pile_2)
The main gameplay loop for the misere version of Red Blue Nim
Game ends when a pile is empty 


9. UI 
display_player_choice()
Displays the choices for the players to select how many marbles you would like to pick up
display_player_options()
Displays the options between choosing a pile, looking at all the remaining marbles, and view the score

10. Main Functionn
main()
Accepts command-line arguments for number of red and blue marbles, version, first-player, and depth

How the code is run: 
Format of command line arguments: 
red_blue_nim.py <num-red> <num-blue> [version] [first-player] [d]
num-red: # of red marbles to be distributed among the 2 piles (Needs to be more than 8)
num-blue: # of blue marbles to be distributed among the 2 piles (Needs to be more than 8)
version: either standard (default)  or misere '-m'
first-player: either computer goes first or human goes first '-h'
d: depth of the minimax algorithm (default 100)

To run the code open up the terminal and insert this for example:
python red_blue_nim.py 10 10 -m -h 
python red_blue_nim.py 10 12 -m -h -d 


