# -*- coding: utf-8 -*-
"""
Exercise 19 - Tkinter app that converts Fahrenheit to Celsius

"""

def exit():
    window.destroy()
 
def convert():
    c = int(e1.get())
    f = (c - 32) * (5/9)
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("350x100")
window.config(bg="green")
window.resizable(width=False,height=False)
window.title('Fahrenheit to Celcius')
 

l3= tk.Label(window,text=" ",bg='white')
 

 
e1= tk.Entry(window,font=('Arial',10))
 
btn1 = tk.Button(window,text=">",font=("Arial", 10),command=convert)

t1=tk.Text(window,state="disabled",width=15,height=0)


e1.pack()

btn1.pack()

t1.pack()

window.mainloop()
# Function to fahrenheit to celsius, result put in label

    
# main
# Set up 350x60 window with green background and title Fahrenheit to Celsius Converter, make it resizeable


# Create the Fahrenheit entry frame called frm_entry with a tkinter Entry widget and label in it


# Layout the temperature tkinter Entry and Label in frm_entry using the .grid() geometry manager


# Create the conversion Button that looks like an arrow and result display Label in window


# Set up the layout for frm_entry, button and label using the .grid() geometry manager


# Run the application through window loop