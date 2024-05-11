from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
tick="✔"

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=img)
canvas.create_text(100,120,text="00:00",fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

timer_label=Label(text="Timer",font=(FONT_NAME,40,"bold",),fg='green',bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button=Button(text="Start",width=7,borderwidth=4)
start_button.grid(column=0,row=2)


reset_button=Button(text="Reset",width=7,borderwidth=4)
reset_button.grid(column=2,row=2)

tick_label=Label(text="✔",fg='GREEN',bg=YELLOW)
tick_label.grid(column=1,row=3)


window.mainloop()