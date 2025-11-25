import tkinter as tk

class GridDemo(tk.Tk):
    def __init__(self):
        super().__init__ ()
        self.title("Contoh grid()")
        self.geometry("300x150")
        tk.Label(self , text="Nama:").grid(row=0, column=0, padx=5, pady =5)
        self.entry_nama = tk.Entry(self)
        self.entry_nama.grid(row=0, column=1, padx=5, pady =5)

        tk.Label(self , text="Umur:").grid(row=1, column=0, padx=5, pady =5)
        self.entry_umur = tk.Entry(self)
        self.entry_umur.grid(row=1, column=1, padx=5, pady =5)

        tk.Button(self , text="Simpan", command=self.show_info).grid(row=2, column=0, columnspan=2, pady=10)

        self.data = tk.Label(self , text="Data akan tampil di sini")
        self.data .grid(row=3, column=0, columnspan=2, pady=5)


    def show_info(self):
        nama = self.entry_nama.get()
        umur = self.entry_umur.get()
        self.data.config(text=f"Nama: {nama}, Umur: {umur}")


if __name__ == "__main__":
    app = GridDemo ()
    app.mainloop ()