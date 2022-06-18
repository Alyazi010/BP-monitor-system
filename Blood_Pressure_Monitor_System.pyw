from tkinter import *
import tkinter.messagebox as tmsg
from time import sleep, strftime
import datetime


root = Tk()
root.geometry("1000x600")
root.title("Blood Pressure Monitor")
root.resizable(0,0)
root.call('wm', 'iconphoto', root._w,PhotoImage(file='icon.png'))

def Quit():
    root.update()
    sleep(0.8)
    root.destroy()



def printInfo():
    global cInfo
    check.config(state=DISABLED)
    cInfo=Canvas(root, height=400, width=350)
    cInfo.configure(bg='black')
    #Uncomment below line to get a done button in the direction window
    #Button(cInfo, text="Done",activebackground='red', bg='black', font='lucida 15', fg='white', command=forget).place(x=270, y=350)
    cInfo.place(x=600, y=100)

    (b, a) = (int(lno.get()), int(uno.get()))

    messages=[('Normal', 'You have normal Blood Pressure !',
               '- Use more salt.\n\n- Lay down and raise your\n\n  feet to the level of your head.\n\n- Drink more water.\n\n- Wear compression stockings.'),
              ('Elevated', 'You have elevated Blood Pressure !',
               '- Less salt and saturated fats.\n\n- More activity.\n\n- A diet high in fruits and vegetables.'),
              ('High 1', 'You have high Blood Pressure.',
               '- Lay down and raise your feet to the level  of\n  your head.\n\n- Prescribe lifestyle changes and may consider\n  adding blood pressure medication based\n  on you.\n\n- “Have your drugs”.'),
              ('High 2', 'You have high Blood Pressure.',
               '- Lay down and raise your feet to the level of your\n  head.\n\n- Prescribe a combination  of  blood pressure\n  medications.'),
              ('High 3', 'You have high Blood Pressure.',
               '- Contact your doctor immediately.\n\n-	OR call 998 (Abu Dhabi).')]
    bpstage=0
    if (a < 120 and b < 80):
        bpstage=0
    elif ((a >= 120 and a < 130) and b < 80):
        bpstage=1
    elif ((a >= 130 and a < 140) or (b >= 80 and b < 90)):
        bpstage=2
    elif (a >= 140 and a < 180) or (b >= 90 and b < 120):
        bpstage=3
    elif a > 180 or b > 120:
        bpstage=4

    Label(cInfo, text=messages[bpstage][0], font="helvetica 20 bold", bg='black', fg='#B2BCFA', pady=3).place(x=8, y=25)
    Label(cInfo, text='Tips:', font ='helvetica 15', bg='black', fg='#B2BCFA', pady=3).place(x=8, y=75)
    Label(cInfo, text=messages[bpstage][2], font="helvetica 12 ", bg='black', fg='#FCE7E8', pady=3, justify=LEFT).place(x=8, y=120,)
    tmsg.showinfo(title=f"{messages[bpstage][0]} !", message=messages[bpstage][1])

def forget():
    sleep(0.2)
    cInfo.place_forget()
    cInfo.update()
    check.config(state=ACTIVE)
    done.config(state=DISABLED)
    lno.set('')
    uno.set('')

def calculate():
    global c2
    c2=Canvas(root, height=400, width=200)
    if lno.get()=='' or uno.get()=='':
        tmsg.showerror(title="Blank input !", message="Enter values first !")
        check.config(state=ACTIVE)
    elif not (lno.get().isdigit() and uno.get().isdigit()):
        tmsg.showerror(title="Invalid Input !", message="Inputs must be numbers.")
        check.config(state=ACTIVE)
    elif int(lno.get())>=int(uno.get()):
        tmsg.showerror(title="Error !", message="Lower number must be smaller than higher number.")
        check.config(state=ACTIVE)
    else:
        done.config(state=ACTIVE)
        printInfo()




C = Canvas(root, height=600, width=1000)
filename = PhotoImage(file = "background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(root, text="Blood Pressure Monitor", font="nunitosansms 27 bold",fg='#030A3C', bg="#F34E4E", justify=LEFT ).pack(anchor='nw',fill='x')

photo=PhotoImage(file='test2.png')
Button(root, text="x", font='lucida 30 bold',padx=10,image=photo, border=0, activebackground="#F34E4E",bg='darkred',command=Quit,width=50, height=50).place(x=1000,y=0, anchor='ne',relheight=0.08, relwidth=0.09)

Label(root, text="Enter Lower Number", font="helvetica 15 ", bg='darkred', fg='#B2BCFA', padx=10, pady=6, width=20).place(x=50, y=245)
Label(root, text="Enter Upper Number", font="helvetica 15 ", bg='darkred', fg='#B2BCFA', padx=10, pady=6, width=20).place(x=50, y=295)
lno=StringVar()
uno=StringVar()
Entry(root, textvariable=lno, bg="#05052F", font='helvetica 17',fg='pink', insertbackground='pink', border=6).place(x=320, y=245)
Entry(root, textvariable=uno, bg="#05052F", font='helvetica 17',fg='pink', insertbackground='pink', border=6).place(x=320, y=295)
check=Button(root, text="Check", border=2, activebackground='red', bg="#B2BCFA",font="helvetica 15 bold", command = calculate)
check.config(state=ACTIVE)
check.place(x=320, y=345)
done=Button(root, text='Done', border=2, activebackground='red', bg='#B2BCFA', font='helvetica 15 bold', command=forget,)
done.config(state=DISABLED)
done.place(x=470, y=345)


c=Canvas(root, width=270, height=400)
Label(c, text="Instructions", font="helvetica 23 bold", bg='black', fg='#B2BCFA',pady=3).place(x=45, y=25)
Label(c, text='Lower Number : ',font='helvetica 12', bg='black', fg='#B2BCFA', pady=6).place(x=16,y=90)
Label(c, text="Lower number is",font='helvetica 11', bg='black', fg='#FCE7E8',pady=6).place(x=135,y=92)
Label(c, text="DIASTOLIC mm hg. Enter the value",font='helvetica 11', bg='black', fg='#FCE7E8',pady=6).place(x=20,y=122)
Label(c, text="in the first box.",font='helvetica 11', bg='black', fg='#FCE7E8',pady=6).place(x=20,y=152)

Label(c, text='Upper Number : ',font='helvetica 12', bg='black', fg='#B2BCFA', pady=6).place(x=16,y=210)
Label(c, text="Upper number is",font='helvetica 11', bg='black', fg='#FCE7E8',pady=6).place(x=135,y=212)
Label(c, text="SYSTOLIC mm hg. Enter the value",font='helvetica 11', bg='black', fg='#FCE7E8',pady=6).place(x=20,y=242)
Label(c, text="in the second box.",font='helvetica 11', bg='black', fg='#FCE7E8',pady=6).place(x=20,y=272)

c.configure(bg='black',border=0)
c.place(x=680, y=100)



def time():
    now = datetime.datetime.now()
    string = now.strftime('%H:%M:%S %A, %B %dth, %Y')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 25, 'bold'),
            background='darkred',
            foreground='#B2BCFA',relief=SOLID,border=6,padx=10)

# Placing clock at the centre
# of the tkinter window
lbl.place(x=0, y=100)
time()

root.mainloop()