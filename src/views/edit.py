from utils import relative_to_assets
from tkinter import Canvas, Entry, Button, PhotoImage

class EditView:
    def __init__(self,main):
        self.window = main
        self.window.geometry("423x299")
        self.window.configure(bg = "#FFFFFF")

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
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=33.0,
            y=238.0,
            width=363.0,
            height=37.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("frame5/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
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
        entry_1 = Entry(
            bd=0,
            bg="#F5F5F5",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
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
        self.window.resizable(False, False)
        self.window.mainloop()
