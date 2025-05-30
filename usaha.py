# Alya membuka usaha menjual jus buah di depan rumahnya. Ia ingin menyusun rencana usaha harian:
# Ia mulai dengan modal awal yang ditentukan oleh pengguna (input).

# Setiap hari:
# Ia membeli bahan baku seharga Rp10.000
# Ia menjual sebanyak jumlah gelas yang ditentukan oleh pengguna (input per hari)
# Harga jual per gelas: Rp5.000
# Setiap malam, ia menghitung:
# Keuntungan kotor hari itu = jumlah gelas × Rp5.000
# Keuntungan bersih = keuntungan kotor – biaya bahan baku
# Modal ditambah keuntungan bersih
# Usaha terus berjalan hingga modal mencapai atau melebihi Rp100.000.

# Tugas:
# Buat program Python yang:
# Meminta pengguna memasukkan:
# Modal awal Alya
# Setiap hari:
# Meminta pengguna memasukkan jumlah gelas jus yang terjual
# Menampilkan:
# Rincian keuntungan harian
# Total modal saat ini
# Menampilkan hari ke berapa modal mencapai Rp100.000

# 💡 Contoh Output:
# Masukkan modal awal: 30000

# === Hari ke-1 ===
# Jual berapa gelas hari ini? 5
# Pendapatan kotor: Rp25000
# Keuntungan bersih: Rp15000
# Modal sekarang: Rp45000

# === Hari ke-2 ===
# Jual berapa gelas hari ini? 4
# Pendapatan kotor: Rp20000
# Keuntungan bersih: Rp10000
# Modal sekarang: Rp55000

# ...
# Target tercapai di hari ke-6 dengan modal Rp100000

modal = int(input("Masukkan modal awal: "))
bahanBaku = 10_000
hari = 0

while modal < 100_000:
    hari += 1
    print (f"==== HARI KE-{hari} ====")
    jual = int(input("Jual berapa gelas hari ini: "))
    pendapatanKotor = jual * 5_000
    print (f"Pendapatan Kotor: Rp{pendapatanKotor:,}")
    pendapatanBersih = pendapatanKotor - bahanBaku
    print (f"Pendapatan Bersih: Rp{pendapatanBersih:,}")
    modal = modal + pendapatanBersih
    print (f"Modal saat ini: Rp{modal:,}")

print (f"Target tercapai di hari ke-{hari} dengan modal Rp{modal}")