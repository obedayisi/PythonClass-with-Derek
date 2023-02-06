from tkinter import *

main_window = Tk()

# Labels
Label(main_window, text = "What's your name?").grid(row = 0, column = 0)
Label(main_window, text = "How old are you?").grid(row = 1, column = 0)

# Text Input
name = Entry(main_window, width = 50, borderwidth = 5).grid(row = 0, column =1)
age = Entry(main_window, width = 50, borderwidth = 5).grid(row = 1, column =1)

def on_click():
	print(f"My name is {name.get()}, and my age is {age.get()}")

# Buttons

Button(main_window, text = "Click Here", command = on_click).grid(row = 2, column = 1)

main_window.mainloop()