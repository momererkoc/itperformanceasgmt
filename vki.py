import tkinter as tk
from tkinter import ttk

class VKIHesaplayici:
    def __init__(self, kok):
        self.kok = kok
        self.kok.title("Vücut Kitle İndeksi (BMI) Hesaplayıcı")

        arka_plan = "#1e1e1e"
        yazı_rengi = "#ffffff"
        giriş_arka_plan = "#2e2e2e"
        buton_arka_plan = "#3a3a3a"
        vurgulama = "#00bfff"

        self.kok.configure(bg=arka_plan)

        stil = ttk.Style()
        stil.theme_use('clam')
        stil.configure("TLabel", background=arka_plan, foreground=yazı_rengi, font=("Segoe UI", 11))
        stil.configure("TButton", background=buton_arka_plan, foreground=yazı_rengi, font=("Segoe UI", 11))
        stil.map("TButton", background=[("active", vurgulama)])

        # Girdi alanları
        ttk.Label(kok, text="Boy (m):").grid(column=0, row=0, padx=10, pady=5, sticky="e")
        self.girdi_boy = tk.Entry(kok, bg=giriş_arka_plan, fg=yazı_rengi, insertbackground=yazı_rengi, relief="flat", bd=0, font=("Segoe UI", 10))
        self.girdi_boy.grid(column=1, row=0, padx=10, pady=5, sticky="ew")

        ttk.Label(kok, text="Kilo (kg):").grid(column=0, row=1, padx=10, pady=5, sticky="e")
        self.girdi_kilo = tk.Entry(kok, bg=giriş_arka_plan, fg=yazı_rengi, insertbackground=yazı_rengi, relief="flat", bd=0, font=("Segoe UI", 10))
        self.girdi_kilo.grid(column=1, row=1, padx=10, pady=5, sticky="ew")

        ttk.Label(kok, text="Yaş:").grid(column=0, row=2, padx=10, pady=5, sticky="e")
        self.girdi_yas = tk.Entry(kok, bg=giriş_arka_plan, fg=yazı_rengi, insertbackground=yazı_rengi, relief="flat", bd=0, font=("Segoe UI", 10))
        self.girdi_yas.grid(column=1, row=2, padx=10, pady=5, sticky="ew")

        ttk.Button(kok, text="BMI Hesapla", command=self.hesapla_bki).grid(column=0, row=3, columnspan=2, pady=15)

        self.sonuc_yazisi = ttk.Label(kok, text="", font=("Segoe UI", 12, "bold"), foreground=vurgulama)
        self.sonuc_yazisi.grid(column=0, row=4, columnspan=2, pady=10)

        self.cizim_alani = tk.Canvas(kok, width=200, height=300, bg="#2e2e2e", highlightthickness=0)
        self.cizim_alani.grid(column=0, row=5, columnspan=2, pady=10)

        self.ad_etiketi = tk.Label(kok, text="by vflhzb1", bg=arka_plan, fg="#888888", font=("Segoe UI", 10, "italic"))
        self.ad_etiketi.grid(column=0, row=6, columnspan=2, pady=(5, 10))

        kok.columnconfigure(1, weight=1)

    def kategori_bki(self, bki):
        if bki <= 18.5:
            return "Düşük Kilolu"
        elif 18.5 < bki <= 24.9:
            return "Normal Kilolu"
        elif 25 <= bki <= 29.9:
            return "Fazla Kilolu"
        elif 30 <= bki <= 40:
            return "Obez"
        else:
            return "Aşırı Obez"

    def renk_bki(self, kategori):
        renkler = {
            "Düşük Kilolu": "#3399FF",
            "Normal Kilolu": "#33CC33",
            "Fazla Kilolu": "#FFCC33",
            "Obez": "#FF6600",
            "Aşırı Obez": "#CC3300"
        }
        return renkler.get(kategori, "#3399FF")

    def hesapla_bki(self):
        try:
            boy = float(self.girdi_boy.get())
            kilo = float(self.girdi_kilo.get())
            yas = int(self.girdi_yas.get())

            if boy <= 0 or kilo <= 0 or yas <= 0:
                raise ValueError

            if yas < 14:
                self.sonuc_yazisi.config(text="14 yaş altına hesaplama yapılamaz.", foreground="#FF4444")
                self.cizim_alani.delete("all")
                return

            bki = kilo / (boy ** 2)
            kategori = self.kategori_bki(bki)
            renk = self.renk_bki(kategori)

            self.sonuc_yazisi.config(text=f"BMI: {bki:.2f} - {kategori}", foreground=renk)

            self.cizim_alani.delete("all")
            self.cizim_beden(bki, renk)

        except ValueError:
            self.sonuc_yazisi.config(text="Lütfen geçerli pozitif sayılar girin.", foreground="#FF4444")
            self.cizim_alani.delete("all")

    def cizim_beden(self, bki, renk):
        self.cizim_alani.delete("all")

        merkez_x = 100
        bas_y = 40
        govde_ust_y = 80
        govde_alt_y = 220
        kol_y = 120
        bacak_ust_y = govde_alt_y
        bacak_alt_y = 280

        cizgi_renk = "#222222"

        bki_sinirli = max(10, min(bki, 50))
        genislik = 40 + ((bki_sinirli - 10) / 40) * 70

        bas_cap = 30
        self.cizim_alani.create_oval(merkez_x - bas_cap, bas_y - bas_cap,
                                     merkez_x + bas_cap, bas_y + bas_cap,
                                     fill=renk, outline=cizgi_renk, width=2)

        boyun_genislik = 15
        boyun_yukseklik = 15
        self.cizim_alani.create_rectangle(merkez_x - boyun_genislik//2, bas_y + bas_cap,
                                         merkez_x + boyun_genislik//2, bas_y + bas_cap + boyun_yukseklik,
                                         fill=renk, outline=cizgi_renk, width=2)

        self.cizim_alani.create_oval(merkez_x - genislik/2, govde_ust_y, merkez_x + genislik/2, govde_alt_y,
                                     fill=renk, outline=cizgi_renk, width=2)

        kol_uzunluk = 60
        kol_kalinlik = 8 + (bki_sinirli - 10) / 40 * 7

        self.cizim_alani.create_line(merkez_x - genislik/2, kol_y,
                                     merkez_x - genislik/2 - kol_uzunluk, kol_y + 40,
                                     width=kol_kalinlik, fill=renk)

        self.cizim_alani.create_line(merkez_x + genislik/2, kol_y,
                                     merkez_x + genislik/2 + kol_uzunluk, kol_y + 40,
                                     width=kol_kalinlik, fill=renk)

        bacak_kalinlik = 10 + (bki_sinirli - 10) / 40 * 10

        self.cizim_alani.create_line(merkez_x - genislik/4, bacak_ust_y,
                                     merkez_x - genislik/4, bacak_alt_y,
                                     width=bacak_kalinlik, fill=renk)

        self.cizim_alani.create_line(merkez_x + genislik/4, bacak_ust_y,
                                     merkez_x + genislik/4, bacak_alt_y,
                                     width=bacak_kalinlik, fill=renk)

if __name__ == "__main__":
    kok = tk.Tk()
    uygulama = VKIHesaplayici(kok)
    kok.mainloop()