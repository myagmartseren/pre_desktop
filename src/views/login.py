from pathlib import Path
from api.auth import login

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Entry, Text, Button, PhotoImage,Frame
from utils import relative_to_assets

class LoginView(Frame):
    def __init__(self,root,db):
        self.window=root
        self.db=db
        #region Init GUI
        self.window.title("Нэвтрэх")
        # self.pack()
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#ADD8E6")
        canvas = Canvas(
            self.window,
            bg = "#ADD8E6",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        canvas.place(x = 0, y = 0)
        background_logo = PhotoImage(
            file=relative_to_assets("frame0/image_1.png"))
        image_1 = canvas.create_image(
            720.0,
            512.0,
            image=background_logo
        )

        background_rectangle = PhotoImage(
            file=relative_to_assets("frame0/image_2.png"))
        image_2 = canvas.create_image(
            660.0,
            491.0,
            image=background_rectangle
        )

        login_image = PhotoImage(
            file=relative_to_assets("frame0/button_1.png"))
        login_button = Button(
            image=login_image,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("frame0/button_1 clicked"),
            command=self.login,
            relief="flat"
        )

        login_button.place(
            x=458.0,
            y=537.0,
            width=404.0,
            height=53.0
        )
        #region Password
        image_image_3 = PhotoImage(
            file=relative_to_assets("frame0/image_3.png"))
        image_3 = canvas.create_image(
            660.0,
            464.0,
            image=image_image_3
        )

        password_image = PhotoImage(
            file=relative_to_assets("frame0/entry_1.png"))
        password_bg = canvas.create_image(
            659.5,
            465.0,
            image=password_image
        )

        self.password_entry = Entry(
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            highlightthickness=0
        )
        self.password_entry.place(
            x=463.0,
            y=444.0,
            width=393.0,
            height=40.0
        )

        canvas.create_text(
            458.0,
            405.0,
            anchor="nw",
            text="Нууц үг\n",
            fill="#003B73",
            font=("Inter SemiBold", 16 * -1)
        )
        #endregion Password

        #region Email
        email_image = PhotoImage(
            file=relative_to_assets("frame0/image_4.png"))
        image_4 = canvas.create_image(
            660.0,
            347.0,
            image=email_image
        )

        email_image_2 = PhotoImage(
            file=relative_to_assets("frame0/entry_2.png"))
        email_bg_2 = canvas.create_image(
            659.5,
            348.0,
            image=email_image_2
        )

        self.email_entry = Entry(
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            highlightthickness=0
        )

        self.email_entry.place(
            x=463.0,
            y=327.0,
            width=393.0,
            height=40.0
        )
        canvas.create_text(
            458.0,
            288.0,
            anchor="nw",
            text="Имэйл хаяг ",
            fill="#003B73",
            font=("Inter SemiBold", 16 * -1)
        )
        #endregion Email

        canvas.create_text(
            458.0,
            230.0,
            anchor="nw",
            text="Нэвтрэх",
            fill="#003B73",
            font=("Inter SemiBold", 24 * -1)
        )
        self.window.resizable(False, False)
        self.window.mainloop()
        #endregion Init GUI
    
    def login(self):
        username = self.email_entry.get()
        password = self.password_entry.get()

        # Call the login_user function from the API module
        # Pass the username and password arguments
        # If login is successful, open the home screen
        if login(username, password):
            self.open_home_view()
        # else:
            # messagebox.showerror("Error", "Invalid username or password")
        # def open_home_view(self):
        #     # Hide the login screen and show the home screen
        #     self.master.withdraw()
        #     home_view = HomeView(self.master)
        #     home_view.pack()
