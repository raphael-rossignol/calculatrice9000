from tkinter import *

# Global Layout

root = Tk()
root.geometry("258x480")
root.configure(bg='gray15')
root.title("Calculatrice9000")
expression = ""
equation = StringVar()
expression_field = Entry(root, textvariable=equation, bg='gray40', font=10)
expression_field.grid(columnspan=4, ipadx=17, ipady=12)


# Operator label

label_equal = Button(text='=', width=5, height=3, font=10, bg='dark orange', command=lambda: button_equal())
label_plus = Button(text='+', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("+"))
label_minus = Button(text='-', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("-"))
label_divide = Button(text='/', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("/"))
label_multiply = Button(text='x', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("*"))
label_clear = Button(text='C', width=5, height=3, font=10, bg='gray25', command=lambda: button_clear())
label_dot = Button(text='.', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("."))
label_square = Button(text='²', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("**"))
label_percentage = Button(text='%', width=5, height=3, font=10, bg='gray25', command=lambda: button_click("//"))
label_squareroot = Button(text='√x', width=5, height=3, font=10, bg='gray25', command=lambda: button_squareroot())


# Number label and layout

def labelnum():
    i = 1
    btns = []
    for j in range(3, 6):
        for k in range(3):
            btns.append(Button(command=lambda i=i: button_click(i), text=i, height=3, width=5, font=10).grid(row=[j], column=[k]))
            i += 1

    Button(command=lambda : button_click(0), text="0", height=3, width=5, font=10).grid(row=6, column=1)

labelnum()


# Operator layout

label_equal.grid(row=6, column=3)
label_plus.grid(row=3, column=3)
label_minus.grid(row=4, column=3)
label_divide.grid(row=5, column=3)
label_multiply.grid(row=2, column=3)
label_clear.grid(row=6, column=0)
label_dot.grid(row=6, column=2)
label_square.grid(row=2, column=1)
label_percentage.grid(row=2, column=2)
label_squareroot.grid(row=2, column=0)


# Button function

def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)


# Button for the ² operator

def button_squareroot():
    global expression
    expression = str(float(equation.get())**0.5)
    equation.set(expression)


def button_clear():
    global expression
    expression = ""
    equation.set("")


def button_equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set('error')
        expression = ""


root.mainloop()