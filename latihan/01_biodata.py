# Note: Tahun saat ini
tahun_sekarang = 2026

# Menampilkan judul program
print("\n === BIODATA ANDA ===")

# Mengambil input dari pengguna
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
kelas = input("Masukkan kelas Anda: ")
tahun_lahir = int(input("Masukkan tahun Lahir Anda: "))

# Menghitung umur berdasarkan tahun lahir
umur = tahun_sekarang - tahun_lahir

# Menampilkan biodata pengguna
print("\n === HASIL BIODATA ANDA ===")
print(f"Nama        : {nama}")
print(f"NIM         : {nim}")
print(f"Kelas       : {kelas}")
print(f"Tahun Lahir : {tahun_lahir}")
print(f"Umur        : sekitar {umur} tahun")  # mengapa umur disebut perkiraan? karena umur yang dihitung hanya berdasarkan tahun lahir saja, tanpa memperhitungkan bulan dan tanggal lahir. Jadi, umur yang dihitung bisa lebih atau kurang dari umur sebenarnya.
