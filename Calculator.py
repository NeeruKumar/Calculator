import tkinter
from tkinter import *
from tkinter import messagebox

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

# function for numerical button clicked
def click(event):
    global data
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if data.get().isdigit():
            value=int(data.get())
        else:
            try:
                value=eval(data.get())
                value=round(value, 6)
            except Exception as e:
                value="Error"

        data.set(value)
        lbl.update()
    elif text=="C":
        data.set("")
    else:
        data.set(data.get()+text)
        lbl.update()










# the label that shows the result
data = StringVar()
data.set('')
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


# The buttons section
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn1.pack(side = LEFT, expand = True, fill = "both",)
btn1.bind("<Button-1>",click)
btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn2.pack(side = LEFT, expand = True, fill = "both",)
btn2.bind("<Button-1>",click)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn3.pack(side = LEFT, expand = True, fill = "both",)
btn3.bind("<Button-1>",click)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btnplus.pack(side = LEFT, expand = True, fill = "both",)
btnplus.bind("<Button-1>",click)
# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn4.pack(side = LEFT, expand = True, fill = "both",)
btn4.bind("<Button-1>",click)
btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn5.bind("<Button-1>",click)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn6.pack(side = LEFT, expand = True, fill = "both",)
btn6.bind("<Button-1>",click)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btnminus.pack(side = LEFT, expand = True, fill = "both",)
btnminus.bind("<Button-1>",click)
# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn7.pack(side = LEFT, expand = True, fill = "both",)
btn7.bind("<Button-1>",click)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn8.pack(side = LEFT, expand = True, fill = "both",)
btn8.bind("<Button-1>",click)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn9.pack(side = LEFT, expand = True, fill = "both",)
btn9.bind("<Button-1>",click)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btnmult.pack(side = LEFT, expand = True, fill = "both",)
btnmult.bind("<Button-1>",click)

# button for frame4


btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btnc.pack(side = LEFT, expand = True, fill = "both",)
btnc.bind("<Button-1>",click)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btn0.pack(side = LEFT, expand = True, fill = "both",)
btn0.bind("<Button-1>",click)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,

)
btnequal.pack(side = LEFT, expand = True, fill = "both",)
btnequal.bind("<Button-1>",click)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)
btndiv.bind("<Button-1>",click)

root.mainloop()
