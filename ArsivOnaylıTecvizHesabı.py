import tkinter as tk
from tkinter import messagebox

def calculate_max_value(area):
    # 18.madde uygulama örnekleri standart
    thresholds = [
        (0, 10, 0.05),
        (11, 100, 0.02),
        (101, 500, 0.01),
        (501, 1000, 0.005),
        (1001, 5000, 0.004),
        (5001, 25000, 0.003),
        (25001, float('inf'), 0.0015)
    ]

    total_value = 0.0

    for low, high, rate in thresholds:
        if area > high:

            if low > 0:
                segment_area = high - low + 1
            else:
                segment_area = high - low + 1
            total_value += segment_area * rate
        else:

            if area > low:
                segment_area = area - low + 1
                total_value += segment_area * rate
            break  # Hesaplama tamam

    return total_value

def calculate():
    try:
        area = float(entry_area.get())
        if area < 0:
            messagebox.showerror("Hata", "Alan değeri negatif olamaz. Lütfen geçerli bir değer girin.")
            return
        max_value = calculate_max_value(area)
        result_var.set(f"Alan: {area} m2, En Çok Değer: {max_value:.2f}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

# windows formu için
window = tk.Tk()
window.title("Arşiv Onaylı Koordinat Doğruluğu Hesaplama Uygulaması")


label_area = tk.Label(window, text="Alan (m2):")
label_area.pack(pady=10)

entry_area = tk.Entry(window)
entry_area.pack(pady=5)

#  buton
button_calculate = tk.Button(window, text="Hesapla", command=calculate)
button_calculate.pack(pady=20)


result_var = tk.StringVar()
label_result = tk.Label(window, textvariable=result_var)
label_result.pack(pady=10)


window.mainloop()
