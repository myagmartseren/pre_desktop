import tkinter as tk
from db import Database
# from encryption.symmetric import SymmetricEncryption
# from encryption.proxy_reencryption import ProxyReencryption
from views.login import LoginView

# initialize database, symmetric encryption, and proxy reencryption
db = Database("database.db")
current_user = None
# se = SymmetricEncryption()
# pre = ProxyReencryption()

# initialize login GUI
main = tk.Tk()
view = LoginView(main, db)
# view.window.mainloop()
