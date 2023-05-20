import tkinter as tk
from views.login import LoginView

current_user = None
API_URL = 'http://localhost:5000'

# initialize login GUI
if __name__ == '__main__':
    main = tk.Tk()
    view = LoginView(main)
