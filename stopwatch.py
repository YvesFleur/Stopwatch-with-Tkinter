from tkinter import *
import datetime
from time import time

root = Tk()

root.title("Stopwatch")
root.minsize(width=250, height=70)

s = 0   #second value
m = 0   #minute value
h = 0   #hour value
runnning = False

def counter():
    global h,m,s, begin, end
    
    if running:
        begin = time()  #time in second when pressing Start button
        s += 1
        if s == 60:
            s = s % 60
            m += 1
        if m == 60:
            m = m % 60
            h += 1
        disp = datetime.time(h, m, s)
        display.config(text=disp)
        end = time()    #time in second after executing values of s, m, h
        time_taken = end - begin    #duration for executing values of s, m, h
        
    #to make sure total is 1000ms
    display.after(round(1000-time_taken*1000), counter) 
    
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

start = Button(root, text='Start', command=start)
start.pack()

stop = Button(root, text='Stop', command=stop)
stop.pack()

root.mainloop()

