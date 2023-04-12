from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root = Tk()
root.title("Alarm")
root.geometry("550x350")


mixer.init()


def th():
    t1 = threading.Thread(target=a, args=())
    t1.start()


def a():

    a = hr.get()
    a_hr = int(a[0:2])
    a_min = int(a[3:5])
    exp1 = 0<=a_hr<24
    exp2 = 0<=a_min<60
    if exp1 and exp2:
        Alarmtime = a
        CurrentTime = time.strftime("%H:%M")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")

        if Alarmtime == CurrentTime:
            mixer.music.load('cf.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('It is time', f'{amsg.get()}')
            if msg == 'ok':
                mixer.music.stop()
    else:
        msg = messagebox.showerror('Invalid data', 'Please enter valid time')


header = Frame(root,bg='red')
header.place(x=5, y=5)

head = Label(root, text="ALARM CLOCK", font=('comic sans', 20))
head.pack(fill=X)



panel = Frame(root)
panel.place(x=5, y=70)

alpp = PhotoImage(file='al.png')

alp = Label(panel, image=alpp)
alp.grid(rowspan=4, column=0)


atime = Label(panel, text="Alarm Time \n(Hr:Min)", font=('comic sans', 18))
atime.grid(row=0, column=1, padx=10, pady=5)

hr = Entry(panel, font=('comic sans', 20), width=5)
hr.grid(row=0, column=2, padx=10, pady=5)

amessage = Label(panel, text="Message", font=('comic sans', 20))
amessage.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

amsg = Entry(panel, font=('comic sans', 15), width=25)
amsg.grid(row=2, column=1, columnspan=2, padx=10, pady=5)


start = Button(panel, text="Start alarm", font=(
    'comic sans', 20), command=th, fg='white', bg='#1dc071')
start.grid(row=3, column=1, columnspan=2, padx=10, pady=5)


root.mainloop()
