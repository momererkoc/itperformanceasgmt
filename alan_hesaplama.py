import tkinter as tk
from tkinter import ttk

class GeometryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometrik Şekil Alan Hesaplayıcı")

        bg_color = "#1e1e1e"
        fg_color = "#ffffff"
        entry_bg = "#2e2e2e"
        button_bg = "#3a3a3a"
        highlight = "#00bfff"

        self.root.configure(bg=bg_color)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Segoe UI", 11))
        style.configure("TButton", background=button_bg, foreground=fg_color, font=("Segoe UI", 11))
        style.map("TButton", background=[("active", highlight)])

        self.shapes = ["Kare", "Dikdörtgen", "Yamuk", "Paralelkenar", "Eşkenar Dörtgen"]
        self.selected_shape = tk.StringVar(value=self.shapes[0])

        ttk.Label(root, text="Şekil Seçin:").grid(column=0, row=0, padx=10, pady=5, sticky="w")
        self.shape_menu = ttk.OptionMenu(root, self.selected_shape, self.shapes[0], *self.shapes, command=self.update_fields)
        self.shape_menu.grid(column=1, row=0, sticky="ew", padx=5)

        self.units = ["mm", "cm", "m", "inch"]
        self.selected_unit = tk.StringVar(value=self.units[1])

        ttk.Label(root, text="").grid(column=0, row=6, padx=10, pady=5, sticky="w")
        self.unit_menu = ttk.OptionMenu(root, self.selected_unit, self.units[1], *self.units)
        self.unit_menu.grid(column=0, row=6, columnspan=2, pady=5)


        self.input_frame = ttk.Frame(root)
        self.input_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.inputs = {}
        self.update_fields(self.shapes[0])

        ttk.Button(root, text="Alanı Hesapla", command=self.calculate_area).grid(column=0, row=7, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="", font=("Segoe UI", 12, "bold"), foreground=highlight)
        self.result_label.grid(column=0, row=8, columnspan=2)

        self.canvas = tk.Canvas(root, width=320, height=200, bg="#2b2b2b", highlightthickness=0)
        self.canvas.grid(column=0, row=9, columnspan=2, pady=10)

        self.footer = tk.Label(root, text="By vflhzb1", fg="#666666", bg=bg_color, font=("Segoe UI", 10, "italic"))
        self.footer.grid(column=0, row=10, columnspan=2, pady=(0, 8))

    def update_fields(self, shape):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.inputs.clear()

        fields = {
            "Kare": ["Kenar"],
            "Dikdörtgen": ["Kısa Kenar", "Uzun Kenar"],
            "Yamuk": ["Üst Taban", "Alt Taban", "Yükseklik"],
            "Paralelkenar": ["Taban", "Yükseklik"],
            "Eşkenar Dörtgen": ["Köşegen1", "Köşegen2"]
        }

        for i, label in enumerate(fields[shape]):
            ttk.Label(self.input_frame, text=label + ":").grid(row=i, column=0, sticky="e", pady=3)

            entry = tk.Entry(
                self.input_frame,
                bg="#2e2e2e",
                fg="#ffffff",
                insertbackground="#ffffff",
                highlightthickness=2,
                highlightbackground="#888888",
                highlightcolor="#00bfff",
                relief="flat",
                bd=0,
                font=("Segoe UI", 10)
            )

            entry.grid(row=i, column=1, pady=3, padx=5)
            self.inputs[label] = entry

    def calculate_area(self):
        try:
            shape = self.selected_shape.get()
            vals = {k: float(v.get()) for k, v in self.inputs.items()}
            unit = self.selected_unit.get()

            # Alan hesaplama
            if shape == "Kare":
                area = vals["Kenar"] ** 2
            elif shape == "Dikdörtgen":
                area = vals["Kısa Kenar"] * vals["Uzun Kenar"]
            elif shape == "Yamuk":
                area = ((vals["Üst Taban"] + vals["Alt Taban"]) * vals["Yükseklik"]) / 2
            elif shape == "Paralelkenar":
                area = vals["Taban"] * vals["Yükseklik"]
            elif shape == "Eşkenar Dörtgen":
                area = (vals["Köşegen1"] * vals["Köşegen2"]) / 2
            else:
                area = 0

            area_m2 = self.convert_area_to_m2(area, unit)

            result_text = (
                f"{shape} Alanı:\n"
                f"{area:.2f} {unit}²\n"
                f"{self.convert_area_m2_to(area_m2, 'mm'):.2f} mm²\n"
                f"{self.convert_area_m2_to(area_m2, 'cm'):.2f} cm²\n"
                f"{self.convert_area_m2_to(area_m2, 'm'):.4f} m²\n"
                f"{self.convert_area_m2_to(area_m2, 'inch'):.2f} inch²"
            )

            self.result_label.config(text=result_text)
            self.draw_shape(shape, vals)

        except ValueError:
            self.result_label.config(text="Lütfen geçerli sayılar girin.")

    def convert_area_to_m2(self, area, unit):
        if unit == "mm":
            return area / 1_000_000
        elif unit == "cm":
            return area / 10_000
        elif unit == "m":
            return area
        elif unit == "inch":
            return area * 0.00064516
        else:
            return area

    def convert_area_m2_to(self, area_m2, target_unit):
        if target_unit == "mm":
            return area_m2 * 1_000_000
        elif target_unit == "cm":
            return area_m2 * 10_000
        elif target_unit == "m":
            return area_m2
        elif target_unit == "inch":
            return area_m2 / 0.00064516
        else:
            return area_m2

    def draw_shape(self, shape, vals):
        self.canvas.delete("all")

        if shape == "Kare":
            l = min(100, vals["Kenar"])
            self.animate_rectangle(100, 50, l, l)

        elif shape == "Dikdörtgen":
            w = min(150, vals["Uzun Kenar"])
            h = min(100, vals["Kısa Kenar"])
            self.animate_rectangle(75, 50, w, h)

        elif shape == "Yamuk":
            top = vals["Üst Taban"]
            bottom = vals["Alt Taban"]
            h = vals["Yükseklik"]
            self.animate_trapezoid(top, bottom, h)

        elif shape == "Paralelkenar":
            base = vals["Taban"]
            h = vals["Yükseklik"]
            self.animate_parallelogram(base, h)

        elif shape == "Eşkenar Dörtgen":
            d1 = vals["Köşegen1"]
            d2 = vals["Köşegen2"]
            self.animate_rhombus(d1, d2)

    def animate_rectangle(self, x, y, w, h):
        for i in range(1, 11):
            self.canvas.delete("all")
            self.canvas.create_rectangle(x, y, x + w * i/10, y + h * i/10, fill="#4da6ff", outline="")
            self.root.update()
            self.canvas.after(40)

    def animate_trapezoid(self, top, bottom, h):
        top = min(100, top)
        bottom = min(150, bottom)
        h = min(100, h)
        for i in range(1, 11):
            self.canvas.delete("all")
            dx = (bottom - top) / 2
            points = [
                100 + dx * i/10, 50,
                100 + (top + dx) * i/10, 50,
                100 + bottom * i/10, 50 + h * i/10,
                100, 50 + h * i/10
            ]
            self.canvas.create_polygon(points, fill="#7fc97f", outline="")
            self.root.update()
            self.canvas.after(40)

    def animate_parallelogram(self, base, h):
        base = min(150, base)
        h = min(100, h)
        for i in range(1, 11):
            self.canvas.delete("all")
            points = [
                80, 50,
                80 + base * i/10, 50,
                60 + base * i/10, 50 + h * i/10,
                60, 50 + h * i/10
            ]
            self.canvas.create_polygon(points, fill="#fdae61", outline="")
            self.root.update()
            self.canvas.after(40)

    def animate_rhombus(self, d1, d2):
        d1 = min(100, d1)
        d2 = min(100, d2)
        for i in range(1, 11):
            self.canvas.delete("all")
            x = 150
            y = 100
            points = [
                x, y - d2 * i/20,
                x + d1 * i/20, y,
                x, y + d2 * i/20,
                x - d1 * i/20, y
            ]
            self.canvas.create_polygon(points, fill="#d95f02", outline="")
            self.root.update()
            self.canvas.after(40)

root = tk.Tk()
app = GeometryApp(root)
root.mainloop()
