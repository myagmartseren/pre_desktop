from tkinter import Canvas, Entry, Button, PhotoImage, messagebox, Frame
from tkinter.filedialog import asksaveasfile
from utils import relative_to_assets
import api
from models import * 
from encryption import *  
from functools import partial

class PopView(Frame):
    def __init__(self, root, id):
        self.file= api.get_file(id)
        if self.file == None:
            messagebox.showerror("Error", "failed get file")
            return
        self.window = root
        print(self.file.owner_id, main.current_user.id
              )
        if self.file.owner_id == main.current_user.id:
            self.window.geometry("423x299")
            self.window.configure(bg = "#FFFFFF")
            self.window.title(self.file.name)
            self.user_buttons = list()
            self.scroll_items = list()

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

            decrypt_btn_img = PhotoImage(
                file=relative_to_assets("pop_up/button_1.png"))
            decrypt_btn_img_hvr = PhotoImage(
                file=relative_to_assets("pop_up/button_2.png"))

            decrypt_btn = Button(
                self.window,
                image=decrypt_btn_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.decrypt,
                relief="flat"
            )

            decrypt_btn.place(
                x=33.0,
                y=236.0,
                width=175.0,
                height=37.0
            )

            delete_btn_img = PhotoImage(
                file=relative_to_assets("pop_up/button_3.png"))
            delete_btn_img_hvr = PhotoImage(
                file=relative_to_assets("pop_up/button_4.png"))

            delete_btn = Button(
                self.window,
                image=delete_btn_img,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_3 clicked"),
                relief="flat"
            )

            delete_btn.place(
                x=224.0,
                y=237.0,
                width=175.0,
                height=37.0
            ) 

            share_btn_img = PhotoImage(
                file=relative_to_assets("pop_up/button_5.png"))
            share_btn_img_hvr = PhotoImage(
                file=relative_to_assets("pop_up/button_6.png"))
            share_btn = Button(
                self.window,
                image=share_btn_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.share,
                relief="flat"
            )

            share_btn.place(
                x=311.0,
                y=15.0,
                width=85.0,
                height=37.0
            )

            entry_frame = PhotoImage(
                file=relative_to_assets("pop_up/image_1.png"))

            canvas.create_image(
                165.0,
                33.0,
                image=entry_frame
            )

            entry_bg = PhotoImage(
                file=relative_to_assets("pop_up/entry_1.png"))
            canvas.create_image(
                164.5,
                34.0,
                image=entry_bg
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

            import tkinter as tk
            from tkinter import ttk

            self.frame = ttk.Frame(self.window)
            self.frame.pack(pady=10)

            self.frame.place(x=12, y=65)

            self.canvas_shared_users = tk.Canvas(
                self.frame,
                width=400,
                height=160,
                bg="#FFFFFF",
                bd=0,
                highlightthickness=0,
                relief="ridge"
            )

            self.canvas_shared_users.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas_shared_users.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.canvas_shared_users.configure(yscrollcommand=scrollbar.set)
            self.canvas_shared_users.bind('<Configure>', lambda e: self.canvas_shared_users.configure(scrollregion=self.canvas_shared_users.bbox("all")))

            scrollable_frame = ttk.Frame(self.canvas_shared_users)
            self.canvas_shared_users.create_window((0, 0), window=scrollable_frame, anchor="nw")

            self.remove_btn_img = tk.PhotoImage(file=relative_to_assets("pop_up/button_7.png"))
            self.remove_btn_img_hvr = tk.PhotoImage(file=relative_to_assets("pop_up/button_9.png"))
            self.shared_users()
        else:
            self.window.geometry("423x91")
            self.window.configure(bg = "#FFFFFF")

            canvas = Canvas(
                self.window,
                bg = "#FFFFFF",
                height = 91,
                width = 423,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            button_image_1 = PhotoImage(
                file=relative_to_assets("pop_up/big_decrypt.png"))
            button_1 = Button(
                self.window,
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.decrypt,
                relief="flat"
            )

            button_1.place(
                x=98.0,
                y=27.0,
                width=227.0,
                height=37.0
            )
            
            # button_image_2 = PhotoImage(
                # file=relative_to_assets("button_2.png")) 

        self.window.resizable(False, False)
        self.window.mainloop()

    def shared_users(self):
        import tkinter as tk
        for button in self.user_buttons:
            button.destroy()
        self.user_buttons = list()
        for item in self.scroll_items:
            self.canvas_shared_users.delete(item)
        self.scroll_items = list()
        emails = api.get_users_by_file(self.file.id)
        for i in range(len(emails)):
            y = 60 * i
            canvas_text = self.canvas_shared_users.create_text(
                30.0,
                20.0 + y,
                anchor="nw",
                text=emails[i],
                fill="#003B73",
                font=("Inter", 12)
            )
            self.scroll_items.append(canvas_text)
    
            canvas_rectangle = self.canvas_shared_users.create_rectangle(
                31.0,
                41.0 + y,
                361.0,
                43.0 + y,
                fill="#003B73",
                outline=""
            )
            self.scroll_items.append(canvas_rectangle)

            temp_button = tk.Button(
                self.frame,
                image=self.remove_btn_img,
                borderwidth=0,
                highlightthickness=0,
                command=partial(self.delete_share,emails[i]),
                relief="flat"
            )
            self.user_buttons.append(temp_button)

            temp_button_window = self.canvas_shared_users.create_window(
                370,
                20.0 + y,
                anchor="nw",
                window=temp_button,
                width=24,
                height=24
            )
            # self.canvas_shared_users.tag_bind(temp_button_window, "<Enter>", lambda event, rect=canvas_rectangle: self.canvas_shared_users.itemconfig(rect, fill="#000000"))
            # self.canvas_shared_users.tag_bind(temp_button_window, "<Leave>", lambda event, rect=canvas_rectangle: self.canvas_shared_users.itemconfig(rect, fill="#003B73"))
            
            self.scroll_items.append(temp_button_window)
        self.canvas_shared_users.configure(scrollregion=self.canvas_shared_users.bbox("all"))
    def delete_share(self, email):
        if api.delete_share(self.file.id,email):
            self.shared_users()
            messagebox.showinfo("Амжилттай","Ажилттай устгалаа")
        else:
            messagebox.showinfo("Алдаа","Алдаа гарлаа")
    
    def decrypt(self):        
        cipher = api.download_file(self.file.path)
        capsule_bytes = bytes.fromhex(self.file.capsule)
        key_bytes = bytes.fromhex(self.file.key)
        if self.file.owner_id == main.current_user.id:    
            key = decrypt_o(capsulse_bytes=capsule_bytes, key_bytes=key_bytes)
        else:
            share = api.get_share(self.file.id)
            if share is None:
                messagebox.showerror("Алдаа","Хүсэлт явхад алдаа гарлаа")
                return
            
            delegator = api.get_user(share.delegator_id)
            if delegator is None:
                messagebox.showerror("Алдаа","delegator_user avahad aldaa garlaa")
                return
            key= decrypt_pre(share, delegator,key_bytes,capsule_bytes)

        file_path = asksaveasfile(mode='w',defaultextension="", initialfile=self.file.name)
        file_decrypt(cipher, key, file_path)

    def share(self):
        email = self.email_entry.get()
        user = api.get_user(email)
        if user == None:
            messagebox.showerror("Error", "failed get user")
            return
        key = generate_k(user)
        temp_share = Share({
            'file_id':self.file.id,
            'delegatee_id': user.id,
            'rekey': key.hex()}
        ) 
        if api.add_share(temp_share):
            messagebox.showinfo("Success", "success")
            self.shared_users()
        else:
            messagebox.showerror("Error", "failed get user")
