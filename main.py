import tkinter

# ----- CONSTANTS ----- #
PINK = "#e2979c"
RED = "#C84B31"
GREEN = "#dce0cd"
YELLOW = "#ECDBBA"
FONT_NAME = "Lucida Console"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ----- UI SETUP ----- #
window = tkinter.Tk()
window.title("The Pomodoro App")
window.config(padx=50, pady=50, bg=RED)

# --- UI SETUP: Components --- #

title_label = tkinter.Label(text="POMODORO", font=(FONT_NAME, 30), bg=RED, fg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=RED, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="tomato_a.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35))

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0)
checkmark_label = tkinter.Label(text="⚙", font=(FONT_NAME, 30), bg=RED, fg=GREEN)
reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0)

tasks = ('Example A', 'Example B', 'Example C', 'Example D', 'Example E')
listbox_label = tkinter.Listbox(height=8, width=30, listvariable=tasks, bg=YELLOW, font=(FONT_NAME, 10))


window.config(padx=50, pady=50, bg=RED)


# --- UI SETUP: Grid Layout --- #
title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)

start_button.grid(column=0, row=2)
checkmark_label.grid(column=1, row=3)
reset_button.grid(column=2, row=2)

listbox_label.grid(column=1, row=5, pady=20)

# --- Window Loop --- #
window.mainloop()
