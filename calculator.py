from tkinter import*

esas=Tk()
esas.title("whoseinm")
a=Entry(esas,width=50,borderwidth=10)
a.grid(row=0,column=0,columnspan=3)

def basmaq(reqemler):
    kecid=a.get()
    a.delete(0,END)
    a.insert(0,str(kecid)+str(reqemler))

def silmek():
    a.delete(0,END)


duyme1=Button(esas,text="1",command=lambda:basmaq(1),padx=40,pady=30,fg="black")
duyme2=Button(esas,text="2",command=lambda:basmaq(2),padx=40,pady=30,fg="black")
duyme3=Button(esas,text="3",command=lambda:basmaq(3),padx=40,pady=30,fg="black")
duyme4=Button(esas,text="4",command=lambda:basmaq(4),padx=40,pady=30,fg="black")
duyme5=Button(esas,text="5",command=lambda:basmaq(5),padx=40,pady=30,fg="black")
duyme6=Button(esas,text="6",command=lambda:basmaq(6),padx=40,pady=30,fg="black")
duyme7=Button(esas,text="7",command=lambda:basmaq(7),padx=40,pady=30,fg="black")
duyme8=Button(esas,text="8",command=lambda:basmaq(8),padx=40,pady=30,fg="black")
duyme9=Button(esas,text="9",command=lambda:basmaq(9),padx=40,pady=30,fg="black")
duyme0=Button(esas,text="0",command=lambda:basmaq(0),padx=147,pady=30,fg="black")
duyme_silmek=Button(esas,text="C",command=lambda:silmek(),padx=40,pady=30,fg="black")
duyme_toplamaq=Button(esas,text="+",command=lambda:basmaq(),padx=40,pady=30,fg="black")
duyme_beraber=Button(esas,text="=",command=lambda:basmaq(),padx=40,pady=30,fg="black")

()
duyme1.grid(row=1,column=0)
duyme2.grid(row=1,column=1)
duyme3.grid(row=1,column=2)

duyme4.grid(row=2,column=0)
duyme5.grid(row=2,column=1)
duyme6.grid(row=2,column=2)

duyme7.grid(row=3,column=0)
duyme8.grid(row=3,column=1)
duyme9.grid(row=3,column=2)

duyme0.grid(row=4,column=0,columnspan=3)
duyme_silmek.grid(row=1,column=3)
duyme_toplamaq.grid(row=3,column=3)
duyme_beraber.grid(row=2,column=3)




esas.mainloop()