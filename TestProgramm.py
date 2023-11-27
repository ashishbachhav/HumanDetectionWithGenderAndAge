import PySimpleGUI as sg

from tkinter import *
import cv2 
from PIL import Image, ImageTk 
  
#sg.Window(title="Hello World", layout=[[]], margins=(150, 100)).read()
#print("Ashish")

def Addition(a,b):
    return a + b

a = 5
b = 3
c = Addition(a,b)

mymessage = "New Addition of a and b is :"
print('{} {}'.format(mymessage, c))

for j in range(5):
    for k in range(j):
        print("*")
    print("\n")
