
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox, Frame
from tkinter.filedialog import asksaveasfile

from utils import relative_to_assets
import api
from models import * 
from encryption import *  

class PopView(Frame):
    def __init__(self, root,id):
        self.file = api.get_file(id)
        if self.file == None:
            messagebox.showerror("Error", "failed get file")
            return
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
        cipher = api.download_file(self.file.path)
        capsule_bytes = bytes.fromhex(self.file.capsule)
        key_bytes = bytes.fromhex(self.file.key)
        
        if self.file.id == main.current_user.id:    
            key = decrypt_o(capsulse_bytes=capsule_bytes,key_bytes=key_bytes)
        
        else:
            share = api.get_share(self.file.get("id"))
            if share is None:
                messagebox.showerror("Алдаа","Хүсэлт явхад алдаа гарлаа")
                return
            
            delegator = api.get_user(share.get("delegator_id"))
            if delegator is None:
                messagebox.showerror("Алдаа","delegator_user avahad aldaa garlaa")
                return 
            key= decrypt_pre(share, delegator)

        file_path = asksaveasfile(mode='w',defaultextension="", initialfile=self.file.name)
        file_decrypt(key,cipher,file_path)

    def share(self):
        email = self.email_entry.get()
        user = api.get_user(email)
        if user == None:
            messagebox.showerror("Error", "failed get user")
            return
        key = generate_k(self.file, user)
        
        temp_share = Share({
            'file_id':self.file.get("id"),
            'delegatee_id': user.get("id"),
            'rekey': hex(key.__bytes__())}
        )
        
        if api.add_share(temp_share):
            messagebox.showinfo("Success", "success")
        else:
            messagebox.showerror("Error", "failed get user")
