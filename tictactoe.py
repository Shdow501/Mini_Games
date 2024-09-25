
import numpy as np

# All the winning combinations for comparison
wining_combinations = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], # All row combinations
                       [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], # All column combinations
                       [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]] # Diagonal combinations

class tictactoe():
    """
    Program to play a 2 player tick tac toe game
    """

    def __init__(self):
        self.x_positions = []
        self.o_positions = []
        self.turn = "X"
        self.pos = ''
        self.check_status = False
        self.board = np.empty((3,3), dtype='str')
        self.board[:] = ' '
        self.main()

    def user_input(self):
        print(f"enter the postion you want to play ({self.turn} plays):")
        self.pos = input()
        self.pos = tuple(map(int, self.pos.split(" ")))
        if self.pos in self.x_positions or self.pos in self.o_positions:
            print("Invalid position. Position already filled!")
            self.user_input()
        if self.turn == "X":
            self.x_positions.append(self.pos)
        else:
            self.o_positions.append(self.pos)
        self.check_status = self.check_win()
    
    def check_win(self):
        while len(self.x_positions) <3:
            return False
        if len(self.x_positions) >= 3 or len(self.o_positions) >= 3:
            for combos in wining_combinations:
                if set(combos).issubset(self.x_positions) or set(combos).issubset(self.o_positions):
                    return True
        return False
    
    def printboard(self):
        for position in self.x_positions:
            self.board[position] = 'X'
        for position in self.o_positions:
            self.board[position] = 'O'
        print(self.board)
        

    def main(self):
        while not self.check_status:
            self.user_input()
            self.printboard()
            if self.check_status == True:
                print(f"{self.turn} wins!")
                break
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

# Calling the class which in turn runs the code
tictactoe()
