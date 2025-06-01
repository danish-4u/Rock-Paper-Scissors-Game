from tkinter import *
import random

Comput_score = 0
play_score = 0

def outcome_handler(player_choice):
    global Comput_score
    global play_score
    outcomes = ["Rock", "Paper", "Scissors"]
    
    random_no = random.randint(0, 2)
    computer_choice = outcomes[random_no]
    
    Player_choice.config(text=f"Player Choosen: {player_choice.capitalize()}")
    Computer_choice.config(text=f"Computer Choosen: {computer_choice}")
    
    if player_choice == computer_choice.lower():
        outcome.config(text="It's a tie!")
    elif (player_choice == "rock" and computer_choice.lower() == "scissors") or \
         (player_choice == "scissors" and computer_choice.lower() == "paper") or \
         (player_choice == "paper" and computer_choice.lower() == "rock"):
        play_score += 1
        outcome.config(text="Player Wins!", font=("FZShuTi", 18))
    else:
        Comput_score += 1
        outcome.config(text="Computer Wins!",font=("FZShuTi", 18))
    
    Player_Score.config(text=f"Player Score: {play_score}")
    Computer_Score.config(text=f"Computer Score: {Comput_score}")

master = Tk()
master.title('RPS')

Label(master, text="Rock - Paper - Scissors", font=("FZShuTi", 18), fg="Red").grid(row=0, sticky=N, pady=20, padx=250) 
Label(master, text="Please Select an Option", font=("Arial", 12)).grid(row=1, sticky=N,pady=10)

Player_Score = Label(master, text="Player Score: 0", font=("Calibri", 12)) 
Player_Score.grid(row=2, sticky=W)

Computer_Score = Label(master, text="Computer Score: 0", font=("Calibri", 12))
Computer_Score.grid(row=2, sticky=E)

Player_choice = Label(master, font=("Calibri", 12)) 
Player_choice.grid(row=3, sticky=W,pady=20)

Computer_choice = Label(master, font=("Calibri", 12))
Computer_choice.grid(row=3, sticky=E,pady=20)

outcome = Label(master, font=("Calibri", 12))
outcome.grid(row=4, sticky=N,pady=10)

Button(master, text="Rock",font=("Calibri", 12), width=15, command=lambda: outcome_handler("rock")).grid(row=6, sticky=W, padx=5, pady=5)
Button(master, text="Paper",font=("Calibri", 12), width=15, command=lambda: outcome_handler("paper")).grid(row=6, sticky=N, pady=5)
Button(master, text="Scissors", font=("Calibri", 12),width=15, command=lambda: outcome_handler("scissors")).grid(row=6, sticky=E, padx=5, pady=5)

master.mainloop()
