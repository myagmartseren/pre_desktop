
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/myagmartseren/Documents/school/pre_desktop/build/assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#1A1D2B")


canvas = Canvas(
    window,
    bg = "#1A1D2B",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    50.0,
    233.0,
    284.0,
    276.0,
    fill="#ADD8E6",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    1024.0,
    fill="#ADD8E6",
    outline="")

canvas.create_rectangle(
    349.0,
    182.0,
    1399.0,
    1024.0,
    fill="#D4F1F4",
    outline="")

canvas.create_rectangle(
    348.579345703125,
    90.0,
    1024.8828125,
    140.0,
    fill="#E8EBEC",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    655.5,
    115.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=402.0,
    y=90.0,
    width=507.0,
    height=48.0
)

canvas.create_rectangle(
    363.475830078125,
    99.0,
    392.27587890625,
    128.0,
    fill="#000000",
    outline="")

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
    x=53.0,
    y=403.0,
    width=234.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=53.0,
    y=191.0,
    width=130.0,
    height=51.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
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
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1097.0,
    y=89.0,
    width=182.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
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
    width=237.0,
    height=43.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    126.0,
    126.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    817.0,
    402.0,
    image=image_image_2
)

canvas.create_text(
    481.0,
    467.0,
    anchor="nw",
    text="Аюулгүй фаил хуваалцах үйлчилгээ",
    fill="#003B73",
    font=("Inter Bold", 50 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1330.0,
    y=90.0,
    width=62.0,
    height=43.0
)
window.resizable(False, False)
window.mainloop()