# Sebuah HP memiliki baterai yang saat ini berada di 10%. Setiap 1 menit, baterai bertambah 5% saat diisi daya. HP akan dianggap penuh jika baterainya mencapai 100%.
# Tugas:
# Buat program Python menggunakan perulangan untuk menampilkan:
# Proses pengisian baterai tiap menit
# Berapa menit yang dibutuhkan hingga baterai penuh

# contoh output:
# Menit ke-1: Baterai 15%
# Menit ke-2: Baterai 20%
# ...
# Baterai penuh dalam 18 menit!

baterai = 10
menit = 0

while baterai < 100:
    menit += 1
    baterai += 5
    print (f"Menit Ke-{menit}, baterai {baterai}%")

print (f"Baterai penuh dalam {menit} menit")