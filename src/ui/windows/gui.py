
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#ADD8E6")


canvas = Canvas(
    window,
    bg = "#ADD8E6",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    512.0,
    image=image_image_1
)

canvas.create_rectangle(
    369.0,
    107.0,
    951.0,
    875.0,
    fill="#F5F5F5",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    660.0,
    347.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=463.0,
    y=321.0,
    width=394.0,
    height=51.0
)

canvas.create_text(
    458.0,
    288.0,
    anchor="nw",
    text="Имэйл хаяг ",
    fill="#003B73",
    font=("Inter SemiBold", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    660.0,
    464.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=463.0,
    y=438.0,
    width=394.0,
    height=51.0
)

canvas.create_text(
    458.0,
    405.0,
    anchor="nw",
    text="Нууц үг\n",
    fill="#003B73",
    font=("Inter SemiBold", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=458.0,
    y=537.0,
    width=404.0,
    height=53.0
)

canvas.create_text(
    458.0,
    230.0,
    anchor="nw",
    text="Нэвтрэх",
    fill="#003B73",
    font=("Inter SemiBold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
