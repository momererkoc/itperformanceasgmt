import tkinter as tk
from tkinter import ttk
import subprocess
import os
import sys

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Uygulama Ana Menüsü")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TButton", font=("Segoe UI", 12), foreground="white", background="#3a3a3a")
        self.style.map("TButton", background=[("active", "#00bfff")])

        ttk.Label(root, text="Uygulama Seçin", font=("Segoe UI", 14, "bold"), foreground="white", background="#1e1e1e").pack(pady=20)

        ttk.Button(root, text="Geometrik Alan Hesaplama", command=self.run_alan).pack(pady=10)
        ttk.Button(root, text="Mayın Tarlası", command=self.run_mayin).pack(pady=10)
        ttk.Button(root, text="Vücut Kitle İndeksi (VKİ)", command=self.run_vki).pack(pady=10)

        tk.Label(root, text="By vflhzb1", font=("Segoe UI", 10, "italic"), fg="gray", bg="#1e1e1e").pack(side="bottom", pady=10)

    def run_script(self, filename):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)
        script_path = os.path.join(base_path, filename)
        subprocess.Popen([sys.executable, script_path])

    def run_alan(self):
        self.run_script("alan_hesaplama.py")

    def run_mayin(self):
        self.run_script("mayin.py")

    def run_vki(self):
        self.run_script("vki.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
