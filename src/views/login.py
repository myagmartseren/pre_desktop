from tkinter import Canvas, Entry, Button, PhotoImage, messagebox
from utils import relative_to_assets
import api
from .home import HomeView
from .register import RegisterView
from models import User

class LoginView:
    def __init__(self,main):
        self.window = main
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#ADD8E6")
        #region GUI
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
        logo_bg_img = PhotoImage(file=relative_to_assets("frame0/image_1.png"))
        logo_canva = canvas.create_image(720.0,512.0,image=logo_bg_img)

        bg_frame = PhotoImage(file=relative_to_assets("frame0/image_2.png"))
        bg_image = canvas.create_image(660.0,491.0,image=bg_frame)

        login_image = PhotoImage(file=relative_to_assets("frame0/button_1.png"))
        login_button = Button(
            image=login_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )

        login_button.place(
            x=458.0,
            y=537.0,
            width=404.0,
            height=53.0
        )

        register_img = PhotoImage(file=relative_to_assets("frame0/button_2.png"))
        register_button = Button(
            image=register_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_register_view,
            relief="flat"
        )

        register_button.place(
            x=458.0,
            y=606.0,
            width=404.0,
            height=53.0
        )

        image_image_3 = PhotoImage(file=relative_to_assets("frame0/image_3.png"))
        image_3 = canvas.create_image(
            660.0,
            464.0,
            image=image_image_3
        )

        password_img = PhotoImage(file=relative_to_assets("frame0/entry_1.png"))
        password_bg = canvas.create_image(659.5,465.0,image=password_img)
        self.password = Entry(
            show='*',
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            highlightthickness=0
        )
        self.password.place(
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

        image_image_4 = PhotoImage(file=relative_to_assets("frame0/image_4.png"))
        image_4 = canvas.create_image(
            660.0,
            347.0,
            image=image_image_4
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("frame0/entry_2.png"))
        entry_bg_2 = canvas.create_image(
            659.5,
            348.0,
            image=entry_image_2
        )
        self.email = Entry(
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            highlightthickness=0
        )
        self.email.place(
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

        canvas.create_text(
            458.0,
            230.0,
            anchor="nw",
            text="Нэвтрэх",
            fill="#003B73",
            font=("Inter SemiBold", 24 * -1)
        )
        #endregion GUI
        self.window.resizable(False, False)
        self.window.mainloop()
    
    def login(self):
        email = self.email.get()
        password = self.password.get()
        user = api.login(email, password)
        import main
        if user:
            main.current_user = user
            self.open_home_view()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_register_view(self):
        RegisterView(self.window)

    def open_home_view(self):
        HomeView(self.window)