import random

hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
es_jeruk = []
es_teh = []
es_kopi = []

for hari in hari_list:
    print(f"\n==== Hari {hari} ===")
    
    jeruk = random.randint(20, 80)
    kopi = random.randint(20, 80)
    teh = random.randint(20, 80)
    
    es_jeruk.append(jeruk)
    es_kopi.append(kopi)
    es_teh.append(teh)
    
    print(f"Es Jeruk: {jeruk}")
    print(f"Es Kopi : {kopi}")
    print(f"Es Teh  : {teh}")

# Total penjualan mingguan
total_es_jeruk = sum(es_jeruk)
total_es_kopi = sum(es_kopi)
total_es_teh = sum(es_teh)

# Simpan total dalam list
total = [total_es_jeruk, total_es_kopi, total_es_teh]
minuman = ["Es Jeruk", "Es Kopi", "Es Teh"]

# Cari minuman terlaris
terlaris_index = total.index(max(total))

print("\n=== Laporan Penjualan Mingguan ===")
print(f"Total Es Jeruk: {total_es_jeruk}")
print(f"Total Es Kopi : {total_es_kopi}")
print(f"Total Es Teh  : {total_es_teh}")
print(f"\nMinuman terlaris: {minuman[terlaris_index]} ({max(total)} penjualan)")