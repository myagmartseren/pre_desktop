from tkinter import Canvas, Entry, Button, PhotoImage, Frame
from utils import relative_to_assets

# frame1
class HomeView(Frame):
    def __init__(self,main):
        self.window = main
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
            1440.0,
            1024.0,
            fill="#ADD8E6",
            outline="")

        image_image_1 = PhotoImage(file=relative_to_assets("frame1/image_1.png"))
        image_1 = canvas.create_image(
            874.0,
            603.0,
            image=image_image_1
        )

        canvas.create_text(
            481.0,
            467.0,
            anchor="nw",
            text="Аюулгүй фаил хуваалцах үйлчилгээ",
            fill="#003B73",
            font=("Inter Bold", 50 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("frame1/image_2.png"))
        image_2 = canvas.create_image(
            817.0,
            402.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("frame1/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=53.0,
            y=403.0,
            width=234.0,
            height=43.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("frame1/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=50.0,
            y=331.0,
            width=237.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("frame1/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=52.0,
            y=265.0,
            width=234.0,
            height=43.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("frame1/button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=53.0,
            y=191.0,
            width=130.0,
            height=51.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("frame1/button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=1330.0,
            y=92.0,
            width=62.0,
            height=43.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("frame1/button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=1097.0,
            y=89.0,
            width=182.0,
            height=50.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("frame1/image_3.png"))
        image_3 = canvas.create_image(
            686.579345703125,
            115.0,
            image=image_image_3
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("frame1/entry_1.png"))
        entry_bg_1 = canvas.create_image(
            706.0,
            114.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FDFEFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=408.0,
            y=96.0,
            width=596.0,
            height=35.0
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("frame1/image_4.png"))
        image_4 = canvas.create_image(
            126.0,
            126.0,
            image=image_image_4
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("frame1/button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=53.0,
            y=736.0,
            width=237.0,
            height=43.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("frame1/button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=50.0,
            y=845.0,
            width=234.0,
            height=43.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()
