# Tic-Tac-Toe (A1..C3) with EASY or HARD difficulty

import math
import random

ROWS = ["A", "B", "C"]
COLS = ["1", "2", "3"]

def idx_from_coord(coord: str):
    coord = coord.strip().upper()
    if len(coord) != 2:
        return None
    r, c = coord[0], coord[1]
    if r not in ROWS or c not in COLS:
        return None
    return ROWS.index(r) * 3 + COLS.index(c)

def coord_from_idx(i: int):
    return f"{ROWS[i//3]}{COLS[i%3]}"

def print_board(board):
    print()
    print("   1   2   3")
    for r in range(3):
        row_label = ROWS[r]
        row_cells = [board[r*3 + c] if board[r*3 + c] != " " else " " for c in range(3)]
        print(f"{row_label}  {row_cells[0]} | {row_cells[1]} | {row_cells[2]}")
        if r < 2:
            print("  ---+---+---")
    print()

WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "DRAW"
    return None

def available_moves(board):
    return [i for i, v in enumerate(board) if v == " "]

# ------------------------- HARD MODE (minimax) --------------------
def minimax(board, player, maximizing_symbol, minimizing_symbol):
    winner = check_winner(board)

    if winner == maximizing_symbol:
        return (1, None)
    if winner == minimizing_symbol:
        return (-1, None)
    if winner == "DRAW":
        return (0, None)

    moves = available_moves(board)

    if player == maximizing_symbol:
        best_score = -math.inf
        best_move = None
        for m in moves:
            board[m] = player
            score, _ = minimax(board, minimizing_symbol, maximizing_symbol, minimizing_symbol)
            board[m] = " "
            if score > best_score:
                best_score = score
                best_move = m
        return (best_score, best_move)
    else:
        best_score = math.inf
        best_move = None
        for m in moves:
            board[m] = player
            score, _ = minimax(board, maximizing_symbol, maximizing_symbol, minimizing_symbol)
            board[m] = " "
            if score < best_score:
                best_score = score
                best_move = m
        return (best_score, best_move)

# ------------------------- EASY MODE (random) ---------------------
def easy_move(board):
    return random.choice(available_moves(board))

# ------------------------- Choose Based on Difficulty --------------
def computer_move(board, comp_symbol, human_symbol, difficulty):
    if difficulty == "hard":
        _, move = minimax(board, comp_symbol, comp_symbol, human_symbol)
        return move
    else:  # easy mode
        return easy_move(board)

# ------------------------------------------------------------------
def main():
    print("Welcome to Tic-Tac-Toe (A1..C3)")

    # Choose symbol
    while True:
        human = input("Choose your symbol (X/O): ").strip().upper()
        if human in ("X", "O"):
            break
        print("Enter X or O only.")

    comp = "O" if human == "X" else "X"

    # Choose who starts
    start = input("Do you want to start first? (yes/no): ").strip().lower()
    human_turn = True if start == "yes" else False

    # Choose difficulty
    while True:
        diff = input("Choose difficulty (easy / hard): ").strip().lower()
        if diff in ("easy", "hard"):
            break
        print("Enter 'easy' or 'hard'.")

    board = [" "] * 9
    print_board(board)

    while True:
        if human_turn:
            while True:
                move = input("Enter coordinate to play (A1..C3): ").strip().upper()
                idx = idx_from_coord(move)
                if idx is None:
                    print("Invalid input. Try again.")
                    continue
                if board[idx] != " ":
                    print("That location is already filled.")
                    continue
                board[idx] = human
                break

            print_board(board)

        else:
            print("Computer is thinking...")
            idx = computer_move(board, comp, human, diff)
            board[idx] = comp
            print(f"Computer plays {coord_from_idx(idx)}")
            print_board(board)

        # Check winner
        result = check_winner(board)
        if result:
            if result == human:
                print("You won")
            elif result == comp:
                print("Computer won")
            else:
                print("It's a draw!")
            break

        human_turn = not human_turn


if __name__ == "__main__":
    main()
