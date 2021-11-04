# All imports here
from random import sample
import time

empty = "#"

# Completely empty board - no numbers
# All #'s are blank spots
_board = [
        [5, 3, empty, empty, 7, empty, empty, empty, empty],
        [6, empty, empty, 1, 9, 5, empty, empty, empty],
        [empty, 9, 8, empty, empty, empty, empty, 6, empty],
        [8, empty, empty, empty, 6, empty, empty, empty, 3],
        [4, empty, empty, 8, empty, 3, empty, empty, 1],
        [7, empty, empty, empty, 2, empty, empty, empty, 6],
        [empty, 6, empty, empty, empty, empty, 2, 8, empty],
        [empty, empty, empty, 4, 1, 9, empty, empty, 5],
        [empty, empty, empty, empty, 8, empty, empty, 7, 9]
    ]


def calculate(board):

    global empty

    # Find an empty spot on the board
    find = find_empty(board)

    if not find: return True

    else: row, column = find

    # For each empty spot, check every value from 1 to 10
    for x in range(1, 10):

        if is_valid(board, x, (row, column)):

            board[row][column] = x

            # Keep trying until it works
            if calculate(board): return True

            # If nothing works, then backtrack and try new values
            board[row][column] = empty

    return False


def is_valid(board, number, position):

    # Row
    for x in range(len(board[0])):

        if board[position[0]][x] == number and position[1] != x: return False

    # Column
    for x in range(len(board)):

        if board[x][position[1]] == number and position[0] != x: return False

    # Box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for x in range(box_y * 3, box_y * 3 + 3):

        for y in range(box_x * 3, box_x * 3 + 3):

            if board[x][y] == number and (x, y) != position: return False

    return True


# Print the current state of the board
def print_board(board):

    print("")

    for x in range(len(board)):

        if x % 3 == 0 and x != 0: print("------¦-------¦------")

        for y in range(len(board[0])):

            if y % 3 == 0 and y != 0: print("¦ ", end = "")

            if y == 8: print(board[x][y])

            else: print(str(board[x][y]) + " ", end = "", sep = " ")

    print("")


# Find empty spot in sudoku board
def find_empty(board):

    global empty

    for x in range(len(board)):

        for y in range(len(board[0])):

            if board[x][y] == empty: return (x, y)

    return None

def get_board():

    global _board
    global empty

    print("Generating a random sudoku board...")

    base  = 3
    side  = base * base

    # Sudoku board pattern, based on rows and columns
    def pattern(r, c): return (base * (r % base) + r // base + c) % side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s): return sample(s, len(s)) 

    rows  = [g * base + row for g in shuffle(range(base)) for row in shuffle(range(base))] 
    columns  = [g * base + column for g in shuffle(range(base)) for column in shuffle(range(base))]

    numbers  = shuffle(range(1, base * base + 1))

    # Generate board via randomized pattern
    _board = [[numbers[pattern(r, c)] for c in columns] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties): _board[p // side][p % side] = empty

number_of_games = input("How many boards do you want to solve? ")
print("")

if number_of_games == "": number_of_games = 100
else: number_of_games = int(number_of_games)

start = time.perf_counter()

for games in range(number_of_games):

    print("-------------------------------\n")
    print("Game number: " + str(games + 1) + "/" + str(number_of_games) + "\n")
    get_board()
    print("\nOriginal board: ")
    print_board(_board)
    calculate(_board)

    print("------------------------\n")
    print("New board: ")
    print_board(_board)

stop = time.perf_counter()

time_elapsed = round((stop - start), 3)

print("All boards solved!")
print("Time elapsed: " + str(time_elapsed) + " seconds")

input("Press enter to exit...")