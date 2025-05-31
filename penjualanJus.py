import random

hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
jus_list = ["Jus Apel", "Jus Mangga", "Jus Semangka"]

apel = []
mangga = []
semangka = []

# Simulasi penjualan setiap hari
for hari in hari_list:
    print(f"\n==== Hari {hari} ====")

    penjualan_apel = random.randint(20, 100)
    apel.append(penjualan_apel)
    print(f"Jus Apel: {penjualan_apel}")

    penjualan_mangga = random.randint(20, 100)
    mangga.append(penjualan_mangga)
    print(f"Jus Mangga: {penjualan_mangga}")

    penjualan_semangka = random.randint(20, 100)
    semangka.append(penjualan_semangka)
    print(f"Jus Semangka: {penjualan_semangka}")

# Total dan rata-rata
total_apel = sum(apel)
total_mangga = sum(mangga)
total_semangka = sum(semangka)

rata_apel = total_apel / len(hari_list)
rata_mangga = total_mangga / len(hari_list)
rata_semangka = total_semangka / len(hari_list)

print("\n=== Laporan Mingguan ===")
print(f"Total Jus Apel: {total_apel} (Rata-rata: {rata_apel:.1f})")
print(f"Total Jus Mangga: {total_mangga} (Rata-rata: {rata_mangga:.1f})")
print(f"Total Jus Semangka: {total_semangka} (Rata-rata: {rata_semangka:.1f})")

# Mencari jus terlaris
total_list = [total_apel, total_mangga, total_semangka]
max_index = total_list.index(max(total_list))
jus_terlaris = jus_list[max_index]
print(f"\nJus terlaris minggu ini: {jus_terlaris} ({max(total_list)} penjualan)")

# Hari penjualan terbanyak untuk Jus Semangka
max_semangka = max(semangka)
hari_terlaris_semangka = hari_list[semangka.index(max_semangka)]
print(f"Hari terbaik untuk Jus Semangka: {hari_terlaris_semangka} ({max_semangka} penjualan)")
