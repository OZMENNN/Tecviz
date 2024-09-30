import tkinter as tk
from tkinter import messagebox
"""
    Verilen m² (alan) değeri için kademeli katsayılarla toplam değer hesaplar.

    Katsayılar:
    0-10 m²      : 0.05
    11-100 m²    : 0.02
    101-500 m²   : 0.01
    501-1000 m²  : 0.005
    1001-5000 m² : 0.004
    5001-25000 m²: 0.003
    25000+ m²    : 0.0015
    """
def hesapla_alan_degeri(m2):
    """
    Verilen m² (alan) değeri için kademeli katsayılarla toplam değer hesaplar.
    """
    try:
        m2 = float(m2)
        toplam_deger = 0

        # 25000+ m² aralığı
        if m2 > 25000:
            toplam_deger += (m2 - 25000) * 0.0015
            m2 = 25000

        # 5001-25000 m² aralığı
        if m2 > 5000:
            toplam_deger += (m2 - 5000) * 0.003
            m2 = 5000

        # 1001-5000 m² aralığı
        if m2 > 1000:
            toplam_deger += (m2 - 1000) * 0.004
            m2 = 1000

        # 501-1000 m² aralığı
        if m2 > 500:
            toplam_deger += (m2 - 500) * 0.005
            m2 = 500

        # 101-500 m² aralığı
        if m2 > 100:
            toplam_deger += (m2 - 100) * 0.01
            m2 = 100

        # 11-100 m² aralığı
        if m2 > 10:
            toplam_deger += (m2 - 10) * 0.02
            m2 = 10

        # 0-10 m² aralığı
        toplam_deger += m2 * 0.05

        return toplam_deger
    except ValueError:
        return None


def hesapla_button_click():
    m2_input = entry_m2.get()
    sonuc = hesapla_alan_degeri(m2_input)

    if sonuc is None:
        messagebox.showerror("Hata", "Lütfen geçerli bir metrekare değeri giriniz!")
    else:
        label_sonuc.config(text=f"Toplam Değer: {sonuc:.2f}")


# Tkinter arayüzü oluşturma
window = tk.Tk()
window.title("Arşiv Onaylı Koordinat Doğruluğu Hesaplama")

# m² Girişi
label_m2 = tk.Label(window, text="Alan Miktarı  Metrekare (m²):")
label_m2.grid(row=0, column=0, padx=10, pady=10)

entry_m2 = tk.Entry(window)
entry_m2.grid(row=0, column=1, padx=10, pady=10)

# Hesapla Butonu
button_hesapla = tk.Button(window, text="Hesapla", command=hesapla_button_click)
button_hesapla.grid(row=1, column=0, columnspan=2, pady=10)

# Sonuç Gösterimi
label_sonuc = tk.Label(window, text="En Çok Değer(+-m²): -")
label_sonuc.grid(row=2, column=0, columnspan=2, pady=10)

# Arayüzü çalıştır
window.mainloop()
