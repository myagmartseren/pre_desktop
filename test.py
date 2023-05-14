import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

# Define the open_file() function.
def open_file():
    # Get the file name from the text entry box.
    filename = entry.get()

    # Open the file dialog.
    filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
    filename = filedialog.askopenfilename(title="Select a file", initialdir="/", filetypes=filetypes)

    # Display the file name in the label.
    label.config(text=filename)

# Create a label to display the file name.
label = tk.Label(root, text="File name:")

# Create a text entry box to enter the file name.
entry = tk.Entry(root)

# Create a button to open the file browser.
button = tk.Button(root, text="Open", command=open_file)

# Layout the widgets.
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0)

# Start the main loop.
root.mainloop()
