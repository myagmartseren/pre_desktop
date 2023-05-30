
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox, Frame
from utils import relative_to_assets
import api

class LoginView(Frame):
    def __init__(self,main):
        self.window = main
        self.window.title("Нэвтрэх")
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#ADD8E6")
        icon = PhotoImage(file="../assets/images/logo.png")
        self.window.iconphoto(True, icon)

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

        logo_bg_img = PhotoImage(file=relative_to_assets("login/logo_bg.png"))
        canvas.create_image(720.0,512.0,image=logo_bg_img)

        frame_bg = PhotoImage(file=relative_to_assets("login/frame_bg.png"))
        canvas.create_image(660.0,491.0,image=frame_bg)

        #region Login Button
        login_btn_img = PhotoImage(file=relative_to_assets("login/btn_login.png"))
        login_btn_img_hvr = PhotoImage(file=relative_to_assets("login/btn_login_hvr.png"))
        
        def login_on_enter(event):
            login_btn.configure(image=login_btn_img_hvr)

        def login_on_leave(event):
            login_btn.configure(image=login_btn_img)

        login_btn = Button(
            image=login_btn_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        login_btn.place(
            x=458.0,
            y=537.0,
            width=404.0,
            height=53.0
        )

        login_btn.bind("<Enter>", login_on_enter)
        login_btn.bind("<Leave>", login_on_leave)
        #endregion Login Button

        register_img = PhotoImage(file=relative_to_assets("login/btn_register.png"))
        
        register_button = Button(
            image=register_img,
            borderwidth=0,
            highlightthickness=0,
            command= self.open_register_view,
            relief="flat"
        )

        register_button.place(
            x=458.0,
            y=606.0,
            width=404.0,
            height=53.0
        )

        image_bg = PhotoImage(file=relative_to_assets("login/image_bg.png"))
        canvas.create_image(
            660.0,
            464.0,
            image=image_bg
        )

        entry_img = PhotoImage(file=relative_to_assets("login/entry.png"))
        canvas.create_image(659.5,465.0,image=entry_img)
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

        canvas.create_image(
            660.0,
            347.0,
            image=image_bg
        )

        canvas.create_image(
            659.5,
            348.0,
            image=entry_img
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
        from .register import RegisterView 
        RegisterView(self.window)

    def open_home_view(self):
        from .home import HomeView
        HomeView(self.window)

