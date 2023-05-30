import tkinter as tk
from views import LoginView
current_user = None
private_key = None
# API_URL = 'http://localhost:5000'

# initialize login GUI
if __name__ == '__main__':
    root = tk.Tk()
    LoginView(root)
    root.mainloop()
