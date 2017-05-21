#Sample program to demonstrate tkinter library. This program will get the input from users in KG nd convert the values to 
#grams, pound and ounces using the below conversion rates.
#1 kg = 1000 grams
#1 kg = 2.20462 pounds
#1 kg = 35.274 ounces

from tkinter import *

window = Tk()

def convert():
	kg = e1_value.get()
	t1.delete(1.0, END)
	t2.delete(1.0, END)
	t3.delete(1.0, END)
	t1.insert(END, float(kg) * 1000)
	t2.insert(END, float(kg) * 2.20462)
	t3.insert(END, float(kg) * 35.274)


l1 = Label(window, text = 'Kg')
l1.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

b1 = Button(window, text = 'Convert', command = convert)
b1.grid(row = 0, column = 2)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 2)


window.mainloop()