from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnequalinput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    
win = Tk()
win.title("Calculator")
win.geometry("268x386")
operator = ""

#Display Screen
text_Input = StringVar()
txt = Entry(win, textvariable = text_Input,bg = "black", bd = 15, relief = "raised", justify = "right",font=("Arial",14), fg = "white",)
txt.grid(row = 0, column = 0, columnspan = 4, ipadx = 10, ipady = 15)

#Numbers
btn1 = Button(win, text = "7",command = lambda:btnClick(7), bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn1.grid(row = 1, column = 0)

btn2 = Button(win, text = "8", command = lambda:btnClick(8),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 10,padx = 10, pady = 10)
btn2.grid(row = 1, column = 1)

btn3 = Button(win, text = "9", command = lambda:btnClick(9),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn3.grid(row = 1, column = 2)

btn4 = Button(win, text = "+", command = lambda:btnClick("+"),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn4.grid(row = 1, column = 3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
btn5 = Button(win, text = "4",command = lambda:btnClick(4),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn5.grid(row = 2, column = 0)

btn6 = Button(win, text = "5", command = lambda:btnClick(5),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn6.grid(row = 2, column = 1)

btn7 = Button(win, text = "6", command = lambda:btnClick(6),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn7.grid(row = 2, column = 2)

btn8 = Button(win, text = "-", command = lambda:btnClick("-"),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn8.grid(row = 2, column = 3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
btn9 = Button(win, text = "1",command = lambda:btnClick(1),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn9.grid(row = 3, column = 0)

btn10 = Button(win, text = "2", command = lambda:btnClick(2),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn10.grid(row = 3, column = 1)

btn11 = Button(win, text = "3", command = lambda:btnClick(3),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn11.grid(row = 3, column = 2)

btn12 = Button(win, text = "*", command = lambda:btnClick("*"),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn12.grid(row = 3, column = 3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
btn13 = Button(win, text = "0",command = lambda:btnClick(0),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn13.grid(row = 4, column = 0)

btn14 = Button(win, text = "C", command = btnClearDisplay,  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn14.grid(row = 4, column = 1)

btn15 = Button(win, text = "=", command = btnequalinput,  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn15.grid(row = 4, column = 2)

btn16 = Button(win, text = "/", command = lambda:btnClick("/"),  bg = "white", font=("Arial",12), relief = "raised", borderwidth = 15,padx = 10, pady = 10)
btn16.grid(row = 4, column = 3)



