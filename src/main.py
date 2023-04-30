import tkinter as tk
from ui.windows.main_window import MainWindow


def main():
    # Create the root Tkinter window
    root = tk.Tk()

    # Create the main application window
    main_window = MainWindow(root)

    # Start the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
