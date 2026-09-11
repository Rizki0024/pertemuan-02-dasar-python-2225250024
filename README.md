# Pertemuan 02: Dasar Python di VS Code dan Pengumpulan melalui GitHub

## Identitas Mahasiswa
- **Nama**: Rizki Ramadan
- **NIM**: 2225250024
- **Kelas**: 3F
- **Mata Kuliah**: Algoritma dan Pemrograman
- **Program Studi**: S1 Pendidikan Matematika, FKIP, Universitas Sultan Ageng Tirtayasa
- **Dosen Pengampu**: Dr. Aan Hendrayana, S.Si., M.Pd.

---

## Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas mata kuliah Algoritma dan Pemrograman Pertemuan ke-2. Repositori ini memuat implementasi dasar bahasa pemrograman Python (variabel, tipe data, input-output, operator aritmetika), pengujian program, serta perekaman proses kerja menggunakan Git dan GitHub.

---

## Struktur dan Daftar Berkas
```text
pertemuan-02-dasar-python-[NIM]/
├── .gitignore
├── README.md
├── latihan/
│   ├── 01_biodata.py
│   ├── 02_persegi_panjang.py
│   ├── 03_konversi_suhu.py
│   └── 04_nilai_akhir.py
└── tugas/
    └── kalkulator_koordinat.py

**Deskripsi Berkas:**
1. latihan/01_biodata.py: Program untuk menerima input data diri (nama, NIM, kelas, tahun lahir) dan menampilkan kartu biodata beserta perkiraan umur menggunakan konstanta tahun berjalan.
2. latihan/02_persegi_panjang.py: Program untuk menghitung luas dan keliling persegi panjang dari input panjang dan lebar bertipe pecahan (float).
3. latihan/03_konversi_suhu.py: Program untuk mengonversi nilai suhu dari derajat Celsius ke Fahrenheit dan Kelvin.
4. latihan/04_nilai_akhir.py: Program untuk menghitung nilai akhir mahasiswa berdasarkan bobot persentase tugas (20%), UTS (30%), dan UAS (50%).
5. tugas/kalkulator_koordinat.py: Program utama (Kuis 1) untuk menghitung perubahan koordinat (dx, dy), jarak Euclidean antara dua titik, serta titik tengah dua titik dalam bidang Kartesius.

---

## Cara Menjalankan Program
- Pastikan Python 3 telah terpasang di sistem dan terminal berada pada direktori utama proyek.
- Jalankan program melalui terminal dengan perintah berikut:
- Menjalankan Tugas Utama:
python tugas/kalkulator_koordinat.py (Gunakan python3 jika menggunakan sistem operasi macOS atau Linux)
- Menjalankan Berkas Latihan:
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py
python latihan/04_nilai_akhir.py

---

## Hasil Pengujian Tugas Utama (Test Case Wajib)
Pengujian pada program tugas/kalkulator_koordinat.py dilakukan terhadap 3 kasus uji (test case) yang ditetapkan pada modul:

| Kasus |  Titik A  | Titik B  |    Nilai dx & dy     | Jarak | Titik Tengah | Status |
|-------|-----------|----------|----------------------|-------|--------------|--------|
|   1   |  (0, 0)   |  (3, 4)  | dx = 3.00, dy = 4.00 | 5.00  | (1.50, 2.00) | Sesuai |
|   2   |  (-2, 1)  |  (4, 1)  | dx = 6.00, dy = 0.00 | 6.00  | (1.00, 1.00) | Sesuai |
|   3   | (2.5, -1) | (2.5, 3) | dx = 0.00, dy = 4.00 | 4.00  | (2.50, 1.00) | Sesuai |

---

## Refleksi
- Konsep yang paling saya pahami adalah...
Konsep yang paling saya pahami adalah penggunaan variabel, input, konversi tipe data, dan operator aritmatika dalam Python. Saya mulai memahami bahwa data yang dimasukkan melalui input() perlu dikonversi terlebih dahulu menjadi int atau float apabila akan digunakan dalam perhitungan.
- Kesalahan yang saya temukan adalah...
Kesalahan yang saya temukan selamma mengerjakan latihan adalah kesalahan dalam memahami tipe data dan penulisan rumus. Saya memperbaikinya dengan membaca kembali materi, memeriksa kode, menjalankan program, dan membandingkan hasil program dengan perhitungan secara manual.
- Pada pertemuan berikutnya saya ingin lebih memahami...
Pada pertemuan berikutnya saya ingin lebih memahami cara membuat program yang lebih terstruktur dan memahami konsep pemrograman berikutnya secara bertahap agar dapat menyelesaikan masalah dengan kode Python yang lebih baik.

---

Sumber
1. Materi pertemuan 02 - Dasar Python, Algoritma dan Pemrograman, Universitas Sultan Ageng Tirtayasa.
2. ChatGPT, digunakan sebagai bantuan belajar dan pemecahan masalah dalam memahami materi, menyusun kode, dan mengecek hasil program

Tools yang digunakan
- Python
- Visual Studio Code
- Git
- GitHub
- ChatGPT