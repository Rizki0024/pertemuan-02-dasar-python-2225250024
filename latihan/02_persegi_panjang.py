# Menampilkan judul program
print("\n === PERHITUNGAN LUAS DAN KELILING PERSEGI PANJANG ===")

# Mengambil input dari pengguna
panjang = float(input("Masukkan Panjang persegi panjang: "))
lebar = float(input("Masukkan Lebar persegi panjang: "))

# Rumus menghitung luas dan keliling persegi panjang
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil perhitungan luas dan keliling persegi panjang dengan format 2 angka di belakang koma
print("\n === HASIL PERHITUNGAN LUAS DAN KELILING PERSEGI PANJANG ===")
print(f"Luas        : {luas:.2f}")
print(f"Keliling    : {keliling:.2f}")