from tkinter import Canvas, Entry, Button, PhotoImage
from utils import relative_to_assets
from api.auth import register
from models import User
from .home import HomeView
import tkinter as tk

class RegisterView:
    def __init__(self, main):
        self.window = main
        self.window.title('Бүртгүүлэх')
        self.window.geometry("1354x676")
        self.window.configure(bg="#FFFFFF")
        # region GUI
        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=676,
            width=1354,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            574.35986328125,
            676.0,
            fill="#D4F1F4",
            outline="")

        register_image = PhotoImage(
            file=relative_to_assets("frame3/button_1.png"))

        register_button = Button(
            image=register_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.register_action(),
            relief="flat"
        )
        register_button.place(
            x=695.0,
            y=501.0,
            width=221.0,
            height=32.0
        )

        canvas.create_text(
            694.0,
            122.0,
            anchor="nw",
            text="Бүртгүүлэх",
            fill="#003B73",
            font=("Inter SemiBold", 19 * -1)
        )

        logo_bg_image = PhotoImage(
            file=relative_to_assets("frame3/image_1.png"))
        image_1 = canvas.create_image(
            1080.0,
            388.0,
            image=logo_bg_image
        )

        password_confirm_entry_image = PhotoImage(
            file=relative_to_assets("frame3/entry_1.png"))
        password_confirm_entry_bg_1 = canvas.create_image(
            1080.5,
            388.0,
            image=password_confirm_entry_image
        )

        self.password_confirm_entry = Entry(
            show="*",
            bd=0,
            bg="#FFFAFA",
            fg="#000716",
            highlightthickness=0
        )

        self.password_confirm_entry.place(
            x=973.0,
            y=375.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            970.0,
            354.0,
            anchor="nw",
            text="Нууц үгээ баталгаажуулах",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("frame3/image_2.png"))
        image_2 = canvas.create_image(
            803.0,
            388.0,
            image=image_image_2
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("frame3/entry_2.png"))
        entry_bg_2 = canvas.create_image(
            803.5,
            388.0,
            image=entry_image_2
        )
        self.password_entry = Entry(
            show="*",
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.password_entry.place(
            x=696.0,
            y=375.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            695.0,
            354.0,
            anchor="nw",
            text="Нууц үг",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("frame3/image_3.png"))
        image_3 = canvas.create_image(
            804.0,
            331.0,
            image=image_image_3
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("frame3/entry_3.png"))
        entry_bg_3 = canvas.create_image(
            804.5,
            331.0,
            image=entry_image_3
        )
        self.email_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email_entry.place(
            x=697.0,
            y=318.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            694.0,
            295.0,
            anchor="nw",
            text="Имэйл хаяг",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("frame3/image_4.png"))
        image_4 = canvas.create_image(
            804.0,
            271.0,
            image=image_image_4
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("frame3/entry_4.png"))
        entry_bg_4 = canvas.create_image(
            804.5,
            271.0,
            image=entry_image_4
        )
        self.username_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.username_entry.place(
            x=697.0,
            y=258.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            695.0,
            236.0,
            anchor="nw",
            text="Хэрэглэгчийн нэр",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("frame3/image_5.png"))
        image_5 = canvas.create_image(
            1080.0,
            211.0,
            image=image_image_5
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("frame3/entry_5.png"))
        entry_bg_5 = canvas.create_image(
            1081.0,
            210.5,
            image=entry_image_5
        )
        self.firstname_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.firstname_entry.place(
            x=974.0,
            y=197.0,
            width=214.0,
            height=25.0
        )

        canvas.create_text(
            970.0,
            178.0,
            anchor="nw",
            text="Нэр ",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("frame3/image_6.png"))
        image_6 = canvas.create_image(
            804.0,
            211.0,
            image=image_image_6
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("frame3/entry_6.png"))
        entry_bg_6 = canvas.create_image(
            804.5,
            211.0,
            image=entry_image_6
        )
        self.lastname_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.lastname_entry.place(
            x=697.0,
            y=198.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            694.0,
            180.0,
            anchor="nw",
            text="Овог",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("frame3/image_7.png"))
        image_7 = canvas.create_image(
            740.0,
            63.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("frame3/image_8.png"))
        image_8 = canvas.create_image(
            287.0,
            338.0,
            image=image_image_8
        )
        self.window.resizable(False, False)
        self.window.mainloop()
        # endregion GUI

    def register_action(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()
        if register(user=User({"firstname": self.firstname_entry.get(), "lastname": self.lastname_entry.get(), "email": email, "password": password, "username":self.username_entry.get()})):
            HomeView(self.window)
        else:
            tk.messagebox.showinfo("Pop-up Message", "failed to register")
