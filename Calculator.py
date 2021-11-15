from tkinter import *
from tkinter.messagebox import *
from typing import Type
from math import *

def allClear(event):
    textArea.delete(0, END)

def backSpace(event):
    exp = textArea.get()
    exp = exp[0:len(exp)-1]
    textArea.delete(0, END)
    textArea.insert(0, exp)

def clickButtonAction(event):
    b=event.widget
    text=b['text']

    if text=="×":
        textArea.insert(END,"*")
        return

    elif text=="÷":
        textArea.insert(END,"/")
        return
    
    elif text=="√x":
        val = float(textArea.get())
        textArea.delete(0, END)
        textArea.insert(END, pow(val,1/2))
        return

    elif text=="x²":
        val = float(textArea.get())
        textArea.delete(0, END)
        textArea.insert(END, pow(val,2))
        return

    elif text=="x^y":
        textArea.insert(END,"**")
        return

    elif text=="x!":
        val = int(textArea.get())
        textArea.delete(0, END)
        textArea.insert(END, factorial(val))
        return

    elif text=='=':
        try:
            exp = textArea.get()
            answer = eval(exp)
            textArea.delete(0, END)
            textArea.insert(0, answer)
        except ZeroDivisionError:
            showerror("Error","You cannot divide a number by zero.")
        except NameError:
            showerror("Error","Invalid input in the expression.")
        except TypeError:
            showerror("Error","You are expected to enter mathematical expressions only.")
        return

    textArea.insert(END,text)

standardCalc = True

def scientificMode():
 
    global standardCalc

    if standardCalc:

        buttonFrame.pack_forget()
        extraFrame.pack(side=TOP,pady=10)
        buttonFrame.pack(side=TOP)
        calWindow.geometry('300x390')
        standardCalc = False
    else:
        extraFrame.pack_forget()
        calWindow.geometry('300x300')
        standardCalc = True   
       

if __name__ == '__main__':
    calWindow = Tk()
    calWindow.title("Calculator")
    calWindow.geometry('300x300')

    textArea = Entry(calWindow, justify=RIGHT, font="segoe 20")
    textArea.pack(side=TOP, fill=BOTH, pady=15, padx=10)

    #general part of the calculator
    buttonFrame = Frame(calWindow)
    buttonFrame.pack(side=TOP, padx=5, pady=10)

    num=1
    for i in range(3):
        for j in range(3):
            btn = Button(buttonFrame, text=num, font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
            btn.grid(row=i, column=j, padx=1, pady=1)
            num = num+1
            btn.bind('<Button-1>', clickButtonAction)

    btndot = Button(buttonFrame, text=".", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    btndot.grid(row=3, column=0, padx=1, pady=1)
    btndot.bind('<Button-1>', clickButtonAction)

    btnzero = Button(buttonFrame, text="0", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    btnzero.grid(row=3, column=1, padx=1, pady=1)
    btnzero.bind('<Button-1>', clickButtonAction)

    equalbtn = Button(buttonFrame, text="=", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    equalbtn.grid(row=3, column=2, padx=1, pady=1)
    equalbtn.bind('<Button-1>', clickButtonAction)

    addbtn = Button(buttonFrame, text="+", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    addbtn.grid(row=0, column=3, padx=1, pady=1)
    addbtn.bind('<Button-1>', clickButtonAction)

    subbtn = Button(buttonFrame, text="-", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    subbtn.grid(row=1, column=3, padx=1, pady=1)
    subbtn.bind('<Button-1>', clickButtonAction)

    mulbtn = Button(buttonFrame, text="×", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    mulbtn.grid(row=2, column=3, padx=1, pady=1)
    mulbtn.bind('<Button-1>', clickButtonAction)

    divbtn = Button(buttonFrame, text="÷", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    divbtn.grid(row=3, column=3, padx=1, pady=1)
    divbtn.bind('<Button-1>', clickButtonAction)

    backspacebtn = Button(buttonFrame, text='DEL', font="segoe 12", width=14, relief=GROOVE, activebackground='grey', activeforeground='white')
    backspacebtn.grid(row=4, column=0, padx=1, pady=1, columnspan=2)
    backspacebtn.bind('<Button-1>', backSpace)

    clearbtn = Button(buttonFrame, text="AC", font="segoe 12", width=14, relief=GROOVE, activebackground='grey', activeforeground='white')
    clearbtn.grid(row=4, column=2, padx=1, pady=1, columnspan=2)
    clearbtn.bind('<Button-1>', allClear)

    #additional section of the calculator
    extraFrame = Frame(calWindow)

    sqrtbtn = Button(extraFrame, text="√x", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    sqrtbtn.grid(row=0, column=0, padx=1, pady=1)
    sqrtbtn.bind('<Button-1>', clickButtonAction)

    squarebtn = Button(extraFrame, text="x²", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    squarebtn.grid(row=0, column=1, padx=1, pady=1)
    squarebtn.bind('<Button-1>', clickButtonAction)

    powerbtn = Button(extraFrame, text="x^y", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    powerbtn.grid(row=0, column=2, padx=1, pady=1)
    powerbtn.bind('<Button-1>', clickButtonAction)

    factorialbtn = Button(extraFrame, text="x!", font="segoe 15", width=5, relief=GROOVE, activebackground='grey', activeforeground='white')
    factorialbtn.grid(row=0, column=3, padx=1, pady=1)
    factorialbtn.bind('<Button-1>', clickButtonAction)

    calmenu = Menu(calWindow)
    more = Menu(calmenu, tearoff=0, font="segoe 10")
    more.add_checkbutton(label="Expand", command=scientificMode)
    calmenu.add_cascade(label="More", menu=more)
    calWindow.config(menu=calmenu)


    calWindow.mainloop()
