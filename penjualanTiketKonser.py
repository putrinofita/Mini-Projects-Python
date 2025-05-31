import random

# list harga
VIP = 150_000
reguler = 100_000
ekonomi = 70_000
list_tiket = ["Tiket VIP", "Tiket Reguler", "Tiket Ekonomi"]
tiket_VIP = []
tiket_reguler = []
tiket_ekonomi = []
pendapatan_VIP = []
pendapatan_reguler = []
pendapatan_ekonomi = []

for i in range(5) :
    print(f"\n===== Hari {i+1} =====")
    tiket = random.randint(20, 120)
    tiket_VIP.append(tiket)
    print(f"Tiket VIP terjual sebanyak: {tiket}")
    pendapatan = tiket * VIP
    pendapatan_VIP.append (pendapatan)

    tiket = random.randint(20, 120)
    tiket_reguler.append(tiket)
    print(f"Tiket reguler terjual sebanyak: {tiket}")
    pendapatan = tiket * reguler
    pendapatan_reguler.append (pendapatan)

    tiket = random.randint(20, 120)
    tiket_ekonomi.append(tiket)
    print(f"Tiket ekonomi terjual sebanyak: {tiket}")
    pendapatan = tiket * ekonomi
    pendapatan_ekonomi.append (pendapatan)

total = sum(pendapatan_VIP) + sum(pendapatan_reguler) + sum(pendapatan_ekonomi)
print (f"\nTotal pemasukan selama 5 hari dari semua jenis tiket adalah Rp{total:,}")

total_list = [sum(tiket_VIP), sum(tiket_ekonomi), sum(tiket_reguler)]
max_index = total_list.index(max(total_list))
tiket_trend = list_tiket[max_index]

print (f"Jenis tiket yang paling banyak terjual adalah {tiket_trend} dengan penjualan tiket sebanyak {total_list[max_index]}")