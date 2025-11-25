from tkinter import filedialog
import tkinter as tk


class GambarDemo(tk.Tk):
    def __init__(self):
        super().__init__ ()
        self.title("Image Page")
        self.geometry("400x600")

        self.label = tk.Label(self);
        self.label.pack()

        tk.Button(self ,text="Pilih",command=self.pilih).pack()
        tk.Button(self ,text="Hapus",command=self.hapus).pack()


    def pilih(self):
        f = filedialog.askopenfilename(
        filetypes =[("Image","*.png;*.gif" )])

        if f:
            img = tk.PhotoImage(file=f)
            self.label.img = img
            self.label.config(image=img)

    def hapus(self):
        self.label.config(image='')

if __name__ == "__main__":
    app = GambarDemo()
    app.mainloop()