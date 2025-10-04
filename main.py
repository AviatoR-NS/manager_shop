import tkinter as tk
from gui import StoreApp


def main():
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

