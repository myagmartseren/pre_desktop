from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from utils import relative_to_assets


class MainView:
    def __init__(self,main,db):
        self.window = main
        self.db=db
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#1A1D2B")
        self.window.resizable(False, False)

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

        image_image_1 = PhotoImage(
            file=relative_to_assets("frame2/image_1.png"))
        image_1 = canvas.create_image(
            880.0,
            603.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("frame2/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=1099.0,
            y=278.0,
            width=282.0,
            height=195.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("frame2/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=773.0,
            y=278.0,
            width=282.0,
            height=195.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("frame2/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=443.0,
            y=278.0,
            width=282.0,
            height=195.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("frame2/button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=50.0,
            y=397.0,
            width=239.0,
            height=46.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("frame2/button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=50.0,
            y=331.0,
            width=239.0,
            height=43.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("frame2/button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=53.0,
            y=265.0,
            width=236.0,
            height=43.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("frame2/button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=53.0,
            y=191.0,
            width=130.0,
            height=51.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("frame2/image_2.png"))
        image_2 = canvas.create_image(
            126.0,
            126.0,
            image=image_image_2
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("frame2/button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=1333.0,
            y=90.0,
            width=62.0,
            height=43.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("frame2/button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=1105.0,
            y=89.0,
            width=184.0,
            height=50.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("frame2/image_3.png"))
        image_3 = canvas.create_image(
            691.0,
            115.0,
            image=image_image_3
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("frame2/entry_1.png"))
        entry_bg_1 = canvas.create_image(
            706.5,
            114.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#E8EBEC",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=400.0,
            y=93.0,
            width=613.0,
            height=41.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()
