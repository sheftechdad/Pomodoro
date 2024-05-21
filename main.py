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
reps=0
time_stop=None

# ---------------------------- TIMER RESET -------------------------------
def  timer_reset():
    window.after_cancel(time_stop)
    canvas.itemconfig(timer,text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec= WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text=" Break",fg=PINK,bg=YELLOW)

    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text=" Break", fg=RED , bg=YELLOW)

    else:
        count_down(work_sec)
        timer_label.config(text="WORK" , fg=GREEN , bg=YELLOW)








# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer,text=f'{count_min}:{count_sec}')
    if count>0:
        global time_stop
        time_stop=window.after(1000,count_down, count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
            tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
tick="✔"

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=img)
timer=canvas.create_text(100,120,text="00:00",fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)
#count_down(5)

timer_label=Label(text="Timer",font=(FONT_NAME,40,"bold",),fg='green',bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button=Button(text="Start",width=7,borderwidth=4,command=start_timer)
start_button.grid(column=0,row=2)


reset_button=Button(text="Reset",width=7,borderwidth=4,command=timer_reset)
reset_button.grid(column=2,row=2)

tick_label=Label(fg='GREEN',bg=YELLOW)
tick_label.grid(column=1,row=3)


window.mainloop()