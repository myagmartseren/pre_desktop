from tkinter import Canvas, Entry, Button, PhotoImage, StringVar
from utils import relative_to_assets

files =  list()
for i in range(9):
    files.append("Файл нэр")

class MainView:
    def __init__(self, main):
        self.window = main
        self.files = files
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
            file=relative_to_assets("main/background.png"))
        image_1 = canvas.create_image(
            880.0,
            603.0,
            image=background_image
        )
        #endregion Frame

        #region Files
        file_image = PhotoImage(file=relative_to_assets("main/file.png"))
        x = 443.0
        y = 278.0
        for i in range(3):
            for j in range(3):
                if i*3+j<= len(self.files):
                    self.file_names.append(StringVar())
                    self.file_names[i*3+j].set(self.files[i*3+j])

                    self.file_buttons.append(Button(
                        image=file_image,
                        borderwidth=0,
                        highlightthickness=0,
                        command=lambda: print("button_3 clicked"),
                        relief="flat",
                        textvariable=self.file_names[i*3+j],
                        compound="center",
                    ))
                    self.file_buttons[i*3+j].place(
                        x=x+300*i,
                        y=y+227*j,
                        width=282.0,
                        height=195.0
                    )
        #endregion Files

        #region Left Bar
        #region shared files
        shared_image = PhotoImage(
            file=relative_to_assets("main/shared_files.png"))
        shared_button = Button(
            image=shared_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("shared with me clicked"),
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
            file=relative_to_assets("main/shared_with_me_files.png"))
        shared_with_me_button = Button(
            image=shared_with_me_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
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
            file=relative_to_assets("main/my_files.png"))
        my_files_button = Button(
            image=my_files_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
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
            file=relative_to_assets("main/new_file.png"))
        new_file_button = Button(
            image=new_file_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
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
            file=relative_to_assets("main/logo.png"))
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
            file=relative_to_assets("main/logout.png"))
        logout_button = Button(
            image=logout_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("main/button_14 clicked"),
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
        self.username.set("Хэрэглэгч")

        username_image = PhotoImage(
            file=relative_to_assets("main/username.png"))
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
            file=relative_to_assets("main/search.png"))
        search_canva = canvas.create_image(
            691.0,
            115.0,
            image=search_image
        )
        #endregion Search background

        #region Search entry
        search_entry_image = PhotoImage(
            file=relative_to_assets("main/search_entry.png"))
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
            file=relative_to_assets("main/page_1.png"))
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
            file=relative_to_assets("main/page_2.png"))
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
        #     file=relative_to_assets("main/button_16.png"))
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
