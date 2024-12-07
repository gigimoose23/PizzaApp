import tkinter
import tkinter.ttk;
pizzaOptions = ["Cheese", "Pepperoni", "Veg", "Vegan", "Super Pizza (Veg, Vegan, Cheese AND Pepperoni)"]
def doIt(ev):
    print(pizzaB.get())
root = tkinter.Tk()
pizzaB = tkinter.ttk.Combobox(root,values=pizzaOptions,width=20,state="readonly")
pizzaB.bind(sequence="<<ComboboxSelected>>",func=doIt)
pizzaB.set("Choose Option")

pizzaB.place(x=0,y=0)
root.geometry("300x300")
root.title("Pizza App")
root.resizable(False,False)


root.mainloop()