from utils import relative_to_assets
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox 
import api
from cryptography.fernet import Fernet
from umbral import (SecretKey, Signer,PublicKey, CapsuleFrag,Capsule, decrypt_original,decrypt_reencrypted, generate_kfrags,reencrypt)
from models import *
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
        if self.file.owner == main.current_user.id:    
            key = decrypt_original(SecretKey.from_bytes(main.private_key),Capsule.from_bytes(capsule_bytes), key_bytes)
        else:
            share = api.get_share(self.file.get("id"))

            cfrag = share.get("rekey").replace('\\x', '').replace(' ', '')
            cfrag_bytes = bytes.fromhex(cfrag)
            
            delegator_user = api.get_user(share.get("delegator_id"))


            suspicious_cfrag = CapsuleFrag.from_bytes(bytes(cfrag_bytes))
            cfrags = suspicious_cfrag.verify(Capsule.from_bytes(capsule_bytes),
                       verifying_pk=delegator_user.get("signer_key"),
                       delegating_pk=delegator_user.get("public_key"),
                       receiving_pk=main.current_user.public_key,
                       )
            key = decrypt_reencrypted(receiving_sk=main.private_key,
                                    delegating_pk=delegator_user.get("public_key"),
                                    capsule=capsule_bytes,
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
        print("after get user",user)
        capsule_hex = self.file.get("capsule").replace('\\x', '').replace(' ', '')
        capsule_bytes = bytes.fromhex(capsule_hex)

        print("user_pub key", user.get("public_key"))        
        user_pk_hex =user.get("public_key").replace('\\x', '').replace(' ', '')
        user_pk_bytes = bytes.fromhex(user_pk_hex)

        kfrags = generate_kfrags(delegating_sk=SecretKey.from_bytes(main.private_key),
                         receiving_pk=PublicKey.from_bytes(user_pk_bytes),
                         signer=Signer(SecretKey.from_bytes(main.private_key)),
                         threshold=1,
                         shares=20)
        cfrag = reencrypt(capsule=Capsule.from_bytes(capsule_bytes), kfrag=kfrags[0])
        print("delegator id ",main.current_user.id, main.current_user)
        if api.add_share(Share({
        "file_id":self.file.get("id"),
        "delegator_id": main.current_user.id,
        'delegatee_id': user.get("id"),
        "rekey":cfrag.__bytes__()})):
            messagebox.showerror("Success", "success")
            
        else:
            messagebox.showerror("Error", "failed get user")
