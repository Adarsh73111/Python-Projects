# from tkinter import *
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
#
# # ---------------------------- TIMER RESET ------------------------------- #
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #
#
# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#
# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)
#
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato = PhotoImage(file="tomato.png")
# canvas.create_image(102, 112, image=tomato)
# canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
#
#
# window.mainloop()

# Sound effect and Animation

from tkinter import *
import math
import winsound
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20

reps = 0
timer = None
particles = []


def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0
    # Ensure tomato is visible if reset during explosion
    canvas.itemconfig(tomato_item, state="normal")
    for p in particles:
        canvas.delete(p)
    particles.clear()


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def explode_tomato():
    # 1. Hide the tomato
    canvas.itemconfig(tomato_item, state="hidden")

    # 2. Play Sound
    winsound.PlaySound("SystemHand", winsound.SND_ASYNC)

    # 3. Create Explosion Particles
    colors = ["red", "orange", "yellow", "white"]
    for _ in range(30):
        x_speed = random.randint(-20, 20)
        y_speed = random.randint(-20, 20)
        size = random.randint(5, 15)
        color = random.choice(colors)
        particle = canvas.create_oval(100, 112, 100 + size, 112 + size, fill=color, outline="")
        particles.append({"id": particle, "x": x_speed, "y": y_speed})

    animate_explosion(0)


def animate_explosion(step):
    if step < 20:
        # Move particles outward
        for p in particles:
            canvas.move(p["id"], p["x"], p["y"])

        # Shake the window slightly
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        window.geometry(f"+{500 + offset_x}+{300 + offset_y}")

        window.after(30, animate_explosion, step + 1)
    else:
        # Cleanup explosion
        for p in particles:
            canvas.delete(p["id"])
        particles.clear()

        # Restore Tomato and Next Step
        canvas.itemconfig(tomato_item, state="normal")
        start_timer()

        # Add checkmarks
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        explode_tomato()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Center the window initially so shake looks normal
window.geometry("+500+300")

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Assigned to variable 'tomato_item' so we can manipulate it
tomato_item = canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()