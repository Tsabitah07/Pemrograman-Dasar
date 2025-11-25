import tkinter as tk

class FrameDemo(tk.Tk):
    def __init__(self):
        super().__init__ ()
        self.title("Layout dalam Frame")
        self.geometry("300x200")

        self.frame_atas = tk.Frame(self , bg="lightgray")
        self.frame_atas.pack(fill="x", pady =10)

        tk.Label(self.frame_atas , text="Ini bagian atas").pack(pady =5)

        self.frame_bawah = tk.Frame(self)
        self.frame_bawah.pack(pady =10)

        tk.Button(self.frame_bawah , text="Tombol 1").pack(side="left", padx =5)
        tk.Button(self.frame_bawah , text="Tombol 2").pack(side="left", padx =5)

if __name__ == "__main__":
    app = FrameDemo ()
    app.mainloop ()