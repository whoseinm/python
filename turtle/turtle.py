
from tkinter import*

esas=Tk()

a=Entry(esas,width=100)
a.pack()
a.insert(0,"mekan?")


def basmaq():
    cumle=Label(esas,text="Sabunchu gencler evi"(),fg="red",bg="yellow")
    cumle.pack()
duyme=Button(esas,text="Click me!",command=basmaq,fg="yellow",bg="black",padx=100,pady=50)
duyme.pack()

esas.mainloop()