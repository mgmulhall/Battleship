#Unit Tests for Battle Ship Game

import unittest
#from pydocsDemo import *
from battleship import setupShips,isGameOver,checkHitOrMiss
import random
from pydoc import *
grid_size=10
ship_counter=0
ship_num=5
twoDarray = [ ['.']*grid_size for i in range(grid_size) ]
Over_board=[ ['.']*grid_size for i in range(grid_size) ]

class TestBattleShip(unittest.TestCase):
    ship_counter=0
    ship_num=5
    twoDarray = [ ['.']*grid_size for i in range(grid_size) ]

    def test_setupShips(self):
        #Test that there are the correct number of ships
        self.assertEqual(setupShips(twoDarray),ship_num)

        #Create board with 5 ships, the rests "."
        ships_array = [ ['.']*grid_size for i in range(grid_size) ]
        for ship in range(ship_num):
            ship_r, ship_cl=random.randint(0,grid_size-1), random.randint(0,grid_size-1)
        #Get new coordinates if ship is already there
            while ships_array[ship_r][ship_cl] =='S':
                ship_r, ship_cl = random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            ships_array[ship_r][ship_cl]='S'

        #Count dots on board
        dot_count=0
        for i in range(0,grid_size):
            for j in range (0,grid_size):
                if ships_array[i][j]=='.':
                    dot_count+=1
        
        #Test that all spots that are not ships, are dots
        #100 spots total- dot count should equal ship_num
        self.assertEqual(setupShips(ships_array),(100-dot_count))
    
    def test_isGameOver(self):
        
        #Build board with floating ships
        notOver_board=[ ['.']*grid_size for i in range(grid_size) ]
        for ship in range(ship_num):
            ship_r, ship_cl=random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            while notOver_board[ship_r][ship_cl] =='S':
                ship_r, ship_cl = random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            notOver_board[ship_r][ship_cl]='S'
        
        #Test if board with floating ships returns false
        self.assertEqual(isGameOver(notOver_board),False)

        #Build board with no floating ships
        for ship in range(ship_num):
            ship_r, ship_cl=random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            while Over_board[ship_r][ship_cl] =='X':
                ship_r, ship_cl = random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            Over_board[ship_r][ship_cl]='X'

        #Test if board with no floating ships returns true
        self.assertTrue(isGameOver(Over_board))

    def test_checkHitOrMiss(self):
        thearray=twoDarray

        #Build board with ships
        for ship in range(ship_num):
            ship_r, ship_cl=random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            while thearray[ship_r][ship_cl] =='S':
                ship_r, ship_cl = random.randint(0,grid_size-1), random.randint(0,grid_size-1)
            thearray[ship_r][ship_cl]='S'

        #Test if users guess was a hit
        self.assertEqual(checkHitOrMiss(thearray,ship_r,ship_cl),"HIT")
        
        #Find coordinates to miss
        miss_row, miss_col=random.randint(0,grid_size-1), random.randint(0,grid_size-1)
        while thearray[miss_row][miss_col] =='S':
            miss_row, ship_cl = random.randint(0,grid_size-1), random.randint(0,grid_size-1)

        #Test if users guess was a miss
        self.assertEqual(checkHitOrMiss(thearray,miss_row,miss_col),"MISS")
        
if __name__ == '__main__':
    unittest.main()