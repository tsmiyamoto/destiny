import tkinter as tk
from datetime import datetime as dt


class Gui_output:

    meishiki = None
    birthday = dt.now()
    sex = -1

    def __init__(self, meishiki):

        self.meishiki = meishiki
        self.birthday = meishiki.birthday
        self.sex = meishiki.sex

    def meishiki_output(self):

        root = tk.Tk()

        root.geometry("350x100")

        root.mainloop()
