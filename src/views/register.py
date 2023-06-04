
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox, Frame
from utils import relative_to_assets
from models import *
import api
from .login import LoginView

class RegisterView(Frame):
    def __init__(self, main):
        self.window = main
        self.window.title('Бүртгүүлэх')
        self.window.geometry("1052x676")
        self.window.configure(bg = "#FFFFFF")

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 676,
            width = 1052,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            574.35986328125,
            676.0,
            fill="#D4F1F4",
            outline="")
        #region Register button
        register_btn_image = PhotoImage(
            file=relative_to_assets("register/register.png"))
        register_btn_img_hvr = PhotoImage(
            file=relative_to_assets("register/register_hvr.png"))
        
        register_btn = Button(
            image=register_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.register_action,
            relief="flat"
        )
        register_btn.place(
            x=687.0,
            y=510.0,
            width=221.0,
            height=32.0
        )

        def register_on_enter(event):
            register_btn.configure(image=register_btn_img_hvr)
        def register_on_leave(event):
            register_btn.configure(image=register_btn_image)     
        
        register_btn.bind("<Enter>",register_on_enter)
        register_btn.bind("<Leave>",register_on_leave)
        #endregion Register Button

        #region Cancel button
        cancel_btn_image = PhotoImage(
            file=relative_to_assets("register/cancel.png"))
        
        cancel_btn = Button(
            image=cancel_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.cancel_action,
            relief="flat"
        )

        cancel_btn.place(
            x=687.0,
            y=563.0,
            width=221.0,
            height=32.0
        )
        #endregion Cancel Button

        canvas.create_text(
            694.0,
            122.0,
            anchor="nw",
            text="Бүртгүүлэх",
            fill="#003B73",
            font=("Inter SemiBold", 19 * -1)
        )

        frame_img = PhotoImage(
            file=relative_to_assets("register/frame.png"))
        entry_bg = PhotoImage(
            file=relative_to_assets("register/entry_bg.png"))
             
        #region Password
        canvas.create_image(
            796.0,
            401.0,
            image=frame_img
        )
        canvas.create_image(
            796.5,
            401.0,
            image=entry_bg
        )
        self.password_confirm_entry = Entry(
            show='*',
            bd=0,
            bg="#FFFAFA",
            fg="#000716",
            highlightthickness=0
        )
        
        self.password_confirm_entry.place(
            x=689.0,
            y=388.0,
            width=215.0,
            height=24.0
        )
        #endregion Password
        
        canvas.create_text(
            686.0,
            367.0,
            anchor="nw",
            text="Нууц үгээ баталгаажуулах",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )
        canvas.create_image(
            795.0,
            330.0,
            image=frame_img
        )
        canvas.create_image(
            795.5,
            330.0,
            image=entry_bg
        )
        self.password_entry = Entry(
            show='*',
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.password_entry.place(
            x=688.0,
            y=317.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            687.0,
            296.0,
            anchor="nw",
            text="Нууц үг",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        canvas.create_image(
            796.0,
            273.0,
            image=frame_img
        )

        canvas.create_image(
            796.5,
            273.0,
            image=entry_bg
        )

        self.email_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.email_entry.place(
            x=689.0,
            y=260.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            686.0,
            237.0,
            anchor="nw",
            text="Имэйл хаяг",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        canvas.create_image(
            796.0,
            213.0,
            image=frame_img
        )

        canvas.create_image(
            796.5,
            213.0,
            image=entry_bg
        )
        
        self.username_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.username_entry.place(
            x=689.0,
            y=200.0,
            width=215.0,
            height=24.0
        )

        canvas.create_text(
            687.0,
            178.0,
            anchor="nw",
            text="Хэрэглэгчийн нэр",
            fill="#189AB4",
            font=("Inter SemiBold", 9 * -1)
        )

        logo_small = PhotoImage(file=relative_to_assets("register/logo_small.png"))
        canvas.create_image(
            740.0,
            63.0,
            image=logo_small
        )

        logo_big_img = PhotoImage(file=relative_to_assets("register/logo_big.png"))
        canvas.create_image(
            287.0,
            338.0,
            image=logo_big_img
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def register_action(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        password_confirm = self.password_confirm_entry.get().strip()
        
        if len(email)==0:
            messagebox.showerror("Алдаа","Имейл хаяг хоосон байна!")
            return           
        
        if password != password_confirm:
            messagebox.showerror("Алдаа","Нууц үг таарахгүй байна!")
            return
        
        check, error = api.register(user=User({"email": email, "password": password, "username":self.username_entry.get()}))
        if check:
            from .home import HomeView
            HomeView(self.window)
        else:
            messagebox.showerror("Error", error)
    def cancel_action(self):
        # pass
        LoginView(self.window)

