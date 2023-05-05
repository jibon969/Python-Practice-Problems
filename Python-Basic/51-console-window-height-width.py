
"""
Write a Python program to get the height and width of the console window.
"""
import tkinter as tk
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("screen_width  : ", screen_width)
print("screen_height : ", screen_height)


maxsize = root.maxsize()
minsize = root.minsize()

print("maxsize : ", maxsize)
print("minsize : ", minsize)


