import tkinter as tk
from tkinter import ttk
from latihan_2_second_form import SecondForm

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Data Mahasiswa - Main")
        self.geometry("400x140")
        self.resizable(False, False)

        lbl = ttk.Label(self, text="Aplikasi Data Mahasiswa", font=("Segoe UI", 12))
        lbl.pack(pady=(30,10))

        menubar = tk.Menu(self)
        nav_menu = tk.Menu(menubar, tearoff=0)
        nav_menu.add_command(label="Daftar Mahasiswa", command=self.open_second_form)
        nav_menu.add_command(label="Keluar", command=self.quit)
        menubar.add_cascade(label="Navigasi", menu=nav_menu)
        self.config(menu=menubar)

        self._second_form = None

    def open_second_form(self):
        if self._second_form is None or not tk.Toplevel.winfo_exists(self._second_form):
            self._second_form = SecondForm(self)
        else:
            self._second_form.lift()
            self._second_form.focus_force()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()