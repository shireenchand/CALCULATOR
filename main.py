from tkinter import *

root = Tk()
root.title("CALCULATOR")

#CREATING THE INPUT AND DISPLAY FIELD
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#FUNCTION FOR THE ON CLICK ACTION
def buttonClick(x):
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current)+str(x))

#FUNCTION TO CLEAR
def buttonClear():
    e.delete(0,END)


#FUNCTION TO ADD THE NUMBERS
def add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global op
    op = "+"
    e.delete(0,END)

#FUNCTION TO SUBTRACT THE NUMBERS
def sub():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global op
    op = "-"
    e.delete(0, END)

#FUNCTION TO MULTIPLY THE NUMBERS
def mul():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global op
    op = "x"
    e.delete(0, END)

#FUNCTION TO DIVIDE THE NUMBERS
def div():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global op
    op = "/"
    e.delete(0, END)

#FUNCTION TO GET THE RESULT
def equal():
    second_number = e.get()
    e.delete(0,END)
    s_num = int(second_number)
    if(op=='+'):
        e.insert(0, f_num+s_num)
    elif(op=='-'):
        e.insert(0, f_num-s_num)
    elif(op=='x'):
        e.insert(0,f_num*s_num)
    else:
        e.insert(0,f_num/s_num)

#CREATING THE BUTTONS
button1 = Button(root,text="1", padx=40,pady=20,command=lambda: buttonClick(1))
button2 = Button(root,text="2", padx=40,pady=20,command=lambda: buttonClick(2))
button3 = Button(root,text="3", padx=40,pady=20,command=lambda: buttonClick(3))
button4 = Button(root,text="4", padx=40,pady=20,command=lambda: buttonClick(4))
button5 = Button(root,text="5", padx=40,pady=20,command=lambda: buttonClick(5))
button6 = Button(root,text="6", padx=40,pady=20,command=lambda: buttonClick(6))
button7 = Button(root,text="7", padx=40,pady=20,command=lambda: buttonClick(7))
button8 = Button(root,text="8", padx=40,pady=20,command=lambda: buttonClick(8))
button9 = Button(root,text="9", padx=40,pady=20,command=lambda: buttonClick(9))
button0 = Button(root,text="0", padx=40,pady=20,command=lambda: buttonClick(0))
buttonadd = Button(root,text="+", padx=40,pady=20,command=add)
buttonsub = Button(root,text="-", padx=40,pady=20,command=sub)
buttonmul = Button(root,text="x", padx=40,pady=20,command=mul)
buttondiv = Button(root,text="/", padx=40,pady=20,command=div)
buttonequal = Button(root,text="=", padx=40,pady=20,command=equal)
buttonclear = Button(root, text="CLEAR",padx=40,pady=20,command=buttonClear )

#POSITIONING THE BUTTONS
button1.grid(row=3,column=0, sticky="nsew")
button2.grid(row=3,column=1, sticky="nsew")
button3.grid(row=3,column=2, sticky="nsew")
button4.grid(row=2,column=0, sticky="nsew")
button5.grid(row=2,column=1, sticky="nsew")
button6.grid(row=2,column=2, sticky="nsew")
button7.grid(row=1,column=0, sticky="nsew")
button8.grid(row=1,column=1, sticky="nsew")
button9.grid(row=1,column=2, sticky="nsew")
button0.grid(row=4,column=0, sticky="nsew")
buttonadd.grid(row=3,column=3, sticky="nsew")
buttonsub.grid(row=2,column=3, sticky="nsew")
buttonmul.grid(row=1,column=3, sticky="nsew")
buttondiv.grid(row=4,column=3, sticky="nsew")
buttonequal.grid(row=4,column=1, sticky="nsew")
buttonclear.grid(row=4, column=2, sticky="nsew")


#LOOP TO KEEP THE PROGRAM GOING ON
root.mainloop()
