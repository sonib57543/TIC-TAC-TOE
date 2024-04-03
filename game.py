from player import HumanPlayer, RandomComputerPlayer  # Import player classes from player.py

class TicTacToe:  # Corrected the class name to "TicTacToe"
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize the board with empty spaces
        self.current_winner = None  # Initialize the current winner as None

    def print_board(self):
        # Print the current state of the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        # Print the board with numbers representing each position
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        # Return a list of available moves (indices of empty spaces)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Check if there are any empty squares left on the board
        return ' ' in self.board

    def num_empty_squares(self):
        # Return the number of empty squares left on the board
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Make a move on the board if the chosen square is empty
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.is_winner(square, letter):  # Check if the player wins after making the move
                self.current_winner = letter
            return True  # Return True if the move is valid
        return False  # Return False if the move is invalid

    def is_winner(self, square, letter):
        # Check if the player wins after making a move
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):  # Check the row
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):  # Check the column
            return True

        if square % 2 == 0:  # Check diagonals if the square is on a diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False  # Return False if no winning condition is met

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Start the game with player X
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  # Switch players after each move

    if print_game:
        print("It's a tie!")  # Print tie message if the game ends in a tie

# Main program
if __name__ == '__main__':
    x_player = HumanPlayer('X')  # Create a human player with letter X
    o_player = RandomComputerPlayer('O')  # Create a random computer player with letter O
    tictactoe = TicTacToe()  # Create a TicTacToe game instance
    play(tictactoe, x_player, o_player, print_game=True)  # Start the game with the specified players
