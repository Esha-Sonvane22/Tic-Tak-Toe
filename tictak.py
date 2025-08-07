from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Tic Tac Toe")
root.configure(bg="#cceeff")  # Background color for whole window

# Title frame and label
frame1 = Frame(root, bg="#cceeff")
frame1.pack(pady=10)

titlelable1 = Label(frame1, text="Tic Tac Toe", font=("Comic Sans MS", 24), fg="blue", width=20, bg="#cceeff")
titlelable1.grid(row=0, column=0)

# Status label (Turn indicator)
status_label = Label(frame1, text="Turn: X", font=("Comic Sans MS", 18), bg="#cceeff", fg="black")
status_label.grid(row=1, column=0)

# Frame for buttons
frame2 = Frame(root, bg="#cceeff")
frame2.pack(pady=20)

# Initial board setup
board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

turn = "X"
game_over = False

def checkforwin(player):
    if board[1] == board[2] == board[3] == player:
        return True
    elif board[4] == board[5] == board[6] == player:
        return True
    elif board[7] == board[8] == board[9] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[3] == board[6] == board[9] == player:
        return True
    elif board[1] == board[5] == board[9] == player:
        return True
    elif board[3] == board[5] == board[7] == player:
        return True
    return False

def checkfordraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def restartgame():
    global game_over, turn
    game_over = False
    turn = "X"
    for button in buttons:
        button["text"] = " "
    for i in board.keys():
        board[i] = " "
    titlelable1.config(text="Tic Tac Toe")
    status_label.config(text="Turn: X")

def play(event):
    global turn, game_over
    if game_over:
        return

    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == "X":
            button["text"] = "X"
            board[clicked] = turn
            if checkforwin(turn):
                titlelable1.config(text=f"{turn} wins!")
                status_label.config(text="Game Over")
                game_over = True
                return
            turn = "O"
            status_label.config(text="Turn: O")
        else:
            button["text"] = "O"
            board[clicked] = turn
            if checkforwin(turn):
                titlelable1.config(text=f"{turn} wins!")
                status_label.config(text="Game Over")
                game_over = True
                return
            turn = "X"
            status_label.config(text="Turn: X")

        if checkfordraw():
            titlelable1.config(text="It's a draw!")
            status_label.config(text="Game Over")
            game_over = True

# Create 9 buttons with styling
button_style = {"width": 4, "height": 2, "font": ("Comic Sans MS", 28),
                "bg": "#dbeafe", "relief": "groove", "borderwidth": 5, "fg": "#000080"}

button1 = Button(frame2, text=" ", **button_style)
button1.grid(row=0, column=0, padx=5, pady=5)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text=" ", **button_style)
button2.grid(row=0, column=1, padx=5, pady=5)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text=" ", **button_style)
button3.grid(row=0, column=2, padx=5, pady=5)
button3.bind("<Button-1>", play)

button4 = Button(frame2, text=" ", **button_style)
button4.grid(row=1, column=0, padx=5, pady=5)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text=" ", **button_style)
button5.grid(row=1, column=1, padx=5, pady=5)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text=" ", **button_style)
button6.grid(row=1, column=2, padx=5, pady=5)
button6.bind("<Button-1>", play)

button7 = Button(frame2, text=" ", **button_style)
button7.grid(row=2, column=0, padx=5, pady=5)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text=" ", **button_style)
button8.grid(row=2, column=1, padx=5, pady=5)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text=" ", **button_style)
button9.grid(row=2, column=2, padx=5, pady=5)
button9.bind("<Button-1>", play)

# Restart button
restartButton = Button(frame2, text="Restart Game", width=19, height=1,
                       font=("Comic Sans MS", 20), bg="#dbeafe", relief="groove", borderwidth=5, command=restartgame)
restartButton.grid(row=4, column=0, columnspan=3, pady=5)

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

root.mainloop()
