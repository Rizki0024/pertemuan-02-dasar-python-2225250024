# Note : Konstanta untuk konversi suhu
KELVIN_OFFSET = 273.15

# Menampilkan judul program
print("\n === KONVERSI SUHU ===")

# Mengambil input dari pengguna
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Rumus konversi suhu
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

# Menampilkan hasil konversi suhu dengan format 2 angka di belakang koma
print("\n === HASIL KONVERSI SUHU ===")
print(f"Celsius : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin : {kelvin:.2f} K")
