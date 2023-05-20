import tkinter as tk
from views.login import LoginView

current_user = None

# initialize login GUI
if __name__ == '__main__':
    main = tk.Tk()
    view = LoginView(main)
