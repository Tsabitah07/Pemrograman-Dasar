# python
import tkinter as tk
from tkinter import filedialog, ttk
try:
    from PIL import Image, ImageTk, ImageSequence
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False


class Player:
    def __init__(self, canvas: tk.Canvas, x: int, y: int, name: str):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.name = name
        self.frames = []  # list of tk.PhotoImage frames
        self.frame_index = 0
        self.image_id = None
        self.anim_delay = 100  # ms between frames
        self._anim_running = False

    def load_from_file(self, path: str):
        if not path:
            return
        self.frames.clear()
        if PIL_AVAILABLE:
            img = Image.open(path)
            # collect frames
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert("RGBA")
                tkimg = ImageTk.PhotoImage(frame)
                self.frames.append(tkimg)
            # try to read duration from image (use first frame if not present)
            try:
                self.anim_delay = img.info.get("duration", self.anim_delay)
            except Exception:
                pass
        else:
            # fallback: single-frame PhotoImage (tk supports GIF)
            try:
                tkimg = tk.PhotoImage(file=path)
                self.frames.append(tkimg)
            except Exception as e:
                print("Failed to load image:", e)
                return

        # create or update canvas image
        if self.image_id is None:
            self.image_id = self.canvas.create_image(self.x, self.y, image=self.frames[0], anchor="nw")
        else:
            self.canvas.itemconfig(self.image_id, image=self.frames[0])
        self.frame_index = 0
        if not self._anim_running and len(self.frames) > 1:
            self._anim_running = True
            self._animate()

    def _animate(self):
        if not self._anim_running or not self.frames:
            return
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        try:
            self.canvas.itemconfig(self.image_id, image=self.frames[self.frame_index])
        except Exception:
            pass
        # schedule next frame
        self.canvas.after(self.anim_delay, self._animate)

    def stop_animation(self):
        self._anim_running = False

    def move(self, dx: int, dy: int):
        self.canvas.move(self.image_id, dx, dy)
        # update internal coordinates
        self.x += dx
        self.y += dy


class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Two Players - Animated GIFs (WASD + Arrows)")
        self.geometry("800x600")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=780, height=520, bg="lightgray")
        self.canvas.pack(padx=10, pady=10)

        control_frame = ttk.Frame(self)
        control_frame.pack(fill="x", padx=10)

        btn1 = ttk.Button(control_frame, text="Load Player 1 GIF (W/A/S/D)", command=self.load_player1)
        btn1.pack(side="left", padx=5)
        btn2 = ttk.Button(control_frame, text="Load Player 2 GIF (Arrows)", command=self.load_player2)
        btn2.pack(side="left", padx=5)

        # initial positions
        self.player1 = Player(self.canvas, 50, 50, "Player1")
        self.player2 = Player(self.canvas, 600, 350, "Player2")

        # create placeholders so there is always an image_id to move
        placeholder = tk.PhotoImage(width=64, height=64)
        # fill placeholder with a simple pixel so it isn't empty
        placeholder.put(("red",), to=(0, 0, 63, 63))
        self.player1.frames = [placeholder]
        self.player1.image_id = self.canvas.create_image(self.player1.x, self.player1.y, image=placeholder, anchor="nw")
        placeholder2 = tk.PhotoImage(width=64, height=64)
        placeholder2.put(("blue",), to=(0, 0, 63, 63))
        self.player2.frames = [placeholder2]
        self.player2.image_id = self.canvas.create_image(self.player2.x, self.player2.y, image=placeholder2, anchor="nw")

        # key mapping
        self.p1_map = {
            "w": (0, -10),
            "s": (0, 10),
            "a": (-10, 0),
            "d": (10, 0),
        }
        self.p2_map = {
            "Up": (0, -10),
            "Down": (0, 10),
            "Left": (-10, 0),
            "Right": (10, 0),
        }

        # bind keypress to the root window as required
        self.bind("<KeyPress>", self.on_key)
        # ensure focus so key events are received
        self.focus_force()

    def load_player1(self):
        path = filedialog.askopenfilename(title="Select GIF for Player 1", filetypes=[("GIF files", "*.gif"), ("All files", "*.*")])
        if path:
            self.player1.load_from_file(path)

    def load_player2(self):
        path = filedialog.askopenfilename(title="Select GIF for Player 2", filetypes=[("GIF files", "*.gif"), ("All files", "*.*")])
        if path:
            self.player2.load_from_file(path)

    def on_key(self, event):
        key = event.keysym
        # normalize lower-case letters for WASD
        if len(key) == 1:
            key = key.lower()
        if key in self.p1_map:
            dx, dy = self.p1_map[key]
            self.player1.move(dx, dy)
        elif key in self.p2_map:
            dx, dy = self.p2_map[key]
            self.player2.move(dx, dy)


if __name__ == "__main__":
    app = GameWindow()
    app.mainloop()