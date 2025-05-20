import tkinter as tk
from tkinter import messagebox
import random

ADIM = "vflhzb1"

SEVIYELER = {
    "Kolay": {"boyut": 9, "mayin": 10},
    "Orta": {"boyut": 12, "mayin": 20},
    "Zor": {"boyut": 15, "mayin": 40},
}

class Hucre:
    def __init__(self, satir, sutun):
        self.satir = satir
        self.sutun = sutun
        self.mayin = False
        self.acik = False
        self.bayrak = False
        self.cevredeki_mayin = 0

class MayinTarlasi:
    def __init__(self, kok, boyut, mayin_sayisi):
        self.kok = kok
        self.boyut = boyut
        self.mayin_sayisi = mayin_sayisi
        self.tahta = [[Hucre(i, j) for j in range(boyut)] for i in range(boyut)]
        self.butonlar = [[None for _ in range(boyut)] for _ in range(boyut)]
        self.oyun_bitti = False

        self.kok.title("💣 Mayın Tarlası")
        self.kok.configure(bg="#1e1e1e")

        self.olustur_gui()
        self.yerlestir_mayinlar()

    def olustur_gui(self):
        for i in range(self.boyut):
            for j in range(self.boyut):
                buton = tk.Button(self.kok, width=3, height=1, bg="#2d2d2d", fg="white",
                                  font=("Helvetica", 10, "bold"),
                                  command=lambda x=i, y=j: self.hucre_ac(x, y))
                buton.bind("<Button-3>", lambda e, x=i, y=j: self.bayrak_degistir(x, y))
                buton.grid(row=i, column=j, padx=1, pady=1)
                self.butonlar[i][j] = buton

        tk.Label(self.kok, text=f"by {ADIM}", font=("Helvetica", 9), fg="gray", bg="#1e1e1e").grid(
            row=self.boyut, column=0, columnspan=self.boyut, pady=5
        )

    def yerlestir_mayinlar(self):
        secilen = random.sample([(i, j) for i in range(self.boyut) for j in range(self.boyut)], self.mayin_sayisi)
        for i, j in secilen:
            self.tahta[i][j].mayin = True

        for i in range(self.boyut):
            for j in range(self.boyut):
                if self.tahta[i][j].mayin:
                    continue
                sayi = sum(self.tahta[x][y].mayin for x in range(max(0, i-1), min(self.boyut, i+2))
                                                  for y in range(max(0, j-1), min(self.boyut, j+2)))
                self.tahta[i][j].cevredeki_mayin = sayi

    def hucre_ac(self, i, j):
        if self.oyun_bitti or self.tahta[i][j].bayrak:
            return
        if self.tahta[i][j].mayin:
            self.butonlar[i][j].config(text="💣", bg="#ff4444")
            self.oyun_bitti = True
            self.oyunu_kaybettin()
            return

        self.acilari_genislet(i, j)
        if self.oyunu_kazandin():
            self.oyunu_kazandin_mesaji()

    def acilari_genislet(self, i, j):
        hucre = self.tahta[i][j]
        if hucre.acik or hucre.bayrak:
            return
        hucre.acik = True
        self.butonlar[i][j].config(relief="sunken", bg="#3e3e3e")
        if hucre.cevredeki_mayin > 0:
            self.butonlar[i][j].config(text=str(hucre.cevredeki_mayin))
        else:
            for x in range(max(0, i-1), min(self.boyut, i+2)):
                for y in range(max(0, j-1), min(self.boyut, j+2)):
                    if not (x == i and y == j):
                        self.acilari_genislet(x, y)

    def bayrak_degistir(self, i, j):
        if self.oyun_bitti or self.tahta[i][j].acik:
            return

        hucre = self.tahta[i][j]
        if hucre.bayrak:
            hucre.bayrak = False
            self.butonlar[i][j].config(text="")
        else:
            hucre.bayrak = True
            self.butonlar[i][j].config(text="🚩")

    def oyunu_kaybettin(self):
        for i in range(self.boyut):
            for j in range(self.boyut):
                hucre = self.tahta[i][j]
                buton = self.butonlar[i][j]
                if hucre.mayin:
                    buton.config(text="💣", bg="#ff4444", fg="white")
        messagebox.showinfo("Oyun Bitti", "💥 Mayına bastın, kaybettin!")

    def oyunu_kazandin(self):
        for i in range(self.boyut):
            for j in range(self.boyut):
                hucre = self.tahta[i][j]
                if not hucre.acik and not hucre.mayin:
                    return False
        return True

    def oyunu_kazandin_mesaji(self):
        self.oyun_bitti = True
        messagebox.showinfo("Tebrikler", "🎉 Tüm mayınlardan kaçındın, kazandın!")

def seviye_secimi_ekrani():
    secim_penceresi = tk.Tk()
    secim_penceresi.title("Mayın Tarlası - Seviye Seç")
    secim_penceresi.configure(bg="#1e1e1e")

    tk.Label(secim_penceresi, text="Zorluk Seviyesi Seçin", font=("Helvetica", 14, "bold"),
             fg="white", bg="#1e1e1e").pack(pady=10)

    def secimi_baslat(seviye):
        secim_penceresi.destroy()
        ana_pencere = tk.Tk()
        ayarlar = SEVIYELER[seviye]
        MayinTarlasi(ana_pencere, ayarlar["boyut"], ayarlar["mayin"])
        ana_pencere.mainloop()

    for seviye in SEVIYELER:
        tk.Button(secim_penceresi, text=seviye, width=15, height=2,
                  command=lambda s=seviye: secimi_baslat(s),
                  bg="#333", fg="white", activebackground="#555", font=("Helvetica", 12)).pack(pady=5)

    tk.Label(secim_penceresi, text=f"by {ADIM}", font=("Helvetica", 10), fg="gray", bg="#1e1e1e").pack(pady=(20, 5))

    secim_penceresi.mainloop()

if __name__ == "__main__":
    seviye_secimi_ekrani()
