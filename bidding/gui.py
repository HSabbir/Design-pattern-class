import tkinter as tk
from tkinter import ttk
from tkinter import *
from bidding import biddingraw

# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')



root = Tk()

# This is the section of code which creates the main window
root.geometry('880x570')
root.configure(background='#F0F8FF')
root.title('bidding')


# This is the section of code which creates the a label
Label(root, text='this is a label', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=300, y=77)


# This is the section of code which creates a button
Button(root, text='Bidder 1', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=179, y=289)


# This is the section of code which creates the a label
Label(root, text='bid value', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=188, y=239)


# This is the section of code which creates a button
Button(root, text='Bidder 2', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=362, y=297)


# This is the section of code which creates a button
Button(root, text='Bidder 3 ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=571, y=299)


# This is the section of code which creates the a label
Label(root, text='bid val 2', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=371, y=246)


# This is the section of code which creates the a label
Label(root, text='bid val 3', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=577, y=249)


root.mainloop()
