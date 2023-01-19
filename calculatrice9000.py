from tkinter import *

# Global Layout

root = Tk()
root.geometry('400x480')
root.configure(bg='gray15')
root.title('Calculatrice9000')

expression = ''
equation = StringVar()
expression_field = Entry(root, textvariable=equation, bg='gray40', font=10)
expression_field.grid(columnspan=4, ipadx=17, ipady=12)

label_historic = []
historic = Listbox(root, listvariable=label_historic, bg='gray40', height=30, width=25)
historic.place(x=260, y=0)


# Operator label + bind for numpad

label_equal = Button(text='=', width=5, height=3, font=10, bg='dark orange', command=lambda: button_equal())
root.bind('<Return>', lambda event: button_equal())
label_plus = Button(text='+', width=5, height=3, font=10, bg='gray25', command=lambda: button_click('+'))
root.bind('+', lambda event: button_click('+'))
label_minus = Button(text='-', width=5, height=3, font=10, bg='gray25', command=lambda: button_click('-'))
root.bind('-', lambda event: button_click('-'))
label_divide = Button(text='/', width=5, height=3, font=10, bg='gray25', command=lambda: button_click('/'))
root.bind('/', lambda event: button_click('/'))
label_multiply = Button(text='x', width=5, height=3, font=10, bg='gray25', command=lambda: button_click('*'))
root.bind('*', lambda event: button_click('*'))
label_clear = Button(text='C', width=5, height=3, font=10, bg='gray25', command=lambda: button_clear())
label_dot = Button(text='.', width=5, height=3, font=10, bg='gray25', command=lambda: button_click('.'))
root.bind('.', lambda event: button_click('.'))
label_square = Button(text='²', width=5, height=3, font=10, bg='gray25', command=lambda: button_square())
label_percentage = Button(text='%', width=5, height=3, font=10, bg='gray25', command=lambda: button_click('//'))
label_squareroot = Button(text='√x', width=5, height=3, font=10, bg='gray25', command=lambda: button_squareroot())
label_clear_historic = Button(text='Clear Historic', width=12, height=3, font=2, bg='gray25', command=lambda: button_clear_historic())


# Number label and layout


def labelnum():
    i = 1
    for j in range(3, 6):
        for k in range(3):
            Button(command=lambda i=i: button_click(i), text=i, height=3, width=5, font=10).grid(row=[j], column=[k])
            root.bind(i, lambda event, i=i: button_click(i))
            i += 1

    Button(command=lambda: button_click(0), text='0', height=3, width=5, font=10).grid(row=6, column=1)

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
label_clear_historic.grid(row=6, column=4)


# Button function

def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)


# Button for the "sqrt" operator

def button_squareroot():
    global expression
    historic_memo = expression  # Keep the operation values
    expression = str(float(equation.get())**0.5)
    equation.set(expression)

    historic_result = historic_memo + "=" + expression
    historic.insert(0, historic_result)  # Display operation values + results


# Button for the ² operator

def button_square():
    global expression
    historic_memo = expression  # Keep the operation values
    expression = str(float(equation.get())**2)
    equation.set(expression)

    historic_result = historic_memo + "=" + expression
    historic.insert(0, historic_result)  # Display operation values + results


def button_clear():
    global expression
    expression = ''
    equation.set('')


def button_clear_historic():
    historic.delete(0, END)


def button_equal():
    try:
        global expression
        historic_memo = expression     # Keep the operation values
        total = str(eval(expression))
        equation.set(total)
        expression = total

        historic_result = historic_memo + "=" + expression
        historic.insert(0, historic_result)         # Display operation values + results

    except:
        equation.set('error')
        expression = ''


root.mainloop()