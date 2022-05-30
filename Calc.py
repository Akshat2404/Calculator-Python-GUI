import time
from tkinter import *

screen_width=470
screen_height=432

root=Tk()
root.geometry(f'{screen_width}x{screen_height}')
root.minsize(screen_width, screen_height)
root.maxsize(screen_width, screen_height)
root.title('Calculator')
root.wm_iconbitmap('1.ico')

def clear_screen(event):
    equation.set('')
    # screen.update()

def backspace(event):
    equation.set(equation.get()[:-1])

def make_equation(event):
    global equation
    text = event.widget.cget('text')
    equation.set(equation.get() + text)
    print(equation.get())
    # screen.update()
    
def calculate(event):
    if equation.get().isdigit():
        value = int(equation.get())
    else:
        try:
            value = eval(equation.get())
            equation.set(value)
        except Exception as e:
            print(e)
            equation.set('Error 404')
            screen.update()
            time.sleep(1.25)
            equation.set('')
            screen.update()

# Use a new Label/Entry to print the answer

equation=StringVar()
equation.set('')
screen=Entry(root, textvariable=equation, font='lucida 32',)
screen.pack(fill=X, side=TOP, padx=10, pady=4)

color='#F5F5F5'
f0=Frame(root, bg=color, relief=SUNKEN)
f0.pack(fill=X)

f1=Frame(root, bg=color, relief=SUNKEN)
f1.pack(fill=X)

f2=Frame(root, bg=color, relief=SUNKEN)
f2.pack(fill=X)

f3=Frame(root, bg=color, relief=SUNKEN)
f3.pack(fill=X)

f4=Frame(root, bg=color, relief=SUNKEN)
f4.pack(fill=X)

def createButton(val, func_name, f):
    b=Button(f, text=val, font=('Helvetica', 28), width=5, height=1,) # bg='#F0FF8F'
    b.pack(side=LEFT)
    b.bind('<Button-1>', func_name)

createButton('(', make_equation, f0)
createButton(')', make_equation, f0)
createButton('<-', backspace, f0)
createButton('CLR', clear_screen, f0)

createButton('1', make_equation, f1)
createButton('2', make_equation, f1)
createButton('3', make_equation, f1)
createButton('+', make_equation, f1)

createButton('4', make_equation, f2)
createButton('5', make_equation, f2)
createButton('6', make_equation, f2)
createButton('-', make_equation, f2)

createButton('7', make_equation, f3)
createButton('8', make_equation, f3)
createButton('9', make_equation, f3)
createButton('*', make_equation, f3)

createButton('.', make_equation, f4)
createButton('0', make_equation, f4)
createButton('=', calculate, f4)
createButton('/', make_equation, f4)


root.mainloop()