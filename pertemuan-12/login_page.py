import tkinter as tk

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x300")

        self.label_welcome = tk.Label(self, text="Welcome, Please Login", font=("Arial", 16))
        self.label_welcome.pack(pady=20)

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=(10, 2))

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=(2, 5))

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=2)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=(2, 5))

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=10, padx=50)

        self.label_success = tk.Label(self, text="Login Success", fg="green")
        self.label_success.pack_forget()

        self.label_failed = tk.Label(self, text="Login Failed \nUsername / Password Salah", fg="red")
        self.label_failed.pack_forget()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "1234":
            print("Login successful!")

            # self.label_success.config()
            self.label_success.pack()

            self.label_failed.pack_forget()
        else:
            print("Login failed. Please try again.")

            # self.label_failed.config()
            self.label_failed.pack()

            self.label_success.pack_forget()

        print(f"Username: {username}, Password: {password}")

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()