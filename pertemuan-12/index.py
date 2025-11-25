import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("800x600")

        self.label_welcome = tk.Label(self, text="Welcome to the Main Window!", font=("Arial", 24))
        self.label_welcome.pack(pady=50)

        self.button_proceed = tk.Button(self, text="Proceed", font=("Arial", 16))
        self.button_proceed.pack(pady=20)



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()