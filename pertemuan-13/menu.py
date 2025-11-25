import tkinter as tk

class MenuDemo(tk.Tk):
    def __init__(self):
        super().__init__ ()
        self.title("Judul Awal")

        m = tk.Menu(self)

        f = tk.Menu(m, tearoff =0)
        f.add_command(label="Ubah Judul", command=self.ubah)
        f.add_command(label="Keluar", command=self.quit)

        m.add_cascade(label="File", menu=f)

        self.config(menu=m)

    def ubah(self):
        self.title("Judul Berubah!")


if __name__ == "__main__":
    app = MenuDemo()
    app.mainloop()