# Note: Bobot penilaian
bobot_tugas = 0.2 # 20%
bobot_uts = 0.3 # 30%
bobot_uas = 0.5 # 50%

# Menampilkan judul program
print("\n === PERHITUNGAN NILAI AKHIR ===")

# Mengambil input dari pengguna 
nama = input("Masukkan nama Anda: ")
nilai_tugas = float(input("Masukkan nilai tugas Anda: "))
nilai_uts = float(input("Masukkan nilai UTS Anda: "))
nilai_uas = float(input("Masukkan nilai UAS Anda: "))

# Rumus menghitung nilai akhir
nilai_akhir = (bobot_tugas * nilai_tugas) + (bobot_uts * nilai_uts) + (bobot_uas * nilai_uas)

# Menampilkan hasil perhitungan nilai akhir
print(f"\n === HASIL PERHITUNGAN NILAI AKHIR ===")
print(f"Nama: {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")