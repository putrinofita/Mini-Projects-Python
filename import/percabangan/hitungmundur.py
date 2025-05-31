from datetime import datetime

# Ambil tanggal hari ini
hari_ini = datetime.now()

# Input dari user
tanggal = int(input("Tanggal ulang tahun (DD): "))
bulan = int(input("Bulan ulang tahun (MM): "))

# Buat tanggal ulang tahun di tahun ini
tahun_sekarang = hari_ini.year
ulang_tahun = datetime(tahun_sekarang, bulan, tanggal)

# Jika ulang tahun sudah lewat tahun ini, pakai tahun depan
if ulang_tahun < hari_ini:
    ulang_tahun = datetime(tahun_sekarang + 1, bulan, tanggal)

# Hitung selisih hari
selisih = (ulang_tahun - hari_ini).days

print(f"Ulang tahunmu masih {selisih} hari lagi!")