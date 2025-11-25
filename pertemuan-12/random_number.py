import tkinter as tk
import random

class GuessTheNumber(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tebak Angka")
        self.geometry("300x200")

        self.number_to_guess = random.randint(1, 10)
        self.attempts = 0

        tk.Label(self, text="Tebak angka antara 1 dan 10:").pack(pady=10)
        self.entry_guess = tk.Entry(self)
        self.entry_guess.pack(pady=5)

        tk.Button(self, text="Tebak", command=self.check_guess).pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.result_label.config(text="Terlalu rendah! Coba lagi.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Terlalu tinggi! Coba lagi.")
            else:
                self.result_label.config(text=f"Benar! Kamu menebak dalam {self.attempts} percobaan. \nAngka Random : {self.number_to_guess}")

                self.button_reset = tk.Button(self, text="Main Lagi", command=self.reset_game)
                self.button_reset.pack(pady=10)
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid.")
        self.entry_guess.delete(0, tk.END)

    def reset_game(self):
        self.number_to_guess = random.randint(1, 10)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry_guess.delete(0, tk.END)
        self.button_reset.pack_forget()



if __name__ == "__main__":
    app = GuessTheNumber()
    app.mainloop()