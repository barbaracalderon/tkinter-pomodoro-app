import tkinter
import math

# ----- CONSTANTS ----- #

PINK = "#e2979c"
RED = "#C84B31"
GREEN = "#dce0cd"
YELLOW = "#ECDBBA"
FONT_NAME = "Lucida Console"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# --- UI FUNCTIONS: Countdown Clock --- #

def start_timer():
    start_countdown(10)

def start_countdown(count):

    count_min = math.floor(count/60)
    count_sec = count%60
    canvas.itemconfig(time_display, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, start_countdown, count - 1)


# --- UI FUNCTIONS: Add/Remove tasks --- #

def add_button_click():
    listbox_label.insert(tkinter.END, entry_task.get())


def remove_button_click():
    listbox_label.delete(tkinter.ANCHOR)


# ----- UI SETUP ----- #
window = tkinter.Tk()
window.title("The Pomodoro App")
window.config(padx=20, pady=20, bg=RED)

# --- UI SETUP: Components --- #

title_label = tkinter.Label(text="POMODORO", font=(FONT_NAME, 30), bg=RED, fg=YELLOW)
title_task_label = tkinter.Label(text="& tasks", font=(FONT_NAME, 20), bg=RED, fg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=RED, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="tomato_a.png")
canvas.create_image(100, 112, image=tomato_img)
time_display = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35))

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, bg=GREEN,
                              command=start_timer)
checkmark_label = tkinter.Label(text="⚙", font=(FONT_NAME, 30), bg=RED, fg=GREEN)
reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, bg=GREEN)

task_phrase = tkinter.Label(text="Keep track of your tasks today.", font=(FONT_NAME, 11),
                            highlightthickness=0, bg=RED, fg=YELLOW)
entry_task = tkinter.Entry(width=53, bg=GREEN)
add_button = tkinter.Button(text="Add task", command=add_button_click, font=(FONT_NAME, 8), highlightthickness=0)
listbox_label = tkinter.Listbox(height=8, width=40, font=(FONT_NAME, 10), bg=GREEN)
remove_button = tkinter.Button(text="Remove task", command=remove_button_click, font=(FONT_NAME, 8),
                               highlightthickness=0)


# --- UI SETUP: Grid Layout --- #
title_label.grid(column=1, row=0)
title_task_label.grid(column=1, row=1)
canvas.grid(column=1, row=2)

start_button.grid(column=0, row=3)
checkmark_label.grid(column=1, row=4)
reset_button.grid(column=2, row=3)

task_phrase.grid(column=1, row=5, pady=10)
entry_task.grid(column=1, row=6)
add_button.grid(column=1, row=7, pady=5)
listbox_label.grid(column=1, row=8, pady=5)
remove_button.grid(column=1, row=9)

# --- Window Loop --- #
window.mainloop()
