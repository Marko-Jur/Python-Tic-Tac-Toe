# Project: TicTacToe
# Version: 09
# Author: Marko Jurisic
# Date: 29 April 2019


# Importing Libraries
import tkinter
from tkinter import *
import pygame
from functools import partial # Used so that button widget commands can take arguments also
import time
import random
 
#Declaring global variables:
##Images
MAINSCREEN = 'heading.gif' # Image for mainscreen
MAINFLASH = 'grey' # Flash main buttons
MAINBUTTON = 'button2.png'# Image for main button
BOARD = 'Board.gif' # Board
X = 'P.gif'
O = 'Y.gif'
XHORIZONTALWINLINE = 'Xline.png'
XVERTICALWINLINE = 'Xlinev.png'
XRLWINLINE = 'Xrl.png'
XLRWINLINE = 'Xlr.png'
OHORIZONTALWINLINE = 'XBHline1.png'
OVERTICALWINLINE = 'XBline1.png'
ORLWINLINE = 'XBline1RL.png'
OLRWINLINE = 'Olr.png' 
ORLWINLINE = 'Orl.png' 

BACKBUTTON = 'back1.png'
PLAYER1 = 'player11.png'
PLAYER2 = 'player22.png'
PLAYER2LINE = 'bline.png'
PLAYER1LINE = 'rline.png'

##Numbers for scores
B0 = 'b0.png'
B1 = 'b1.png'
B2 = 'b2.png'
B3 = 'b3.png'
B4 = 'b4.png'
B5 = 'b5.png'
B6 = 'b6.png'
B7 = 'b7.png'
B8 = 'b8.png'
B9 = 'b9.png'

R0 = 'r0.png'
R1 = 'r1.png'
R2 = 'r2.png'
R3 = 'r3.png'
R4 = 'r4.png'
R5 = 'r5.png'
R6 = 'r6.png'
R7 = 'r7.png'
R8 = 'r8.png'
R9 = 'r9.png'

####Variables
GAMEMODE = 0
TURN = 0
BOARDSQUARES = [0,0,0,0,0,0,0,0,0]
PLAYER1WINS = 0
PLAYER2WINS = 0
DRAW = 0
GAMESWITCHCOM = 1



# Function: FullScreenApp   
# Purpose: Make window size size of the screen
# Input: object
# Output: none
#Function taken from: https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

# Function: clearScreen
# Purpose: Clears the screen
# Input: none
# Output: none
def clearScreen():

    #Clearing everyhing
    ScreenCoverup = Label(window,width = 1500, height = 2000, background = 'white')
    ScreenCoverup.place(x = 0,y = 0)
    window.update()

# Function: checkForWin
# Purpose: Checks if someone has won game
# Input: none
# Output: none    
def checkForWin():

    global BOARDSQUARES                                          
    global PLAYER1WINS                                                      
    global PLAYER2WINS  
    global DRAW 
    global TURN
    global GAMEMODE
    global GAMESWITCHCOM

    #Variable for setting if someone wins
    winFlag = 0 

    #Checking for win sets:
    #First Row: 
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[1] == 'X' and BOARDSQUARES[2] == 'X'): 
        winFlag = 1
        PLAYER1WINS +=1
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[1] == 'O' and BOARDSQUARES[2] == 'O'):
        winFlag = 11
        PLAYER2WINS +=1

    #Second row
    if (BOARDSQUARES[3] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[5] == 'X'):
         winFlag = 2
         PLAYER1WINS +=1

    if  (BOARDSQUARES[3] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[5] == 'O'):
        winFlag = 12
        PLAYER2WINS +=1

    #Third row
    if (BOARDSQUARES[6] == 'X' and BOARDSQUARES[7] == 'X' and BOARDSQUARES[8] == 'X'): 
         winFlag = 3
         PLAYER1WINS +=1
    if (BOARDSQUARES[6] == 'O' and BOARDSQUARES[7] == 'O' and BOARDSQUARES[8] == 'O'):
        winFlag = 13
        PLAYER2WINS +=1

    #First Column
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[3] == 'X' and BOARDSQUARES[6] == 'X'):
         winFlag = 4
         PLAYER1WINS +=1
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[3] == 'O' and BOARDSQUARES[6] == 'O'):
        winFlag = 14
        PLAYER2WINS +=1

    #Second Column
    if (BOARDSQUARES[1] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[7] == 'X'):
         winFlag = 5
         PLAYER1WINS +=1
    if (BOARDSQUARES[1] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[7] == 'O'):
        winFlag = 15
        PLAYER2WINS +=1

    #Third Column
    if (BOARDSQUARES[2] == 'X' and BOARDSQUARES[5] == 'X' and BOARDSQUARES[8] == 'X'):
        winFlag = 6
        PLAYER1WINS +=1
    if (BOARDSQUARES[2] == 'O' and BOARDSQUARES[5] == 'O' and BOARDSQUARES[8] == 'O'):
        winFlag = 16
        PLAYER2WINS +=1

    #Left to right diagnol
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[8] == 'X'):
         winFlag = 7
         PLAYER1WINS +=1
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[8] == 'O'):
        winFlag = 17
        PLAYER2WINS +=1
    #Right to left Diagnol
    if (BOARDSQUARES[2] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[6] == 'X'):
         winFlag = 8
         PLAYER1WINS +=1
    if (BOARDSQUARES[2] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[6] == 'O'):
        winFlag = 18
        PLAYER2WINS +=1

    # Creating images for win

    #Drwaing throughs for sets of 3
    if winFlag == 1:
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XHORIZONTALWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 330, y = 120)
        window.update()
        time.sleep(1.6)
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        drawBoard()

    if winFlag == 2:
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XHORIZONTALWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 330, y = 340)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 3:
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XHORIZONTALWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 330, y = 580)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 4:
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XVERTICALWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 450, y = 0)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 5:
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XVERTICALWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 680, y =0)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 6:
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XVERTICALWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 940, y = 0)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()
    
    if winFlag == 7: 
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XLRWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 390, y = 65)
        Xwin3 = Label(window, image = Xwin).place(x = 610, y = 290)
        Xwin4 = Label(window, image = Xwin).place(x = 820, y = 540)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 8: 
        DRAW = 0 
        time.sleep(0.5)
        Xwin = PhotoImage(file = XRLWINLINE)
        Xwin2 = Label(window, image = Xwin).place(x = 850, y = 65)
        Xwin3 = Label(window, image = Xwin).place(x = 610, y = 281)
        Xwin4 = Label(window, image = Xwin).place(x = 360, y = 510)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 11:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OHORIZONTALWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 300, y = 140)
        window.update()
        time.sleep(1)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 12:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OHORIZONTALWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 300, y = 370)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 13:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OHORIZONTALWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 300, y = 600)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 14:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OVERTICALWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 465, y = 10)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 15:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OVERTICALWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 690, y = 10)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 16:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OVERTICALWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 920, y = 10)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 17:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = OLRWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 400, y = 65)
        Owin3 = Label(window, image = Owin).place(x = 620, y = 290)
        Owin4 = Label(window, image = Owin).place(x = 830, y = 535)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    if winFlag == 18:
        DRAW = 0 
        time.sleep(0.5)
        Owin = PhotoImage(file = ORLWINLINE)
        Owin2 = Label(window, image = Owin).place(x = 865, y = 70)
        Owin3 = Label(window, image = Owin).place(x = 620, y = 285)
        Owin4 = Label(window, image = Owin).place(x = 370, y = 505)
        window.update()
        time.sleep(1.6)
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0
        winFlag = 0
        drawBoard()

    #Checking for draw and exitting
    DRAW += 1
    if DRAW == 9:
        DRAW = 0
        #Reset GAMESWITCH, so that previous player second player is now first to move
        if GAMESWITCHCOM == 1:
            GAMESWITCHCOM = 0
        else:
            GAMESWITCHCOM = 1
        #resets turn for COM game
        TURN = 0 
        time.sleep(1.2)
        drawBoard()


    
    window.update()
    #window.mainloop() # UNCOMMENT IF STUFF STOPS WORKING
    # drawBoard()

# Function: smartComAttack
# Purpose: chooses the attacking coms choice
# Input: none
# Output: none
def smartComAttack():

    global BOARDSQUARES

    attackFlag = 0
    choice = 1

    #Horizontal blocking end
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[1] == 'O' and BOARDSQUARES[2] != 'X'):
        choice = 2
        attackFlag = 1
    if (BOARDSQUARES[3] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[5] != 'X'):
        choice = 5
        attackFlag = 1
    if (BOARDSQUARES[6] == 'O' and BOARDSQUARES[7] == 'O' and BOARDSQUARES[8] != 'X'):
        choice = 8
        attackFlag = 1
    #Horizontal Blocking middle
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[2] == 'O' and BOARDSQUARES[1] != 'X'):
        choice = 1
        attackFlag = 1
    if (BOARDSQUARES[3] == 'O' and BOARDSQUARES[5] == 'O' and BOARDSQUARES[4] != 'X'):
        choice = 4
        attackFlag = 1
    if (BOARDSQUARES[6] == 'O' and BOARDSQUARES[8] == 'O' and BOARDSQUARES[7] != 'X'):
        choice = 7
        attackFlag = 1

    #Horizontal Blocking start
    if (BOARDSQUARES[1] == 'O' and BOARDSQUARES[2] == 'O' and BOARDSQUARES[0] != 'X'):
        choice = 0
        attackFlag = 1
    if (BOARDSQUARES[4] == 'O' and BOARDSQUARES[5] == 'O' and BOARDSQUARES[3] != 'X'):
        choice = 3
    if (BOARDSQUARES[7] == 'O' and BOARDSQUARES[8] == 'O' and BOARDSQUARES[6] != 'X'):
        choice = 6
        attackFlag = 1

    #Vertical Blocking start
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[3] == 'O' and BOARDSQUARES[6] != 'X'):
        choice = 6
        attackFlag = 1
    if (BOARDSQUARES[1] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[7] != 'X'):
        choice = 7
        attackFlag = 1
    if (BOARDSQUARES[2] == 'O' and BOARDSQUARES[5] == 'O' and BOARDSQUARES[8] != 'X'):
        choice = 8
        attackFlag = 1

    #Vertical Blocking middle
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[6] == 'O' and BOARDSQUARES[3] != 'X'):
        choice = 3
        attackFlag = 1
    if (BOARDSQUARES[1] == 'O' and BOARDSQUARES[7] == 'O' and BOARDSQUARES[4] != 'X'):
        choice = 4
        attackFlag = 1
    if (BOARDSQUARES[2] == 'O' and BOARDSQUARES[8] == 'O' and BOARDSQUARES[5] != 'X'):
        choice = 5
        attackFlag = 1

    #Vertical Blocking end
    if (BOARDSQUARES[3] == 'O' and BOARDSQUARES[6] == 'O' and BOARDSQUARES[0] != 'X'):
        choice = 0
        attackFlag = 1
    if (BOARDSQUARES[4] == 'O' and BOARDSQUARES[7] == 'O' and BOARDSQUARES[1] != 'X'):
        choice = 1
        attackFlag = 1
    if (BOARDSQUARES[5] == 'O' and BOARDSQUARES[8] == 'O' and BOARDSQUARES[2] != 'X'):
        choice = 2
        attackFlag = 1

    #Diagnol blocking end
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[8] != 'X'):
        choice = 8
        attackFlag = 1
    if (BOARDSQUARES[2] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[6] != 'X'):
        choice = 6
        attackFlag = 1
    #Diagnol blocking middle
    if (BOARDSQUARES[0] == 'O' and BOARDSQUARES[8] == 'O' and BOARDSQUARES[4] != 'X'):
        choice = 4
        attackFlag = 1
    if (BOARDSQUARES[2] == 'O' and BOARDSQUARES[6] == 'O' and BOARDSQUARES[4] != 'X'):
        choice = 4
        attackFlag = 1
    #Diagnol blocking start
    if (BOARDSQUARES[8] == 'O' and BOARDSQUARES[4] == 'O' and BOARDSQUARES[0] != 'X'):
        choice = 0
        attackFlag = 1
    if (BOARDSQUARES[4] == 'O' and BOARDSQUARES[6] == 'O' and BOARDSQUARES[2] != 'X'):
        choice = 2
        attackFlag = 1




    return choice,attackFlag

# Function: smartComDefence
# Purpose: makes better decisions
# Input: none
# Output: none
def smartComDefence():

    global BOARDSQUARES

    defendFlag = 0
    choice = 10

    #Horizontal blocking end
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[1] == 'X' and BOARDSQUARES[2] != 'O'):
        choice = 2
        defendFlag = 1
    if (BOARDSQUARES[3] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[5] != 'O'):
        choice = 5
        defendFlag = 1
    if (BOARDSQUARES[6] == 'X' and BOARDSQUARES[7] == 'X' and BOARDSQUARES[8] != 'O'):
        choice = 8
        defendFlag = 1
    #Horizontal Blocking middle
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[2] == 'X' and BOARDSQUARES[1] != 'O'):
        choice = 1
        defendFlag = 1
    if (BOARDSQUARES[3] == 'X' and BOARDSQUARES[5] == 'X' and BOARDSQUARES[4] != 'O'):
        choice = 4
        defendFlag = 1
    if (BOARDSQUARES[6] == 'X' and BOARDSQUARES[8] == 'X' and BOARDSQUARES[7] != 'O'):
        choice = 7
        defendFlag = 1

    #Horizontal Blocking start
    if (BOARDSQUARES[1] == 'X' and BOARDSQUARES[2] == 'X' and BOARDSQUARES[0] != 'O'):
        choice = 0
        defendFlag = 1
    if (BOARDSQUARES[4] == 'X' and BOARDSQUARES[5] == 'X' and BOARDSQUARES[3] != 'O'):
        choice = 3
        defendFlag = 1
    if (BOARDSQUARES[7] == 'X' and BOARDSQUARES[8] == 'X' and BOARDSQUARES[6] != 'O'):
        choice = 6
        defendFlag = 1

    #Vertical Blocking start
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[3] == 'X' and BOARDSQUARES[6] != 'O'):
        choice = 6
        defendFlag = 1
    if (BOARDSQUARES[1] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[7] != 'O'):
        choice = 7
        defendFlag = 1
    if (BOARDSQUARES[2] == 'X' and BOARDSQUARES[5] == 'X' and BOARDSQUARES[8] != 'O'):
        choice = 8
        defendFlag = 1

    #Vertical Blocking middle
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[6] == 'X' and BOARDSQUARES[3] != 'O'):
        choice = 3
        defendFlag = 1
    if (BOARDSQUARES[1] == 'X' and BOARDSQUARES[7] == 'X' and BOARDSQUARES[4] != 'O'):
        choice = 4
        defendFlag = 1
    if (BOARDSQUARES[2] == 'X' and BOARDSQUARES[8] == 'X' and BOARDSQUARES[5] != 'O'):
        choice = 5
        defendFlag = 1

    #Vertical Blocking end
    if (BOARDSQUARES[3] == 'X' and BOARDSQUARES[6] == 'X' and BOARDSQUARES[0] != 'O'):
        choice = 0
        defendFlag = 1
    if (BOARDSQUARES[4] == 'X' and BOARDSQUARES[7] == 'X' and BOARDSQUARES[1] != 'O'):
        choice = 1
        defendFlag = 1
    if (BOARDSQUARES[5] == 'X' and BOARDSQUARES[8] == 'X' and BOARDSQUARES[2] != 'O'):
        choice = 2
        defendFlag = 1

    #Diagnol blocking end
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[8] != 'O'):
        choice = 8
        defendFlag = 1
    if (BOARDSQUARES[2] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[6] != 'O'):
        choice = 6
        defendFlag = 1
    #Diagnol blocking middle
    if (BOARDSQUARES[0] == 'X' and BOARDSQUARES[8] == 'X' and BOARDSQUARES[4] != 'O'):
        choice = 4
        defendFlag = 1
    if (BOARDSQUARES[2] == 'X' and BOARDSQUARES[6] == 'X' and BOARDSQUARES[4] != 'O'):
        choice = 4
        defendFlag = 1
    #Diagnol blocking start
    if (BOARDSQUARES[8] == 'X' and BOARDSQUARES[4] == 'X' and BOARDSQUARES[0] != 'O'):
        choice = 0
        defendFlag = 1
    if (BOARDSQUARES[4] == 'X' and BOARDSQUARES[6] == 'X' and BOARDSQUARES[2] != 'O'):
        choice = 2
        defendFlag = 1




    return choice,defendFlag

# Function: consultCom
# Purpose: chooses the coms choice
# Input: none
# Output: none
def consultCom():
    
    global TURN
    global BOARDSQUARES
    choice = 0

    if TURN == 0:
        #getting random number for first choice
        choice = random.randint(0,8)
        print("random1")
        while BOARDSQUARES[choice] == 'X' or BOARDSQUARES[choice] =='O':
            choice = random.randint(0,8)
            print("random2")
             
    
    #elif TURN == 1:
        #choice = 1
    else:
        #Attack first, if not possible to attack, then defend
        choice, attackFlag = smartComAttack()
        if attackFlag == 0:
            choice, defendFlag = smartComDefence()
            print('defending')
            if defendFlag == 0:
                choice = random.randint(0,8)
                while BOARDSQUARES[choice] == 'X' or BOARDSQUARES[choice] =='O':
                    choice = random.randint(0,8)
                print('random3')
            #Placing the choice into list
            BOARDSQUARES[choice] = 'O'
        else:
            BOARDSQUARES[choice] = 'O'
            print('attacking')

    #print(choice)
    return choice



# Function: updateSquareCom
# Purpose: Updates the square that the player picks
# Input: xsquare, ysquare, position global TURN - these are the locations of the sqaure, and the turn of the player, and which square it is
# Output: none
def updateSquareCom(xsquare,ysquare,position):
    
    #Finding whose turn it is
    global TURN
    global BOARDSQUARES
    global GAMESWITCHCOM
    
    if BOARDSQUARES[position] == 'X' or BOARDSQUARES[position] == 'O':
        playGameCom()
    
    #if GAMESWITCHCOM == 1:
        #TURN += 1
        #GAMESWITCHCOM = 0
        #consultCom()


    #Setting up images
    Xplayer = PhotoImage(file = X)
    Oplayer = PhotoImage(file = O)

    #Correcting some position issues:
    if xsquare == 600:
        xsquare = 580
        ysquare = 525
    if xsquare == 840:
        ysquare = 285
    if ysquare == 281:
        ysquare = 290
        xsquare = 605

    
    #Putting in value accoridng to who's turn it is
    if TURN % 1 == 0:
        if GAMESWITCHCOM == 0:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Xplayer)
            square.place(x=xsquare + 30,y=ysquare)
            BOARDSQUARES[position] = 'X'
            window.update()
            checkForWin()

            time.sleep(0.7)
            choice = consultCom()
        else:
            GAMESWITCHCOM = 0 ###################
            choice = consultCom() ##########
            
        
        
        
        #drawing shapes based on computer choice
        if choice == 0:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 380 + 30 ,y=65)
            BOARDSQUARES[choice] = 'O'
            

        if choice == 1:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 610 + 30 ,y=70)
            BOARDSQUARES[choice] = 'O'
            

        if choice == 2:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 850 + 30 ,y=65)
            BOARDSQUARES[choice] = 'O'
            
        
        if choice == 3:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 360 + 30 ,y=280)
            BOARDSQUARES[choice] = 'O'

        if choice == 4:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 605 + 30 ,y=290)
            BOARDSQUARES[choice] = 'O'

        if choice == 5:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 840 + 30 ,y=285)
            BOARDSQUARES[choice] = 'O'

        if choice == 6:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 360 + 30 ,y=510)
            BOARDSQUARES[choice] = 'O'

        if choice == 7:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 580 + 30 ,y=525)
            BOARDSQUARES[choice] = 'O'

        if choice == 8:
            square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
            square.place(x= 810 + 30 ,y=530)
            BOARDSQUARES[choice] = 'O'


    TURN += 1
    
    window.update()

    #Check if someone has won the set
    checkForWin()


    window.mainloop()

# Function: playGameCom
# Purpose: Sets up the sqaures, and let's users click the squares
# Input: none
# Output: none
def playGameCom():
    
    global TURN
    global GAMESWITCHCOM

    #Create buttons for each square. Change backgrounds to blue for checking where they are
    square1x = 380
    square1y = 65 
    square1 = Button(window, width = 28, height = 12, background = 'white', bd = 0,command = partial(updateSquareCom,square1x,square1y,0)) 
    square1.place(x=square1x,y=square1y)
        
    square2x = 610
    square2y = 70
    square2 = Button(window, width = 29, height = 12, background = 'white', bd = 0,command = partial(updateSquareCom,square2x,square2y,1))
    square2.place(x=square2x,y=square2y)

    square3x = 850
    square3y = 65
    square3 = Button(window, width = 31, height = 12, background = 'white', bd = 0,command = partial(updateSquareCom,square3x,square3y,2))
    square3.place(x=square3x,y=square3y)

    square4x = 360
    square4y = 280
    square4 = Button(window, width = 31, height = 13, background = 'white', bd = 0,command = partial(updateSquareCom,square4x,square4y,3))
    square4.place(x=square4x,y=square4y)

    square5x = 610
    square5y = 281
    square5 = Button(window, width = 26, height = 13, background = 'white', bd = 0,command = partial(updateSquareCom,square5x,square5y,4))
    square5.place(x=square5x,y=square5y)

    square6x = 840
    square6y = 275
    square6 = Button(window, width = 35, height = 14, background = 'white', bd = 0,command = partial(updateSquareCom,square6x,square6y,5))
    square6.place(x=square6x,y=square6y)

    square7x = 360
    square7y = 510
    square7 = Button(window, width = 26, height = 17, background = 'white', bd = 0,command = partial(updateSquareCom,square7x,square7y,6))
    square7.place(x=square7x,y=square7y)
        
    square8x = 600
    square8y = 515
    square8 = Button(window, width = 23, height = 17, background = 'white', bd = 0,command = partial(updateSquareCom,square8x,square8y,7))
    square8.place(x=square8x,y=square8y)

    square9x = 810
    square9y = 530
    square9 = Button(window, width = 38, height = 16, background = 'white', bd = 0,command = partial(updateSquareCom,square9x,square9y,8))
    square9.place(x=square9x,y=square9y)


    #Creating back button
    back = PhotoImage(file = BACKBUTTON)

    backButton = Button(window, width = 200, height = 200, background = 'white', image = back, bd = 0,command = mainMenu)
    backButton.place(x=10,y=630)

    #If the game is witched so thatt 0 
    if GAMESWITCHCOM == 1:
        updateSquareCom(square9x,square9y,8)

    window.update()
    window.mainloop()


# Function: updateSquare
# Purpose: Updates the square that the player picks
# Input: xsquare, ysquare, position global TURN - these are the locations of the sqaure, and the turn of the player, and which square it is
# Output: none
def updateSquare(xsquare,ysquare,position):
    
    #Finding whose turn it is
    global TURN
    global BOARDSQUARES
    global GAMEMODE

    #Setting up images
    Xplayer = PhotoImage(file = X)
    Oplayer = PhotoImage(file = O)

    #Correcting some position issues:
    if xsquare == 600:
        xsquare = 580
        ysquare = 525
    if xsquare == 840:
        ysquare = 285
    if ysquare == 281:
        ysquare = 290
        xsquare = 605


    #Putting in value accoridng to who's turn it is
    if TURN % 2 == 0:
        square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Xplayer)
        square.place(x=xsquare + 30,y=ysquare)
        BOARDSQUARES[position] = 'X'
    else:
        square = Button(window, width = 155, height = 165, background = 'white', bd = 0,image = Oplayer) 
        square.place(x=xsquare + 30 ,y=ysquare)
        BOARDSQUARES[position] = 'O'

    TURN += 1
    
    window.update()

    #Check if someone has won the set
    checkForWin()


    window.mainloop()

# Function: playGame
# Purpose: Sets up the sqaures, and let's users click the squares
# Input: none
# Output: none
def playGame():

    global TURN

    #Create buttons for each square. Change backgrounds to blue for checking where they are
    square1x = 380
    square1y = 65 
    square1 = Button(window, width = 28, height = 12, background = 'white', bd = 0,command = partial(updateSquare,square1x,square1y,0)) 
    square1.place(x=square1x,y=square1y)
        
    square2x = 610
    square2y = 70
    square2 = Button(window, width = 29, height = 12, background = 'white', bd = 0,command = partial(updateSquare,square2x,square2y,1))
    square2.place(x=square2x,y=square2y)

    square3x = 850
    square3y = 65
    square3 = Button(window, width = 31, height = 12, background = 'white', bd = 0,command = partial(updateSquare,square3x,square3y,2))
    square3.place(x=square3x,y=square3y)

    square4x = 360
    square4y = 280
    square4 = Button(window, width = 31, height = 13, background = 'white', bd = 0,command = partial(updateSquare,square4x,square4y,3))
    square4.place(x=square4x,y=square4y)

    square5x = 610
    square5y = 281
    square5 = Button(window, width = 26, height = 13, background = 'white', bd = 0,command = partial(updateSquare,square5x,square5y,4))
    square5.place(x=square5x,y=square5y)

    square6x = 840
    square6y = 275
    square6 = Button(window, width = 35, height = 14, background = 'white', bd = 0,command = partial(updateSquare,square6x,square6y,5))
    square6.place(x=square6x,y=square6y)

    square7x = 360
    square7y = 510
    square7 = Button(window, width = 26, height = 17, background = 'white', bd = 0,command = partial(updateSquare,square7x,square7y,6))
    square7.place(x=square7x,y=square7y)
        
    square8x = 600
    square8y = 515
    square8 = Button(window, width = 23, height = 17, background = 'white', bd = 0,command = partial(updateSquare,square8x,square8y,7))
    square8.place(x=square8x,y=square8y)

    square9x = 810
    square9y = 530
    square9 = Button(window, width = 38, height = 16, background = 'white', bd = 0,command = partial(updateSquare,square9x,square9y,8))
    square9.place(x=square9x,y=square9y)


    #Creating back button
    back = PhotoImage(file = BACKBUTTON)

    backButton = Button(window, width = 200, height = 200, background = 'white', image = back, bd = 0,command = mainMenu)
    backButton.place(x=10,y=630)


    window.update()
    window.mainloop()


# Function: drawBoard
# Purpose: Draws the board
# Input: none
# Output: none
def drawBoard():
    
    global BOARDSQUARES
    global PLAYER1WINS
    global PLAYER2WINS
    global GAMEMODE
    global GAMESWITCHCOM

    print('GAMESWITCHCOM IS ',GAMESWITCHCOM)

    clearScreen()

    #Drawing board
    board = PhotoImage(file = BOARD)
    board2 = Label(window, image = board, bg = "white") .grid(row = 0, column = 0, padx  =180, pady = 0)

    #reset the square positions
    BOARDSQUARES = [0,0,0,0,0,0,0,0,0]

    #Draw Player logos
    p1 = PhotoImage(file = PLAYER1)
    p11 = Label(window, image = p1).place(x = 60, y = 60)

    rline = PhotoImage(file = PLAYER1LINE)
    rline2 = Label(window, image = rline).place(x = 50, y = 190)

    p2 = PhotoImage(file = PLAYER2)
    p22 = Label(window, image = p2).place(x = 1200, y = 60)

    bline = PhotoImage(file = PLAYER2LINE)
    bline2 = Label(window, image = bline).place(x = 1180, y = 190)

    #Drawing player scores:
    if PLAYER1WINS == 0:
        r0 = PhotoImage(file = R0)
        r00 = Label(window, image = r0).place(x = 75, y = 250)

    if PLAYER2WINS == 0:
        b0 = PhotoImage(file = B0)
        b00 = Label(window, image = b0).place(x = 1260, y = 250)

    if PLAYER1WINS == 1:
        r1 = PhotoImage(file = R1)
        r11 = Label(window, image = r1).place(x = 75, y = 250)

    if PLAYER2WINS == 1:
        b1 = PhotoImage(file = B1)
        b11 = Label(window, image = b1).place(x = 1260, y = 250)

    if PLAYER1WINS == 2:
        r2 = PhotoImage(file = R2)
        r22 = Label(window, image = r2).place(x = 75, y = 250)

    if PLAYER2WINS == 2:
        b2 = PhotoImage(file = B2)
        b22 = Label(window, image = b2).place(x = 1260, y = 250)

    if PLAYER1WINS == 2:
        r2 = PhotoImage(file = R2)
        r22 = Label(window, image = r2).place(x = 75, y = 250)

    if PLAYER2WINS == 2:
        b2 = PhotoImage(file = B2)
        b22 = Label(window, image = b2).place(x = 1260, y = 250)


    if PLAYER1WINS == 3:
        r3 = PhotoImage(file = R3)
        r33 = Label(window, image = r3).place(x = 75, y = 250)

    if PLAYER2WINS == 3:
        b3 = PhotoImage(file = B3)
        b33 = Label(window, image = b3).place(x = 1260, y = 250)


    if PLAYER1WINS == 4:
        r4 = PhotoImage(file = R4)
        r44 = Label(window, image = r4).place(x = 75, y = 250)

    if PLAYER2WINS == 4:
        b4 = PhotoImage(file = B4)
        b44 = Label(window, image = b4).place(x = 1260, y = 250)

    if PLAYER1WINS == 5:
        r5 = PhotoImage(file = R5)
        r55 = Label(window, image = r5).place(x = 75, y = 250)

    if PLAYER2WINS == 5:
        b5 = PhotoImage(file = B5)
        b55 = Label(window, image = b5).place(x = 1260, y = 250)

    window.update()

    if GAMEMODE == 0:
        playGame()
    if GAMEMODE == 1:
        playGameCom()
    
# Function: playCom
# Purpose: changes Gamemode
# Input:
# Output:
def playCom():

    global GAMEMODE

    GAMEMODE = 1
    
    drawBoard()



# Function: mainMenu
# Purpose: Main menu for the screen
# Input: none
# Output: none
def mainMenu():
    
    #Image for heading
    mainImage = PhotoImage(file = MAINSCREEN)
    heading = Label(window, image = mainImage, bg = "white") .grid(row = 0, column = 0, padx  =180, pady = 0)

    #Adding buttons
    buttonImage = PhotoImage(file = MAINBUTTON)
    vsPlayer = Button(window,text="Player", width = 300, height = 400, background = 'white', fg = 'black', image = buttonImage, bd = 0, compound = CENTER, font=("Comic Sans MS", 32), command = drawBoard )
    vsPlayer.place(x=180,y=360)

    vsCom = Button(window,text="Com", width = 300, height = 400, background = 'white', fg = 'black', image = buttonImage, bd = 0,compound = CENTER, font=("Comic Sans MS", 32),command = playCom)
    vsCom.place(x=580,y=360)

    Online = Button(window,text="Online", width = 300, height = 400, background = 'white',  fg = 'black', image = buttonImage, bd = 0, compound = CENTER, font=("Comic Sans MS", 32))
    Online.place(x=980,y=360)

    window.update()
    window.mainloop()


#Program starts here:
#Creating window 
window = Tk()
window.title("TicTacToe")
window.configure(background="white")
full =FullScreenApp(window)





#Calling functions:
mainMenu()

