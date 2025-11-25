import tkinter as tk

class EntryDemo(tk.Tk):
    def __init__(self):
        super().__init__ ()
        self.title("Kombinasi Layout")
        self.geometry("300x150")

        self.frame_form = tk.Frame(self, padx=10, pady=10, relief="groove", borderwidth=2)
        self.frame_form.pack(pady=10)

        tk.Label(self.frame_form, text="Nama:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.frame_form).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.frame_form, text="Umur:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.frame_form).grid(row=1, column=1, padx=5, pady=5)

        self.frame_tombol = tk.Frame(self)
        self.frame_tombol.pack(pady=10)

        tk.Button(self.frame_tombol, text="Simpan").pack(side="left", padx=5)
        tk.Button(self.frame_tombol, text="Batal").pack(side="left", padx=5)

if __name__ == "__main__":
    app = EntryDemo ()
    app.mainloop ()