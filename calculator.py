from tkinter import *
root = Tk()
root.title("Samuel's Calculator")


class buttons():
    def __init__(self, row, column, width, height, text, command = ''):
        
        self.root = root
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.text = text
        self.command = command
    
    def create(self):
        the_button = Button(self.root, text = self.text, width = self.width, height = self.height, command = self.command)
        the_button.grid(row = self.row, column = self.column)


i = 0
value_1 = 0
value_2 = 0
add_num = False
subtract_num = False
multiply_num = False
divide_num = False
def number_display(num):
    global i
    screen.insert(i,num)
    i += 1

def clear():
    global value_1
    global value_2
    global i
    screen.delete(0,END)
    value_1 = 0
    value_2 = 0
    i = 0

def add():
    global value_1
    global add_num
    global subtract_num
    global divide_num
    global multiply_num
    value_1 = float(screen.get())
    add_num = True
    subtract_num = False
    divide_num = False
    multiply_num = False
    screen.delete(0,END)

def subtract():
    global value_1
    global subtract_num
    global add_num
    global divide_num
    global multiply_num
    value_1 = float(screen.get())
    subtract_num = True
    add_num = False
    divide_num = False
    multiply_num = False
    screen.delete(0,END)

def multiply():
    global value_1
    global multiply_num
    global subtract_num
    global add_num
    global divide_num
    value_1 = float(screen.get())
    multiply_num = True
    add_num = False
    divide_num = False
    subtract_num = False
    screen.delete(0,END)

def divide():
    global value_1
    global divide_num
    global multiply_num
    global subtract_num
    global add_num
    value_1 = float(screen.get())
    divide_num = True
    add_num = False
    multiply_num = False
    subtract_num = False
    screen.delete(0,END)

def enter():
    global value_2
    value_2 = float(screen.get())
    screen.delete(0,END)

    if add_num:
        screen.insert(0,value_1 + value_2)
    if subtract_num:
        screen.insert(0,value_1 - value_2)
    if multiply_num:
        screen.insert(0,value_1 * value_2)
    if divide_num:
        screen.insert(0,value_1 / value_2)

screen = Entry(root, width = 50, borderwidth = 5)
button_1 = buttons(1,0,16,4,'1', command = lambda:number_display(1))
button_2 = buttons(1,1,16,4,'2', command = lambda:number_display(2))
button_3 = buttons(1,2,16,4,'3', command = lambda:number_display(3))
button_4 = buttons(2,0,16,4,'4', command = lambda:number_display(4))
button_5 = buttons(2,1,16,4,'5', command = lambda:number_display(5))
button_6 = buttons(2,2,16,4,'6', command = lambda:number_display(6))
button_7 = buttons(3,0,16,4,'7', command = lambda:number_display(7))
button_8 = buttons(3,1,16,4,'8', command = lambda:number_display(8))
button_9 = buttons(3,2,16,4,'9', command = lambda:number_display(9))
button_0 = buttons(4,0,16,4,'0', command = lambda:number_display(0))
button_decimal = buttons(4,1,16,4,'.', command = lambda:number_display('.'))
button_clear = buttons(4,2,16,4,'CLEAR', command = clear)
button_divide = buttons(1,4,16,4,'/', command = divide)
button_multiply = buttons(2,4,16,4,'*', command = multiply)
button_add = buttons(3,4,16,4,'+', command= add)
button_subtract = buttons(4,4,16,4,'-', command =subtract)
button_enter = buttons(5,4,16,4,'ENTER', command = enter)
    
def display():
    screen.grid(row = 5,column = 0, columnspan = 3, padx = 10, pady = 10)
    button_1.create()
    button_2.create()
    button_3.create()
    button_4.create()
    button_5.create()
    button_6.create()
    button_7.create()
    button_8.create()
    button_9.create()
    button_0.create()
    button_decimal.create()
    button_clear.create()
    button_divide.create()
    button_multiply.create()
    button_add.create()
    button_subtract.create()
    button_enter.create()
    

display()
root.mainloop()

