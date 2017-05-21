#importing libraries
import sys
import os
os.system("cls") #clear screen for windows
#os.system("clear") #clear screen for linux/Mac

#create class Onboard
class Onboard():
    def __init__(self):
        #initialise a list of for values.
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #class method dispay to dispay values
    def dispay(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    #update function for players to start play the game
    def update_box(self, cell_no, player):
        if self.cells[cell_no] == " ": #prevent value override
            self.cells[cell_no] = player

    #function for winner X:
    def winner(self, player):
        #check for first row:
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        #check for second row:
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        #check for third row:
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        #check for fourth row:
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        #check for five row:
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        #check for sixth row:
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        #check for seventh row:
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        #check for eight row:
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

        return False

    #check for tie game by looking into cells
    #we check for tie after win coz the board can be full
    #but there's no win space.
    #we check for each cell if is fill wen all 9 are filled and no winner
    #we assume is a tie
    def tie_game(self):
        used_boxes = 0
        for cell in self.cells:
            if cell != " ":
                used_boxes += 1
        if used_boxes == 9:
            return True
        else:
            return False


    #function for resetting the game:
    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#create instance of Onboad class outside to dispay the values
board = Onboard()
#board.dispay()

#create function header to print welcome msg
def print_header():
    #welcome message
    print("Welcome to Our Tic Tac Toe Game")

def refresh_screen():
    #clear the screen again
    os.system('cls')

    #print the header message
    print_header()

    #show the board
    board.dispay()

#create a loop
while True:
    refresh_screen()

    #PLAYER X
    #Gets x input from player to start first with X for python 2.7 use (raw_input)
    x_choice = int(input("\nX) Please choose number 1 - 9. >"))
    #create a method to update the takes two args the choice &
    board.update_box(x_choice, "X")

    #refresh screen
    refresh_screen()

    #check for winner for player X and ask your to play again
    if board.winner("X"):
        print("\nCongrats X Wins!!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    #check for tie game for player X and ask your to play again
    if board.tie_game():
        print("\nSorry The Game is Tie! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    #PLAYER O
    #We need to refresh for value to be stored in memory b4 2nd player player
    refresh_screen()
    #Gets O input from player Two to start first with O
    o_choice = int(input("\nO) Please choose number 1 - 9. >"))
    board.update_box(o_choice, "O")

    #refresh screen
    refresh_screen()

    #check for winner O and ask your to play again
    if board.winner("O"):
        print("\nCongrats O Wins!!")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    #check for tie game for player O and ask your to play again
    if board.tie_game():
        print("\nSorry The Game is Tie! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
