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

print ("-"*50)
for i in range(7) :
    print(f"============ Hari {i+1} ============")
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
    print ("\n")

print ("-"*50)

total = sum(pendapatan_VIP) + sum(pendapatan_reguler) + sum(pendapatan_ekonomi)
print (f"Total pemasukan selama 7 hari dari semua jenis tiket adalah Rp{total:,}")

total_list = [sum(tiket_VIP), sum(tiket_ekonomi), sum(tiket_reguler)]
max_index = total_list.index(max(total_list))
tiket_trend = list_tiket[max_index]

print (f"Jenis tiket yang paling banyak terjual adalah {tiket_trend} dengan penjualan tiket sebanyak {total_list[max_index]}")
print ("-"*50)


# kontribusi dihitung dari pendapatan paling banyak
print("Kontribusi:")
kontribusi_VIP = (sum(pendapatan_VIP)/total) * 100
print (f"- VIP: {kontribusi_VIP:.1f}%")

kontribusi_reguler = (sum(pendapatan_reguler)/total) * 100
print (f"- Reguler: {kontribusi_reguler:.1f}%")

kontribusi_ekonomi = (sum(pendapatan_ekonomi)/total) * 100
print (f"- Ekonomi: {kontribusi_ekonomi:.1f}%")

print ("-"*50)
kontribusi_tertinggi = [kontribusi_VIP, kontribusi_reguler, kontribusi_ekonomi]
max_index = kontribusi_tertinggi.index(max(kontribusi_tertinggi))
tiket_trend = list_tiket[max_index]
print(f"Tiket dengan kontribusi tertinggi: {tiket_trend} ({kontribusi_tertinggi[max_index]:.1f}%)")