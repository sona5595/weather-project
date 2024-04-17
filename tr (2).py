from tkinter import *
from tkinter import messagebox
import random
from tkinter import font

word_list = ["zealot", "yearn", "yawner", "xenophobia", "wonky", "vermillion", "uncanny", "tangible"]

def welcome():
    name = name_entry.get()                                                        # Welcome the user
    messagebox.showinfo("Hangman", f"Hello, {name}! Time to play Hangman!")
    window.destroy()

window = Tk()
window.title("Welcome to Hangman")                                                 # Create the welcome window
window.geometry('400x450')
window.config(bg="#63b9de")

name_label = Label(window, text="ENTER YOUR NAME ?" , bg=("#63b9de"),font=("bold", 15))
name_label.pack()                                                                   # Label and entry for user's name
name_entry = Entry(window ) 
name_entry.pack()

start_button = Button(window, text="Start Game", command=welcome)
start_button.pack()

window.mainloop()

word = random.choice(word_list)

guesses = ""
turns = 10

game_window = Tk()
game_window.title("Hangman Game")
game_window.geometry('400x450')
game_window.config(bg="#ea9d62")
word_label = Label(game_window, text="Word: " , bg="#ea9d62", font=("Arial", 12))
word_label.pack()
words = Label(game_window, text="wordlist = zealot, yearn, yawner, xenophobia, wonky, vermillion, uncanny, tangible",fg="black",bg="#ea9d62", font=("Arial", 12))
words.pack()
hangman_label = Label(game_window, text="",font=("Arial", 50),bg="#39dbd4")
hangman_label.pack(side=LEFT,)
turns_label = Label(game_window, text=f"Turns left: {turns}",font=("Arial", 15))
turns_label.pack()

def update_display():
    global turns
    word_display = ""
    for char in word:
        if char in guesses:
            word_display += char
        else:
            word_display += "_"
    
    word_label.config(text=f"Word: {word_display}",bg="#ea9d62")
    turns_label.config(text=f"Turns left: {turns}",bg="#ea9d62")
    
    if turns == 10:
        hangman = ""
    elif turns == 9:
        hangman = "  --------  "
    elif turns == 8:
        hangman = "  --------  \n     O      "
    elif turns == 7:
        hangman = "  --------  \n     O    \n        |   "
    elif turns == 6:
        hangman = "  --------  \n     O     \n      /| "
    elif turns == 5:
        hangman = "  --------  \n     O     \n      /|\   "
    elif turns == 4:
        hangman = "  --------  \n     O     \n      /|\     \n   /"
    elif turns == 3:
        hangman = "  --------  \n    O      \n      /|\     \n   / \ "
    elif turns == 2:
        hangman = "  --------  \n     O     \n      /|\     \n   / \     "
    
    else:
        hangman = "  --------  \n     O/   \n      /|\   \n     /|\   "
    
    hangman_label.config(text=hangman)

def guess_letter():
    global turns, guesses
    guess = guess_entry.get()
    if guess in guesses:
        messagebox.showinfo("Hangman", "You've already guessed that letter.")
    elif guess in word:
        guesses += guess
        if all(char in guesses for char in word):
            messagebox.showinfo("Hangman", "Congratulations! You won!")
            game_window.destroy()
        update_display()
    else:
        turns -= 1
        if turns == 0:
            messagebox.showinfo("Hangman", f"You lose! The word was '{word}'.")
            game_window.destroy()
        else:
            messagebox.showinfo("Hangman", f"Incorrect guess. {turns} attempts left.")
            update_display()
    guess_entry.delete(0, END)

guess_entry = Entry(game_window)
guess_entry.pack()

guess_button = Button(game_window, text="Guess", command=guess_letter)
guess_button.pack()

update_display()

game_window.mainloop()
