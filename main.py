from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep+=1
    
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if rep%8==0:
        count_down(long_break_sec)
        title_label.config(title="Break",fg=RED)
    elif rep%2==0:
        count_down(short_break_sec)
        title_label.config(title="Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(title="Work",fg=GREEN)
    
def start_time():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    #itemconfig allows to change the canvas
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>=0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



title_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



#bottons
start_botton=Button(text="start",highlightthickness=0,command=start_timer)
start_botton.grid(column=0,row=2)

reset_botton=Button(text="reset",highlightthickness=0)
reset_botton.grid(column=2,row=2)

#check the labels, when you hit a botton 
check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

#to see the window, also loops throw the buttons
window.mainloop()