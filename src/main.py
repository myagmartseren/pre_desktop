import tkinter as tk
from views.login import LoginView

current_user = None

# initialize login GUI
main = tk.Tk()
view = LoginView(main)
