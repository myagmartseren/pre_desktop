from tkinter import Canvas, Entry, Button, PhotoImage, messagebox, Frame, StringVar,filedialog,Toplevel
from utils import relative_to_assets
from api.auth import register
from models import User
import tkinter as tk
from functools import partial
from models import * 
import api

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
        password_confirm = Entry(
            bd=0,
            bg="#FFFAFA",
            fg="#000716",
            highlightthickness=0
        )
        
        password_confirm.place(
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
        password = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        password.place(
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

        email = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        email.place(
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
        
        username = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        username.place(
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
        email = self.email_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()
        if register(user=User({"email": email, "password": password, "username":self.username_entry.get()})):
            HomeView(self.window)
        else:
            tk.messagebox.showerror("Error", "failed to register")
    def cancel_action(self):
        LoginView(self.window)

class LoginView(Frame):
    def __init__(self,main):
        self.window = main
        self.window.title("Нэвтрэх")
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
            command=self.open_register_view,
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
        RegisterView(self.window)

    def open_home_view(self):
        HomeView(self.window)

import uuid
from cryptography.fernet import Fernet

from umbral import (SecretKey, Signer,PublicKey, CapsuleFrag,Capsule,encrypt, decrypt_original,decrypt_reencrypted, generate_kfrags,reencrypt)

class HomeView(Frame):
    def __init__(self, root):
        super().__init__(root)
 
        self.window = root
        self.window.title('PRE Файл хуваалцах систем')
        self.file_names = list()
        self.file_buttons = list()
        #region GUI Home
        #region Frame
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#1A1D2B")

        canvas = Canvas(
            self.window,
            bg = "#1A1D2B",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1450.0,
            1024.0,
            fill="#ADD8E6",
            outline="")

        background_image = PhotoImage(
            file=relative_to_assets("home/background.png"))
        image_1 = canvas.create_image(
            880.0,
            603.0,
            image=background_image
        )
        #endregion Frame

        #region Files
        self.file_image = PhotoImage(file=relative_to_assets("home/file.png"))
        self.get_files()
        
        #endregion Files

        #region Left Bar
        #region shared files
        shared_image = PhotoImage(
            file=relative_to_assets("home/shared_files.png"))
        shared_button = Button(
            image=shared_image,
            borderwidth=0,
            highlightthickness=0,
            command=partial(self.get_files, True),
            relief="flat"
        )

        shared_button.place(
            x=50.0,
            y=397.0,
            width=239.0,
            height=46.0
        )
        #endregion My shared files

        #region shared with me files
        shared_with_me_image = PhotoImage(
            file=relative_to_assets("home/shared_with_me_files.png"))
        shared_with_me_button = Button(
            image=shared_with_me_image,
            borderwidth=0,
            highlightthickness=0,
            command=partial(self.get_files, False),
            relief="flat"
        )
        shared_with_me_button.place(
            x=50.0,
            y=331.0,
            width=239.0,
            height=43.0
        )
        #endregion shared with me files

        #region My files
        my_files_image = PhotoImage(
            file=relative_to_assets("home/my_files.png"))
        my_files_button = Button(
            image=my_files_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_files,
            relief="flat"
        )
        my_files_button.place(
            x=53.0,
            y=265.0,
            width=236.0,
            height=43.0
        )
        #endregion My files

        #region New File
        new_file_image = PhotoImage(
            file=relative_to_assets("home/new_file.png"))
        new_file_button = Button(
            image=new_file_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_file,
            relief="flat"
        )
        new_file_button.place(
            x=53.0,
            y=191.0,
            width=130.0,
            height=51.0
        )
        #endregion New File

        #region Logo
        logo_image = PhotoImage(
            file=relative_to_assets("home/logo.png"))
        logo_canvas = canvas.create_image(
            126.0,
            126.0,
            image=logo_image
        )
        #endregion Logo
        #endregion Left Bar

        #region Top bar
        #region Logout
        logout_image = PhotoImage(
            file=relative_to_assets("home/logout.png"))
        logout_button = Button(
            image=logout_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat"
        )
        logout_button.place(
            x=1333.0,
            y=90.0,
            width=62.0,
            height=43.0
        )
        #endregion Logout

        #region User
        self.username = StringVar()
        import main
        self.username.set(main.current_user.username)

        username_image = PhotoImage(
            file=relative_to_assets("home/username.png"))
        username_button = Button(
            image=username_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_15 clicked"),
            relief="flat",
            textvariable=self.username,
            compound="center",
            padx=200,
            pady=0,
        )
        username_button.config(fg="#003B73")

        username_button.place(
            x=1105.0,
            y=89.0,
            width=184.0,
            height=50.0
        )
        #endregion Logout

        #region Search background
        search_image = PhotoImage(
            file=relative_to_assets("home/search.png"))
        search_canva = canvas.create_image(
            691.0,
            115.0,
            image=search_image
        )
        #endregion Search background

        #region Search entry
        search_entry_image = PhotoImage(
            file=relative_to_assets("home/search_entry.png"))
        search_entry_bg = canvas.create_image(
            706.5,
            114.5,
            image=search_entry_image
        )
        self.search_entry = Entry(
            bd=0,
            bg="#E8EBEC",
            fg="#000716",
            highlightthickness=0
        )
        self.search_entry.place(
            x=400.0,
            y=93.0,
            width=613.0,
            height=41.0
        )
        #endregion Search background
        #endregion Top bar

        #region Pager

        #region Pager 1
        page1 = StringVar()
        page1.set("1")

        page_image_1 = PhotoImage(
            file=relative_to_assets("home/page_1.png"))
        page_button_1 = Button(
            image=page_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_18 clicked"),
            relief="flat",
            textvariable=page1,
            compound="center"
        )
        page_button_1.configure(fg="#003B73")

        page_button_1.place(
            x=835.0,
            y=977.0,
            width=17.0,
            height=19.0
        )

        canvas.create_text(
            840.0,
            979.0,
            anchor="nw",
            text="1",
            fill="#003B73",
            font=("Inter SemiBold", 13 * -1),
        )
        #endregion Pager 1

        #region Pager 2
        btn_text = StringVar()
        btn_text.set("2")

        page_image_2 = PhotoImage(
            file=relative_to_assets("home/page_2.png"))
        page_button_2 = Button(
            image=page_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_17 clicked"),
            relief="flat",
            textvariable=btn_text,
            compound="center"
        )
        page_button_2.place(
            x=857.0,
            y=977.0,
            width=17.0,
            height=19.0
        )
        page_button_2.configure(fg="#003B73")

        #endregion Pager 2

        #region Pager 3
        # button_image_16 = PhotoImage(
        #     file=relative_to_assets("home/button_16.png"))
        # button_16 = Button(
        #     image=button_image_16,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_16 clicked"),
        #     relief="flat"
        # )
        # button_16.place(
        #     x=879.0,
        #     y=977.0,
        #     width=17.0,
        #     height=19.0
        # )

        # canvas.create_text(
        #     884.0,
        #     979.0,
        #     anchor="nw",
        #     text="3",
        #     fill="#003B73",
        #     font=("Inter SemiBold", 13 * -1)
        # )
        #endregion Pager 3

        #endregion Pager

        #region empty
        # image_image_2 = PhotoImage(
        #     file=relative_to_assets("frame1/image_2.png"))
        # image_2 = canvas.create_image(
        #     817.0,
        #     402.0,
        #     image=image_image_2
        # )
        # canvas.create_text(
        #     481.0,
        #     467.0,
        #     anchor="nw",
        #     text="Аюулгүй фаил хуваалцах үйлчилгээ",
        #     fill="#003B73",
        #     font=("Inter Bold", 50 * -1)
        # )

        #endregion empty

        self.window.resizable(False, False)
        self.window.mainloop()
        #endregion GUI Home
    def get_files(self, shared_files = None):
        for button in self.file_buttons:
            button.destroy()
        files =  list()
        self.file_buttons =  list()

        temp_files = api.get_files(shared_files)
        if temp_files:
            for file in temp_files: 
                files.append(file)
        self.files = files
        
        x = 443.0
        y = 278.0
        for i in range(3):
            for j in range(3):
                if i*3+j< len(self.files):
                    self.file_names.append(StringVar())
                    print(self.files[i*3+j],len(self.files[i*3+j]),self.files[i*3+j].get("name"))
                    self.file_names[i*3+j].set(self.files[i*3+j].get("name"))
                    self.file_buttons.append(Button(
                        self.window,
                        image=self.file_image,
                        borderwidth=0,
                        highlightthickness=0,
                        # command=self.open_pop_view(self.files[i*3+j].get("id")),
                        command=partial(self.open_pop_view, self.files[i*3+j].get("id")),
                        relief="flat",
                        textvariable=self.file_names[i*3+j],
                        compound="center",
                        # text=self.files[i*3+j].get("id"),
                    ))
                    if self.file_buttons[i*3+j] is not None:
                        print("i*3+j",i*3+j)
                        self.file_buttons[i*3+j].place(
                            x=x+300*j,
                            y=y+227*i,
                            width=282.0,
                            height=195.0
                        )
                else:
                    break
        
        pass
    def open_pop_view(self,id):
        pop_window = Toplevel(self.window) 
        PopView(pop_window,id)
    def logout(self):
        if api.logout():
            # from .login import LoginView
            LoginView(self.window)
        else:
            messagebox.showinfo("Pop-up Message", "failed to logout")

    def open_file(self):
        # Open the file dialog.
        file_path = filedialog.askopenfilename(title="Select a file", initialdir="/home")

        filename = file_path.split("/")[-1]

        # Get the file contents.
        with open(file_path, "rb") as f:
            contents = f.read()
        
        generated_uuid = uuid.uuid4()
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_contents = f.encrypt(contents)

        import main
        capsule, encrypted_key = encrypt(PublicKey._from_exact_bytes(bytes.fromhex(main.current_user.public_key)), key) 
        
        # Save the encrypted file contents to a new file.
        # temp_path = relative_to_files(str(generated_uuid))
        temp_path = f"/tmp/{str(generated_uuid)}"
        with open(temp_path, "wb") as f:
            f.write(encrypted_contents)
        
        new_file = api.add_file(File({
            "ower_id": main.current_user.id,
            "name": filename,
            "key": encrypted_key,
            "capsule":capsule.__bytes__(),
            "path":temp_path,
            }))
        if new_file:
            messagebox.showinfo("Pop-up Message", "Successfully add file")
            self.get_files()
        else:
            messagebox.showinfo("Pop-up Message", "failed add file")

class PopView:
    def __init__(self, root,id):
        self.file = api.get_file(id)
        if self.file == None:
            messagebox.showerror("Error", "failed get file")
            return
        print(self.file,self.file.keys())
        self.window = root
        self.window.geometry("423x299")
        self.window.configure(bg = "#FFFFFF")
        self.window.title("File")
        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 299,
            width = 423,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(file=relative_to_assets("frame5/button_1.png"))
        decrypt_button = Button(
            self.window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.decrypt,
            relief="flat"
        )

        decrypt_button.place(
            x=33.0,
            y=238.0,
            width=363.0,
            height=37.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("frame5/button_2.png"))
        share_button = Button(
            self.window,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.share,
            relief="flat"
        )
        share_button.place(
            x=311.0,
            y=15.0,
            width=85.0,
            height=37.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("frame5/image_1.png"))
        
        image_1 = canvas.create_image(
            165.0,
            33.0,
            image=image_image_1
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("frame5/entry_1.png"))
        entry_bg_1 = canvas.create_image(
            164.5,
            34.0,
            image=entry_image_1
        )

        self.email_entry = Entry(
            self.window,
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            highlightthickness=0
        )
        self.email_entry.place(
            x=38.0,
            y=19.0,
            width=253.0,
            height=28.0
        )

        canvas.create_text(
            33.0,
            82.0,
            anchor="nw",
            text="test@gmail.com",
            fill="#003B73",
            font=("Inter", 12 * -1)
        )

        canvas.create_rectangle(
            31.0,
            102.0,
            390.0,
            103.0,
            fill="#003B73",
            outline="")
        
        canvas.pack()
        self.window.resizable(False, False)
        self.window.mainloop()
    def decrypt(self):
        import main
        from tkinter import filedialog
        directory = filedialog.askdirectory()
        cipher = api.download_file(self.file.get("path"))
        capsule_hex = self.file.get("capsule").replace('\\x', '').replace(' ', '')
        capsule_bytes = bytes.fromhex(capsule_hex)
        key_hex = self.file.get("key").replace('\\x', '').replace(' ', '')
        key_bytes = bytes.fromhex(key_hex)
        if self.file.get("owner_id") == main.current_user.id:    
            key = decrypt_original(SecretKey.from_bytes(main.private_key),Capsule.from_bytes(capsule_bytes), key_bytes)
        else:
            share = api.get_share(self.file.get("id"))
            if share is None:
                messagebox.showerror("Error Get Share","Share avahad aldaa garlaa")
                return
            
            cfrag = share.get("rekey").replace('\\x', '').replace(' ', '')
            cfrag_bytes = bytes.fromhex(cfrag)
            
            delegator_user = api.get_user(share.get("delegator_id"))
            if delegator_user is None:
                messagebox.showerror("Error Get delegator_user","delegator_user avahad aldaa garlaa")
                return
            Capsule.from_bytes(capsule_bytes)
            delegator_user.get("signer_key")

            suspicious_cfrag = CapsuleFrag.from_bytes(bytes(cfrag_bytes))
            delegating_pk = PublicKey.from_bytes(bytes.fromhex(delegator_user.get("public_key")))
            # verifying_pk=PublicKey.from_bytes(bytes.fromhex(delegator_user.get("signer_key")))

            cfrags = suspicious_cfrag.verify(Capsule.from_bytes(capsule_bytes),
                       verifying_pk=delegating_pk,
                       delegating_pk=delegating_pk,
                       receiving_pk=PublicKey.from_bytes(bytes.fromhex(main.current_user.public_key)),
                       )
            key = decrypt_reencrypted(receiving_sk=SecretKey.from_bytes(main.private_key),
                                    delegating_pk=delegating_pk,
                                    capsule=Capsule.from_bytes(capsule_bytes),
                                    verified_cfrags=[cfrags],
                                    ciphertext=key_bytes)
        plaincontent = Fernet(key).decrypt(cipher)
        with open(f"{directory}/{self.file.get('name')}","wb") as f:
            f.write(plaincontent)

    def share(self):
        import main
        email = self.email_entry.get()
        user = api.get_user(email)
        if user == None:
            messagebox.showerror("Error", "failed get user")
            return
        capsule_hex = self.file.get("capsule").replace('\\x', '').replace(' ', '')
        capsule_bytes = bytes.fromhex(capsule_hex)

        user_pk_hex =user.get("public_key").replace('\\x', '').replace(' ', '')
        user_pk_bytes = bytes.fromhex(user_pk_hex)

        kfrags = generate_kfrags(delegating_sk=SecretKey.from_bytes(main.private_key),
                         receiving_pk=PublicKey.from_bytes(user_pk_bytes),
                         signer=Signer(SecretKey.from_bytes(main.private_key)),
                         threshold=1,
                         shares=20)
        
        cfrag = reencrypt(capsule=Capsule.from_bytes(capsule_bytes), kfrag=kfrags[0])
        if api.add_share(Share({
        "file_id":self.file.get("id"),
        "delegator_id": main.current_user.id,
        'delegatee_id': user.get("id"),
        "rekey":cfrag.__bytes__()})):
            messagebox.showerror("Success", "success")
            
        else:
            messagebox.showerror("Error", "failed get user")
