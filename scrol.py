import tkinter as tk
from tkinter import ttk

def add_row():
    global row_counter
    text = tk.Text(scrollable_frame, width=30, height=1)
    text.grid(row=row_counter, column=0, padx=10, pady=5)
    button = ttk.Button(scrollable_frame, text="Delete", command=lambda: delete_row(text, button))
    button.grid(row=row_counter, column=1, padx=10, pady=5)
    row_counter += 1
    update_scrollregion()

def delete_row(text, button):
    text.grid_forget()
    button.grid_forget()
    update_scrollregion()

def update_scrollregion():
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Section")

# Create a frame to hold the scrollable section
frame = ttk.Frame(root)
frame.pack(pady=10)

# Create a canvas widget
canvas = tk.Canvas(frame, width=300, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the canvas
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the rows
scrollable_frame = ttk.Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

row_counter = 0

# Create a button to add a new row
add_row_button = ttk.Button(root, text="Add Row", command=add_row)
add_row_button.pack()

root.mainloop()
