from utils import relative_to_assets
from tkinter import Canvas, Entry, Button, PhotoImage

# frame4

class EditView:
    def __init__(self,main):
        self.window = main
        self.window.geometry("1354x676")
        self.window.configure(bg = "#FFFFFF")

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 676,
            width = 1354,
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

        button_image_1 = PhotoImage(
            file=relative_to_assets("frame4/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=695.0,
            y=501.0,
            width=221.0,
            height=32.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("frame4/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=970.0,
            y=501.0,
            width=221.0,
            height=32.0
        )

        canvas.create_text(
            694.0,
            122.0,
            anchor="nw",
            text="Засах",
            fill="#003B73",
            font=("Inter SemiBold", 19 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("frame4/image_1.png"))
        image_1 = canvas.create_image(
            1080.0,
            388.0,
            image=image_image_1
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("frame4/entry_1.png"))
        entry_bg_1 = canvas.create_image(
            1080.5,
            388.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFAFA",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
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
            file=relative_to_assets("frame4/image_2.png"))
        image_2 = canvas.create_image(
            803.0,
            388.0,
            image=image_image_2
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("frame4/entry_2.png"))
        entry_bg_2 = canvas.create_image(
            803.5,
            388.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
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
            file=relative_to_assets("frame4/image_3.png"))
        image_3 = canvas.create_image(
            804.0,
            331.0,
            image=image_image_3
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("frame4/entry_3.png"))
        entry_bg_3 = canvas.create_image(
            804.5,
            331.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
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
            file=relative_to_assets("frame4/image_4.png"))
        image_4 = canvas.create_image(
            804.0,
            271.0,
            image=image_image_4
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("frame4/entry_4.png"))
        entry_bg_4 = canvas.create_image(
            804.5,
            271.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
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
            file=relative_to_assets("frame4/image_5.png"))
        image_5 = canvas.create_image(
            1080.0,
            211.0,
            image=image_image_5
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("frame4/entry_5.png"))
        entry_bg_5 = canvas.create_image(
            1081.0,
            210.5,
            image=entry_image_5
        )
        entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_5.place(
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
            file=relative_to_assets("frame4/image_6.png"))
        image_6 = canvas.create_image(
            804.0,
            211.0,
            image=image_image_6
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("frame4/entry_6.png"))
        entry_bg_6 = canvas.create_image(
            804.5,
            211.0,
            image=entry_image_6
        )
        entry_6 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_6.place(
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
            file=relative_to_assets("frame4/image_7.png"))
        image_7 = canvas.create_image(
            740.0,
            63.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("frame4/image_8.png"))
        image_8 = canvas.create_image(
            287.0,
            338.0,
            image=image_image_8
        )
        self.window.resizable(False, False)
        self.window.mainloop()
