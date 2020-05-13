from tkinter import *
import math
import CalculatorBk as CalB

windows = Tk()
windows.minsize(10, 25)
windows.title("Standard Calculator")

operation = []
before = []
after = []
history = {}

def finalresult():
    before = operation.copy()
    result = CalB.calculate(operation)
    after = operation.copy()
    print(f"{before}={after}")
    history.update({str(before):str(after)})
    print(history)
    display.delete(0, END)
    display.insert(0, result)

def clearlistbox():
    display.delete(0, END)
    operation.clear()

def output(num):
    concat = ""
    if len(operation) == 0:
        operation.append(num)
    elif num.isdigit() and str(operation[-1]).isdigit():
        first = str(operation.pop(-1))
        last = num
        concat = concat + first + last
        operation.append(concat)
    elif num.isdigit() == 0 and str(operation[-1]).isdigit() == 0:
        operation.pop(-1)
        operation.append(num)
    else:
        operation.append(num)
    display.delete(0, END)
    display.insert(0, operation)

def keyoutput(num):
    num = num.char
    concat = ""
    if num == "=":
        finalresult()
    elif len(operation) == 0:
        operation.append(num)
    elif num.isdigit() and str(operation[-1]).isdigit():
        first = str(operation.pop(-1))
        last = num
        concat = concat + first + last
        operation.append(concat)
    elif num.isdigit() == 0 and str(operation[-1]).isdigit() == 0 and len(operation) != 1:
        operation.pop(-1)
        operation.append(num)
    else:
        if str(num) == "+" or str(num) == "-" or str(num) == "*" or str(num) == "/" or str(num).isdigit():
            operation.append(num)
    display.delete(0, END)
    display.insert(0, operation)

#Display Screen:
display = Listbox(windows, height = 10, width = 40)
display.grid(row = 0, column = 0, rowspan = 1, columnspan = 4)

#1 button:
value1 = StringVar()
one_button = Button(windows, text = "1", height = 2, width = 7, command = lambda:output("1"))
one_button.grid(row = 1, column = 0)

#2 button:
value2 = StringVar()
two_button = Button(windows, text = "2", height = 2, width = 7, command = lambda:output("2"))
two_button.grid(row = 1, column = 1)

#3 button:
value3 = StringVar()
three_button = Button(windows, text = "3", height = 2, width = 7, command = lambda:output("3"))
three_button.grid(row = 1, column = 2)

#4 button:
value4 = StringVar()
four_button = Button(windows, text = "4", height = 2, width = 7, command = lambda:output("4"))
four_button.grid(row = 2, column = 0)

#5 button:
value5 = StringVar()
five_button = Button(windows, text = "5", height = 2, width = 7, command = lambda:output("5"))
five_button.grid(row = 2, column = 1)

#6 button:
value6 = StringVar()
six_button = Button(windows, text = "6", height = 2, width = 7, command = lambda:output("6"))
six_button.grid(row = 2, column = 2)

#7 button:
value7 = StringVar()
seven_button = Button(windows, text = "7", height = 2, width = 7, command = lambda:output("7"))
seven_button.grid(row = 3, column = 0)

#8 button:
value8 = StringVar()
eight_button = Button(windows, text = "8", height = 2, width = 7, command = lambda:output("8"))
eight_button.grid(row = 3, column = 1)

#9 button:
value9 = StringVar()
nine_button = Button(windows, text = "9", height = 2, width = 7, command = lambda:output("9"))
nine_button.grid(row = 3, column = 2)

#0 button:
value0 = StringVar()
zero_button = Button(windows, text = "0", height = 2, width = 7, command = lambda:output("0"))
zero_button.grid(row = 4, column = 1)

#C button:
clear_button = Button(windows, text = "C", height = 2, width = 7, command = clearlistbox)
clear_button.grid(row = 4, column = 0)

#'=' button:
equal_button = Button(windows, text = "=", height = 2, width = 7, command = finalresult)
equal_button.grid(row = 4, column = 2)

#'+' button:
plus_button = Button(windows, text = "+", height = 2, width = 7, command = lambda:output("+"))
plus_button.grid(row = 1, column = 3)

#'-' button:
minus_button = Button(windows, text = "-", height = 2, width = 7, command = lambda:output("-"))
minus_button.grid(row = 2, column = 3)

#'*' button:
into_button = Button(windows, text = "*", height = 2, width = 7, command = lambda:output("*"))
into_button.grid(row = 3, column = 3)

#'/' button:
div_button = Button(windows, text = "/", height = 2, width = 7, command = lambda:output("/"))
div_button.grid(row = 4, column = 3)

#Keyboard Input:
windows.bind('<Key>', lambda num:keyoutput(num))

windows.mainloop()

print(operation)