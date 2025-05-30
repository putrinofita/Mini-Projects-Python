# Rina ingin menabung hingga mengumpulkan Rp100.000. Ia mulai menabung Rp2.000 di hari pertama, dan setiap hari jumlah tabungannya bertambah Rp1.000 dari hari sebelumnya.
# Tugas:
# Buat program Python dengan perulangan untuk:
# Menampilkan jumlah tabungan per hari
# Menampilkan total tabungan dan hari ke berapa Rina mencapai target
# Contoh Output:
# Hari ke-1: Rp2000
# Hari ke-2: Rp3000
# ...
# Target tercapai di hari ke-14 dengan total Rp100000

hari = 0
tabungan_harian = 2000
total_tabungan = 0


while total_tabungan < 100_000:
    hari += 1
    total_tabungan += tabungan_harian

    print (f"Hari k-{hari}: Rp{tabungan_harian:,} (total: Rp{total_tabungan})")
    tabungan_harian += 1000

print (f"Target tercapai di hari ke-{hari} dengan total tabungan Rp{total_tabungan:,}")