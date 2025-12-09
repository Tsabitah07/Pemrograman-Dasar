import tkinter as tk
from tkinter import messagebox
import random
import json

# =======================
# KONSTANTA
# =======================
BOARD_SIZE = 12   # 12 petak mengelilingi papan
START_MONEY = 2000
PASS_START_BONUS = 200

# =======================
# CLASS PROPERTY
# =======================
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

# =======================
# CLASS PLAYER
# =======================
class Player:
    def __init__(self, name, color):
        self.name = name
        self.money = START_MONEY
        self.position = 0
        self.color = color
        self.id_on_board = None

    def move(self, steps):
        old_pos = self.position
        self.position = (self.position + steps) % BOARD_SIZE
        # Lewat start
        if self.position < old_pos:
            self.money += PASS_START_BONUS

# =======================
# CLASS GAME
# =======================
class Game:
    def __init__(self, gui):
        self.gui = gui
        self.properties = [
            Property("Start", 0, 0),
            Property("Rumah A", 100, 20),
            Property("Rumah B", 150, 30),
            Property("Rumah C", 200, 40),
            Property("Parkir", 0, 0),
            Property("Toko A", 250, 50),
            Property("Toko B", 300, 60),
            Property("Toko C", 350, 70),
            Property("Restoran", 450, 85),
            Property("Hotel", 600, 120),
            Property("Pajak", 0, 0),
            Property("Bonus", 0, 0)
        ]

        self.players = [
            Player("Player 1", "red"),
            Player("Player 2", "blue")
        ]

        self.turn = 0

    # -------------- SAVE GAME --------------
    def save_game(self):
        data = {
            "turn": self.turn,
            "players": [
                {
                    "name": p.name,
                    "money": p.money,
                    "position": p.position
                } for p in self.players
            ],
            "owners": [prop.owner for prop in self.properties]
        }
        with open("save.json", "w") as f:
            json.dump(data, f)
        messagebox.showinfo("Saved", "Game berhasil disimpan!")

    # -------------- LOAD GAME --------------
    def load_game(self):
        try:
            with open("save.json", "r") as f:
                data = json.load(f)

            self.turn = data["turn"]
            for i, pdata in enumerate(data["players"]):
                self.players[i].money = pdata["money"]
                self.players[i].position = pdata["position"]

            for i, owner in enumerate(data["owners"]):
                self.properties[i].owner = owner

            self.gui.update_board()
            messagebox.showinfo("Loaded", "Game berhasil dimuat!")
        except Exception:
            messagebox.showerror("Error", "File save tidak ditemukan / rusak!")

    # ----------------- GILIRAN -----------------
    def current_player(self):
        return self.players[self.turn]

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    # ----------------- AKSI BERGERAK -----------------
    def roll_dice(self):
        d = random.randint(1, 6)
        player = self.current_player()
        player.move(d)
        messagebox.showinfo("Dadu", f"{player.name} jalan {d} langkah!")
        self.gui.update_board()
        self.check_tile(player)

    # ----------------- CEK PETAK -----------------
    def check_tile(self, player):
        prop = self.properties[player.position]

        # Pajak
        if prop.name == "Pajak":
            player.money -= 150
            self.gui.update_info()
            return

        # Bonus
        if prop.name == "Bonus":
            player.money += 250
            self.gui.update_info()
            return

        # Petak gratis
        if prop.price == 0:
            return

        # Tempat belum dibeli
        if prop.owner is None:
            buy = messagebox.askyesno("Beli?", f"Beli {prop.name} seharga {prop.price}?")
            if buy and player.money >= prop.price:
                player.money -= prop.price
                prop.owner = player.name
                self.gui.update_info()
            return

        # Sudah ada pemilik, bayar sewa
        if prop.owner != player.name:
            owner = next(p for p in self.players if p.name == prop.owner)
            player.money -= prop.rent
            owner.money += prop.rent
            messagebox.showinfo("Sewa", f"{player.name} bayar {prop.rent} ke {owner.name}")
            self.gui.update_info()

# =======================
# GUI TKINTER
# =======================
class MonopolyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Monopoly Lite")

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack(side="left")

        self.game = Game(self)

        # Tombol aksi
        frame = tk.Frame(root)
        frame.pack(side="right", fill="both", expand=True)

        tk.Button(frame, text="Roll Dice", command=self.roll).pack(pady=10)
        tk.Button(frame, text="Save Game", command=self.game.save_game).pack(pady=10)
        tk.Button(frame, text="Load Game", command=self.game.load_game).pack(pady=10)

        self.info = tk.Label(frame, text="", font=("Arial", 12))
        self.info.pack(pady=10)

        self.draw_board()
        self.update_board()

    # ---------------------- DRAW BOARD ----------------------
    def draw_board(self):
        self.tiles = []
        positions = [
            (500, 500), (400, 500), (300, 500), (200, 500),
            (100, 500), (100, 400), (100, 300), (100, 200),
            (100, 100), (200, 100), (300, 100), (400, 100)
        ]

        for i, pos in enumerate(positions):
            x, y = pos
            tile = self.canvas.create_rectangle(x, y, x+100, y+100, fill="lightyellow")
            text = self.canvas.create_text(x+50, y+50, text=self.game.properties[i].name, font=("Arial", 10))
            self.tiles.append((tile, text))

    # ---------------------- UPDATE BOARD ----------------------
    def update_board(self):
        # hapus token sebelumnya
        for p in self.game.players:
            if p.id_on_board:
                self.canvas.delete(p.id_on_board)

        # gambar token player
        positions = [
            (550, 550), (450, 550), (350, 550), (250, 550),
            (150, 550), (150, 450), (150, 350), (150, 250),
            (150, 150), (250, 150), (350, 150), (450, 150)
        ]

        for p in self.game.players:
            x, y = positions[p.position]
            p.id_on_board = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=p.color)

        self.update_info()

    def update_info(self):
        text = ""
        for p in self.game.players:
            text += f"{p.name}: {p.money}\n"
        text += f"\nGiliran: {self.game.current_player().name}"
        self.info.config(text=text)

    def roll(self):
        self.game.roll_dice()
        self.game.next_turn()
        self.update_info()

# =======================
# MAIN
# =======================
if __name__ == "__main__":
    root = tk.Tk()
    MonopolyGUI(root)
    root.mainloop()