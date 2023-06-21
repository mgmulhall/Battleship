# #Maggie Mulhall
# #Battleship Game

# #Initial set up
import random
grid_size = 10
ship_num=5
twoDarray = [ ['.']*grid_size for i in range(grid_size) ]

#Display game title and legend
def welcome():
    print("\nWelcome to BattleShip! \nGuess coordinates of ships until all are sunk!")
    print("\n Ship (unsunk): S \n Missed Guess: O \n Sunk Ship: X\n")

#Display the game grid (with out ships)
def displayArray(thearray):
    print('  0 1 2 3 4 5 6 7 8 9')
    row_num=1
    for row in thearray:
        print("%d|%s|" % (row_num-1, "|".join(row)))
        row_num +=1

#Place ships on board randomly 
def setupShips(thearray):
    twoDarray = [ ['.']*grid_size for i in range(grid_size) ]
    for ship in range(ship_num):
        ship_r, ship_cl=random.randint(0,grid_size-1), random.randint(0,grid_size-1)
        #Get new coordinates if ship is already there
        while thearray[ship_r][ship_cl] =='S':
            ship_r, ship_cl = random.randint(0,grid_size-1), random.randint(0,grid_size-1)
        thearray[ship_r][ship_cl]='S'

    return ship+1
  
#Prompt player for guess and process it
def guess(thearray):
    hits=0
    while isGameOver(thearray)==False:
        #Get and verify row input
        while True:
            row_guess=input("guess a row: ")
            row_guess=verify(row_guess)
            if row_guess!=-1:
                break
            else: print("Invalid Entry, Try again!")

        #Get and verify column input
        while True:
            col_guess=input("guess a column: ")
            col_guess=verify(col_guess)
            if col_guess!=-1:
                break
            else: print("Invalid Entry, Try again!")
        
        #Determine if guess is correct
        result=checkHitOrMiss(thearray,row_guess,col_guess)
        print(result)
        #After guess is processed, show updated board
        displayArray(thearray)

#   Exit when all ships are sunk 
    isGameOver(thearray)
    print("GAME OVER!!")

#Determine if the game is over by searching for all sunken ships
def isGameOver(thearray):
    hits=0
    for i in range(0,grid_size):
        for j in range (0,grid_size):
            if thearray[i][j]=='X':
                hits+=1
    if hits<ship_num:
        return False
    else:
        return True

#Determine if guess was a hit or miss
#Update the board accordingly
def checkHitOrMiss(thearray,row_guess,col_guess):
    if(thearray[row_guess][col_guess]=='S'):
            thearray[row_guess][col_guess]='X'
            return('HIT')
    elif(thearray[row_guess][col_guess]=='O'):
        print("You already missed that spot")
        return("MISS")
    elif(thearray[row_guess][col_guess]=='X'):
        print("You already hit that spot.")
        return("HIT")
    else:
        thearray[row_guess][col_guess]='O'
        return('MISS')

# Criteria to validate guess (row and column)
#  Guess must be a whole number between 0 and grid size
#   Return -1 if guess doesn't meet criteria 

def verify(guess):
        if guess.isdigit() and int(guess) > -1 and int(guess) <grid_size+1:
            guess=int(guess)-1
            return guess+1
        else: return -1 

#The main function
def main(thearray):
    welcome()
    setupShips(twoDarray)
    displayArray(twoDarray)
    guess(twoDarray)

#Call main function to start game
if __name__ == "__main__":
   main(twoDarray)