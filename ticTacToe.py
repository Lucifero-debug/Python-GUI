from tkinter import *

root = Tk()
root.geometry("800x520")
root.title("Tic Tac Toe")
root.resizable(False, False)

def check_winner():
    global turns,game_over
    turns+=1

    # horizontal check 3 rows
    for row in range(3):
        if(board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]['text']!=""):
            label.config(text=board[row][0]["text"]+" is the winner!",foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_gray)
            game_over=True
            return
        
    for col in range(3):
        if(board[0][col]["text"]==board[1][col]["text"]==board[2][col]["text"] and board[0][col]['text']!=""):
            label.config(text=board[0][col]["text"]+" is the winner!",foreground=color_yellow)
            for row in range(3):
                board[row][col].config(foreground=color_yellow,background=color_gray)
            game_over=True
            return
    if (board[0][0].cget("text") == board[1][1].cget("text") == board[2][2].cget("text") and
            board[0][0].cget('text') != ""):
        label.config(text=board[0][0].cget("text") + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_gray)
        game_over = True
        return

    # Diagonal check (top-right to bottom-left)
    if (board[0][2].cget("text") == board[1][1].cget("text") == board[2][0].cget("text") and
            board[0][2].cget('text') != ""):
        label.config(text=board[0][2].cget("text") + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][2 - i].config(foreground=color_yellow, background=color_gray)
        game_over = True
        return

playerX = 'X'
playerO = 'O'
curr_player = playerX
turns=0
game_over=False

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = '#4584b6'
color_yellow = '#ffde57'
color_gray = '#343434'
color_light_gray = '#646464'


def set_title(row, col):
    global curr_player,game_over
    if game_over:
        return

    if board[row][col].cget('text') != "":  # Use cget to get the button's text
        return

    board[row][col].config(text=curr_player)  # Use config to set the button's text

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

    label.config(text=curr_player + "'s turn")  # Update the label text

    check_winner()



def new_game():
    global curr_player
    for row in range(3):
        for col in range(3):
            board[row][col].config(text="")
            curr_player=playerX
            label.config(text=curr_player + "'s turn")



frame = Frame(root)
label = Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_gray, foreground='white')
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for col in range(3):
        board[row][col] = Button(frame, text="", font=("Console", 50, "bold"), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=col: set_title(row, column))
        board[row][col].grid(row=row+1, column=col)

button = Button(frame, text="restart", font=("Consolas", 20), background=color_gray, foreground='white', command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky='we')

frame.pack()

root.mainloop()
