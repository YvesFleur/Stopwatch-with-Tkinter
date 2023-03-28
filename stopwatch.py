from tkinter import *
import datetime

root = Tk()

root.title("Stopwatch")
root.minsize(width=250, height=70)

s = 0
m = 0
h = 0
runnning = False

def counter():
    global h,m,s
    if running:
        s += 1
        if s == 60:
            s = s % 60
            m += 1
        if m == 60:
            m = m % 60
            h += 1
        disp = datetime.time(h, m, s)
        display.config(text=disp)
    display.after(1000, counter)

def start():
    global running
    running = True
    counter()

def stop():
    global running
    running = False
    counter()

display = Label(root)
display.pack(anchor='center')

strt = Button(root, text='Start', command=start)
strt.pack()

stop = Button(root, text='Stop', command=stop)
stop.pack()

root.mainloop()