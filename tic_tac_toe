available_coordinates = {
    'A1': 0, 'B1': 1, 'C1': 2,
    'A2': 3, 'B2': 4, 'C2': 5,
    'A3': 6, 'B3': 7, 'C3': 8
}


winning_combinations = [
    [0, 1, 2],  # horizontal
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],  # vertical
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],  # diagonal
    [2, 4, 6]
]


class TicTacToe:
    def __init__(self):
        self.grid = {
                0: ' ', 1: ' ', 2: ' ',
                3: ' ', 4: ' ', 5: ' ',
                6: ' ', 7: ' ', 8: ' '
        }
        self.x_turns = []
        self.o_turns = []

    def print_grid(self):
        entries = [str(v) for k, v in self.grid.items()]
        lst = entries
        print("  A | B | C ")
        for row in range(3):
            print("+---+---+---+")
            [print(f"| {lst[col+row*3]} ", end=f"") for col in range(3)]
            print(f"| {row+1}")
        print("+---+---+---+")

    def find_cell(self, turn):
        cell = None
        while cell is None:
            try:
                user_input = input(f"Player {turn}, it's your turn! Where do you want to go? > ").upper()
                cell = available_coordinates[user_input]
                available_coordinates.pop(user_input)
            except Exception:
                print("Try again")
                pass
            else:
                return cell

    def take_a_turn(self, turn):
        cell = self.find_cell(turn)
        self.grid[cell] = turn
        if turn == "X":
            self.x_turns.append(cell)
        if turn == "O":
            self.o_turns.append(cell)
        self.print_grid()

    def did_you_win(self, turn):
        for combo in winning_combinations:
            lst = self.x_turns if turn == "X" else self.o_turns
            if (
                    combo[0] in lst and
                    combo[1] in lst and
                    combo[2] in lst
            ):
                return True

    def start(self):
        player_turns = ["X", "O", "X", "O", "X", "O", "X"]
        while True:

            print("let the games begin")
            self.print_grid()

            for turn in player_turns:

                self.take_a_turn(turn)
                if self.did_you_win(turn) is True:
                    print(f"{turn} is declared the WINNER!")
                    break

            if not self.want_to_play_again():
                break

            else:
                self.grid = {
                    0: ' ', 1: ' ', 2: ' ',
                    3: ' ', 4: ' ', 5: ' ',
                    6: ' ', 7: ' ', 8: ' '
                }
                self.x_turns = []
                self.o_turns = []
                continue

    def want_to_play_again(self):
        user_input = input("\nWould you like to play again? \n Yes: Y \n No: N \n > ")

        if user_input.upper() == "Y":
            return True
        else:
            print("BYE! Hope you had fun :) ")
            return False


ttt = TicTacToe()
ttt.start()
