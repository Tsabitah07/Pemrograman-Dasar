import tkinter as tk
from tkinter import ttk

class SecondForm(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Daftar Mahasiswa")
        self.geometry("420x290")
        self.resizable(False, False)

        # Container for treeview + scrollbar
        container = ttk.Frame(self)
        container.pack(padx=10, pady=(10, 5), fill="both", expand=True)

        # Treeview with two columns: NIM and Nama
        columns = ("nim", "nama")
        self.tree = ttk.Treeview(container, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("nim", text="NIM")
        self.tree.heading("nama", text="Nama")
        self.tree.column("nim", width=120, anchor="center")
        self.tree.column("nama", width=260, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)

        # Vertical scrollbar for the treeview
        vsb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        vsb.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=vsb.set)

        # Static student data
        students = [
            ("101001", "Aisyah Rahma"),
            ("101002", "Budi Santoso"),
            ("101003", "Citra Dewi"),
            ("101004", "Dedi Pratama"),
            ("101005", "Eka Putri"),
            ("101006", "Fajar Nugroho"),
            ("101007", "Gina Lestari"),
            ("101008", "Hadi Wijaya"),
            ("101009", "Intan Sari"),
            ("101010", "Joko Susilo"),
            ("101011", "Kiki Amalia"),
            ("101012", "Lina Marlina"),
            ("101013", "Mira Kurnia"),
            ("101014", "Nina Safitri"),
            ("101015", "Oki Prasetyo"),
        ]
        for s in students:
            self.tree.insert("", "end", values=s)

        # Label for selection display
        self.selected_label = ttk.Label(self, text="Terpilih: -")
        self.selected_label.pack(padx=10, pady=(5, 5), anchor="w")

        # Button to show current selection
        btn_frame = ttk.Frame(self)
        btn_frame.pack(padx=10, pady=(0,10), fill="x")
        show_btn = ttk.Button(btn_frame, text="Tampilkan Pilihan", command=self.show_selection)
        show_btn.pack(side="left")

        # Double-click also shows selection
        self.tree.bind("<Double-1>", lambda e: self.show_selection())

    def show_selection(self):
        sel = self.tree.selection()
        if not sel:
            self.selected_label.config(text="Terpilih: -")
            return
        item = sel[0]
        values = self.tree.item(item, "values")
        if values:
            nim, nama = values[0], values[1]
            self.selected_label.config(text=f"Terpilih: NIM = {nim}, Nama = {nama}")
        else:
            self.selected_label.config(text="Terpilih: -")