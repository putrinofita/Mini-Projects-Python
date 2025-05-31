import random

pesanan_list = []
hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
pesanan_diatas_rata = []

for hari in hari_list:
    pesanan = random.randint(30, 100)
    pesanan_list.append(pesanan)
    print(f"{hari}: {pesanan}")

ratarata = sum(pesanan_list) / len(pesanan_list)

for i in range(len(hari_list)):
    if pesanan_list[i] > ratarata:
        pesanan_diatas_rata.append(hari_list[i])

# Cari hari dengan pesanan terbanyak
index_max = pesanan_list.index(max(pesanan_list))
hari_terbanyak = hari_list[index_max]

# Output analisis
print(f"\nTotal pesanan minggu ini: {sum(pesanan_list)}")
print(f"Hari dengan pesanan terbanyak: {hari_terbanyak} ({max(pesanan_list)} Pesanan)")
print(f"Rata-rata pesanan per hari: {ratarata:.1f}")
print(f"Hari di atas rata-rata: {', '.join(pesanan_diatas_rata)}")