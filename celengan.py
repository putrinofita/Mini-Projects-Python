# Menabung di Celengan
# Doni ingin menabung uang di celengan setiap minggu. Ia berencana menabung selama 10 minggu. Setiap minggunya, jumlah uang yang ditabung bertambah Rp5.000 dari minggu sebelumnya. Di minggu pertama, ia menabung Rp10.000.
# Tugas:
# Buat program Python yang menggunakan perulangan untuk menghitung:
# Jumlah uang yang ditabung Doni setiap minggu.
# Total tabungan Doni setelah 10 minggu.

# output:
# Minggu 1: Rp10000
# Minggu 2: Rp15000
# ...
# Total tabungan setelah 10 minggu: Rp???

print ("Selamat datang di layanan untuk menghitung rencana tabungan anda")
print ("-" * 60)

minggu1 = 10_000
total_minggu = 10
total_tabungan = 0

for minggu in range (1, total_minggu + 1):
    print (f"Minggu {minggu}: Rp{minggu1:,}")
    total_tabungan += minggu1
    minggu1 += 5_000

print ("-" * 60)
print (f"Total tabungan setelah {total_minggu} minggu: Rp{total_tabungan:,}")