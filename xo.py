#RAZDEV XO GAME

from tkinter import *
import random
from glob import glob



def next_turn(row, col):
    global player
    if game_cells[row][col]['text'] == "" and check_win() == False:
        if player== symbols[0]:
            game_cells[row][col]['text'] = player
            
            if check_win() == False:
                player= symbols[1]
                label.config(text=(symbols[1] + " turn"))
            elif check_win() == True:
                label.config(text=(symbols[0] + " wins!"))
            elif check_win() == 'tie':
                label.config(text=("Tie, No Winner!"))
        elif player == symbols[1]:
            game_cells[row][col]['text'] = player
            if check_win() == False:
                player = symbols[0]
                label.config(text=(symbols[0] + " turn"))
            elif check_win() == True:
                label.config(text=(symbols[1] + " wins!"))
            elif check_win() == 'tie':
                label.config(text=("Tie, No Winner!"))
#--------------------------------------------------------------------------
def isThereEmptySpaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_cells[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

#---------------------------------------------------------------------------
def check_win():
    # ******************check all horizontal conditions**********
    for row in range(3):
        if game_cells[row][0]['text'] == game_cells[row][1]['text'] == game_cells[row][2]['text'] != "":
            game_cells[row][0].config(bg="cyan")
            game_cells[row][1].config(bg="cyan")
            game_cells[row][2].config(bg="cyan")
            return True

    # *******************check all vertical conditions*********
    for col in range(3):
        if game_cells[0][col]['text'] == game_cells[1][col]['text'] == game_cells[2][col]['text'] != "":
            game_cells[0][col].config(bg="cyan")
            game_cells[1][col].config(bg="cyan")
            game_cells[2][col].config(bg="cyan")
            return True

    # *******************check diagonals conditions***************************
    if game_cells[0][0]['text'] == game_cells[1][1]['text'] == game_cells[2][2]['text'] != "":
        game_cells[0][0].config(bg="cyan")
        game_cells[1][1].config(bg="cyan")
        game_cells[2][2].config(bg="cyan")
        return True
    elif game_cells[0][2]['text'] == game_cells[1][1]['text'] == game_cells[2][0]['text'] != "":
        game_cells[0][2].config(bg="cyan")
        game_cells[1][1].config(bg="cyan")
        game_cells[2][0].config(bg="cyan")
        return True

    #******************** if there are no empty spaces left*********************
    if isThereEmptySpaces() == False:
        for row in range(3):
            for col in range(3):
                game_cells[row][col].config(bg='red')

        return 'tie'

    else:
        return False

#----------------------------------------------------------------------------
def start_newGame():
    global player
    player = random.choice(symbols)

    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_cells[row][col].config(text="", bg="#F0F0F0")
    
window= Tk()
window.title('RazDev XO Game')
symbols= ["X","O"]
player= random.choice(symbols)

game_cells = [
     [0,0,0],
     [0,0,0],
     [0,0,0],
     ]

label = Label(text=(player + " turn"), font=('consolas',40))
label.pack(side = "top")

restart_button= Button(text= "Restart", font=('consolas',30), command=start_newGame)
restart_button.pack()
cells_frame= Frame(window)
cells_frame.pack()

for row in range(3):
    for col in range(3):
        game_cells[row][col]=Button(cells_frame, text="", font=('consolas',40), width=4,height=1, command=lambda row=row, col=col: next_turn(row, col))
        game_cells[row][col].grid(row=row, column=col)

window.mainloop()
