import tkinter as tk
import subprocess
import matplotlib.pyplot as plt

HEIGHT = 200
WIDTH = 300

def open_calculator():
    subprocess.Popen(["python", "SimpleCalculator.py"])

def open_charts():
    subprocess.Popen(["python", "Charts.py"])

root = tk.Tk()
root.title("Calculator")
root.geometry(f"{WIDTH}x{HEIGHT}")

tk.Label(root, text="Choose your Calculator", font=30, fg="black").grid(row=0, column=0, pady=10, columnspan=2)

tk.Button(root, text="Simple Calculator", font=40, width=30, fg="red", command=open_calculator).grid(row=1, column=0, pady=10, padx=20, sticky='ew')
tk.Button(root, text="Charts", font=40, width=30, fg="red", command=open_charts).grid(row=2, column=0, pady=10, padx=20, sticky='ew')

root.grid_columnconfigure(0, weight=1)

root.mainloop()
