# Menampilkan judul program
print("\n === KALKULATOR KOORDINAT ===")

# Menerima koordinat x dan y untuk titik A serta titik B sebagai float
x1 = float(input("Masukkan koordinat x1 (titik A): "))
y1 = float(input("Masukkan koordinat y1 (titik A): "))
x2 = float(input("Masukkan koordinat x2 (titik B): "))
y2 = float(input("Masukkan koordinat y2 (titik B): "))

# Rumus menghitung perubahan koordinat
dx = x2 - x1
dy = y2 - y1

# Rumus menghitung jarak Euclidean
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Rumus menghitung titik tengah
titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

# Menampilkan hasil perhitungan
print(f"\n === HASIL KALKULATOR KOORDINAT ===")
print(f"Titik A: ({x1:.2f}, {y1:.2f})")
print(f"Titik B: ({x2:.2f}, {y2:.2f})")
print(f"Perubahan koordinat (dx, dy): ({dx:.2f}, {dy:.2f})")
print(f"Jarak antara titik A dan B: {jarak:.2f}")
print(f"Titik tengah antara titik A dan B: ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")
