# Validebağ Fen Lisesi Hazırlık Bilişim Teknolojileri Dersi Sene Sonu Performans Ödevi



# 🖥️ Tkinter Uygulama Başlatıcı (Ana Menü)

Bu proje, Python ve Tkinter kullanılarak geliştirilmiş üç farklı GUI uygulamasını merkezi bir menüden başlatmanızı sağlar. Kullanıcı dostu bir arayüzle tüm projelerinizi tek bir ana pencereden başlatabilirsiniz.

## 📦 İçerik

Proje, aşağıdaki üç bağımsız uygulamayı içerir:

| Uygulama Adı                    | Açıklama |
|--------------------------------|----------|
| `alan_hesaplama.py`            | Kullanıcının girdiği geometrik şekillere göre alan hesaplayan uygulama. |
| `mayin.py`                     | Klasik Mayın Tarlası (Minesweeper) oyununun basit bir sürümü. |
| `vki.py`                       | Kullanıcının boy ve kilosunu alarak Vücut Kitle İndeksi (VKİ) hesaplayan uygulama. |

Tüm bu uygulamalar, `main.py` dosyası üzerinden seçilerek çalıştırılabilir.

## 🚀 Başlangıç

### Gereksinimler

- Python 3.7 veya üzeri
- Tkinter (Python ile birlikte gelir)

### Kurulum

1. Bu repoyu klonlayın:

```bash
git clone https://github.com/kullanici_adi/tkinter-app-launcher.git
cd tkinter-app-launcher
```

2. Python ortamınızı oluşturun (opsiyonel ama önerilir):

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

## ⚙️ Kullanım

Ana menüyü başlatmak için:

```bash
python main.py
```

Açılan pencerede üç seçenekten birini seçerek ilgili uygulamayı çalıştırabilirsiniz. Her uygulama yeni bir pencerede başlatılır ve ana menü açık kalmaya devam eder.

## 📁 Proje Yapısı

```
itperformanceasgmt/
├── main.py                # Ana menü (uygulama başlatıcı)
├── alan_hesaplama.py      # Geometrik alan hesaplama arayüzü
├── mayin.py               # Mayın Tarlası oyunu
├── vki.py                 # Vücut Kitle İndeksi hesaplayıcı
└── README.md              # Proje açıklaması (bu dosya)
```

## 🎨 Arayüz

Ana menü sade ve modern bir koyu tema ile tasarlanmıştır. Butonlar `ttk.Style` ile özelleştirilmiş, arayüz hem estetik hem kullanıcı dostu olacak şekilde düzenlenmiştir.

## 🛠️ Derleme (Opsiyonel)

Bu projeyi tek başına çalışabilen bir `.exe` haline getirmek isterseniz:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

> Bu komutla `dist/` klasörü içinde `main.exe` dosyası oluşturulur. Diğer `.py` dosyalarının da aynı klasörde olması gerekir veya `.spec` dosyası düzenlenmelidir.

## 👥 Ekip

- **Muhammed Ömer ERKOÇ** - Hz/B - 433
- **Taha AYDIN** - Hz/B - 433
- **Taha AYDIN** - Hz/B - 433

## 📜 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına göz atabilirsiniz.
