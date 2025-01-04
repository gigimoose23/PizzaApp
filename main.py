import tkinter
import tkinter.ttk
from tkinter import *
OptionPiz = "Cheese"
OptionQuan = "1"
OptionSize = "Small"
pizzaOptions = ["Cheese", "Pepperoni", "Veg", "Vegan", "Super Pizza (Veg, Vegan, Cheese AND Pepperoni)"]
quantities = ["1", "2", "3", "4", "5"]
def doIt(ev):
    print(pizzaB.get())
    global OptionPiz
    OptionPiz = pizzaB.get()
def setQuan(ev):
    print(pizzaQ.get())
    global OptionQuan
    OptionQuan = pizzaQ.get()


root = tkinter.Tk()
favPizLab = tkinter.Label(root,text="Select Your Fav Pizza:",font=("Calibri",11))
OpSize = IntVar()
OpSize.set(1)
def setSize():
    global OptionSize
    varNew = OpSize.get()
    if varNew == 1:
        OptionSize = "Small"
    elif varNew == 2:
        OptionSize = "Medium"
    elif varNew == 3:
        OptionSize = "Large"
ChooseSmallOp = tkinter.Radiobutton(root, text="S",variable=OpSize, value=1,command=setSize)
FinishedOp = tkinter.Label(root,text="Waiting for order...",font=("Calibri",11))
ChooseMedOp = tkinter.Radiobutton(root, text="M",variable=OpSize, value=2,command=setSize)
ChooseLargOp = tkinter.Radiobutton(root, text="L",variable=OpSize, value=3,command=setSize)
topLab = tkinter.Label(root,text="WELCOME TO PIZZA HUT",font=("Calibri",17,"bold"))
quanPizLab = tkinter.Label(root,text="Enter Quantity:",font=("Calibri",11))
pizzaB = tkinter.ttk.Combobox(root,values=pizzaOptions,width=20,state="readonly")
pizzaQ = tkinter.ttk.Combobox(root,values=quantities,width=20,state="readonly")
pizzaQ.bind(sequence="<<ComboboxSelected>>",func=setQuan)
pizzaQ.set(OptionQuan)
def order():
    FinishedOp.config(text="You Ordered " + OptionQuan + " " + OptionPiz + " " + OptionSize + " Size Pizza(s)")
ordBtn = tkinter.Button(root,text="Place Order",command=order)
pizzaB.bind(sequence="<<ComboboxSelected>>",func=doIt)
pizzaB.set(OptionPiz)

favPizLab.place(x=50,y=128)

topLab.place(x=190,y=20)
quanPizLab.place(x=50,y=150)
root.geometry("600x300")
root.title("Pizza App")
root.resizable(False,False)
pizzaB.place(x=240,y=128)
pizzaQ.place(x=240,y=150)

ChooseSmallOp.place(x=420,y=120)
ChooseMedOp.place(x=420,y=140)
ChooseLargOp.place(x=420,y=160)
FinishedOp.place(x=310,y=275,anchor="center")
ordBtn.place(x=310,y=200,anchor="center")
root.mainloop()