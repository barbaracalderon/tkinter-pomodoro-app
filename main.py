import tkinter
import math

# ----- CONSTANTS ----- #

PINK = "#e2979c"
RED = "#C84B31"
GREEN = "#dce0cd"
GREEN_MSG = "#125C13"
YELLOW = "#ECDBBA"
FONT_NAME = "Lucida Console"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None

# --- UI FUNCTIONS: Countdown Clock --- #

def start_timer():
    global repetition
    global title_task_label
    repetition += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetition % 8 == 0:
        title_task_label.config(text="long break", font=(FONT_NAME, 30), bg=GREEN, fg=GREEN_MSG)
        start_countdown(long_break_sec)
    elif repetition % 2 == 0:
        start_countdown(short_break_sec)
        title_task_label.config(text="short break", font=(FONT_NAME, 20), bg=GREEN, fg=PINK)
    else:
        title_task_label.config(text="work and focus", font=(FONT_NAME, 20), bg=RED, fg=PINK)
        start_countdown(work_sec)


def start_countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(time_display, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, start_countdown, count - 1)
    else:
        start_timer()
        engines = ''
        work_sess = math.floor(repetition/2)
        for item in range(work_sess):
            engines += '⚙'
        checkmark_label.config(text=engines)

# --- UI FUNCTIONS: Timer Reset --- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_display, text='00:00')
    title_task_label.config(text="& tasks")
    checkmark_label.config(text='')
    global repetition
    repetition = 0


# --- UI FUNCTIONS: Add/Remove tasks --- #

def add_button_click():
    listbox_label.insert(tkinter.END, entry_task.get())


def remove_button_click():
    listbox_label.delete(tkinter.ANCHOR)


# --- UI FUNCTIONS: Set work and long break variables --- #

def set_work_timer():
    global WORK_MIN
    work_minutes = int(work_entry.get())
    if type(work_minutes) != int:
        WORK_MIN = 25
    else:
        WORK_MIN = work_minutes
    return WORK_MIN

def set_long_break():
    global LONG_BREAK_MIN
    long_break = int(long_break_entry.get())
    if type(long_break) != int:
        LONG_BREAK_MIN = 20
    else:
        LONG_BREAK_MIN = long_break
    return LONG_BREAK_MIN


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
reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, bg=GREEN,
                              command=reset_timer)

checkmark_label = tkinter.Label(font=(FONT_NAME, 30), bg=RED, fg=GREEN)

work_button = tkinter.Button(text="Work Min.", font=(FONT_NAME, 8), highlightthickness=0, bg=GREEN,
                             command=set_work_timer, width=10)
work_entry = tkinter.Entry(width=3, bg=GREEN)
long_break_button = tkinter.Button(text="Break Min.", font=(FONT_NAME, 8), highlightthickness=0, bg=GREEN,
                                   command=set_long_break, width=10)
long_break_entry = tkinter.Entry(width=3, bg=GREEN)

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
reset_button.grid(column=0, row=4)

checkmark_label.grid(column=1, row=4)

work_button.grid(column=2, row=3, padx=6)
work_entry.grid(column=4, row=3)
long_break_button.grid(column=2, row=4, padx=6)
long_break_entry.grid(column=4, row=4)

task_phrase.grid(column=1, row=5, pady=10)
entry_task.grid(column=1, row=6)
add_button.grid(column=1, row=7, pady=5)
listbox_label.grid(column=1, row=8, pady=5)
remove_button.grid(column=1, row=9)

# --- Window Loop --- #
window.mainloop()
