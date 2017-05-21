#importing libraries
import os
os.system("cls") #clear screen for windows
#os.system("clear") #clear screen for linux/Mac

#create class Onboard
class Onboard():
    def __init__(self):
        #initialise a list of for values.
        self.cells = [" ", "X", "O", "X", " ", " ", " ", " ", " ", " "]

    #function to dispay objects values
    def dispay(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

#create an object from Onboard class and dispay the values
board = Onboard()
board.dispay()
