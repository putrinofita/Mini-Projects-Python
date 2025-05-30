# Andi mendaki gunung setinggi 3000 meter. Setiap jam, ia bisa naik 400 meter. Tapi setiap malam (setelah 1 hari, yaitu setiap 6 jam), ia turun kembali 200 meter karena kelelahan.
# Tugas:
# Buat program Python menggunakan perulangan untuk menghitung:
# Ketinggian Andi setelah setiap jam
# Berapa jam yang dibutuhkan hingga mencapai atau melewati puncak

# contoh output:
# Jam ke-1: 400 meter
# ...
# Jam ke-6: 2400 meter (turun 200 meter, jadi 2200 meter)
# ...
# Andi mencapai puncak dalam XX jam

tinggiGunung = 0
jam = 0

while tinggiGunung < 3000:
    jam += 1
    tinggiGunung += 400
    print (f"Jam ke-{jam}: {tinggiGunung} Meter")

    if jam % 6 == 0:
        tinggiGunung -= 200
        print (f"Jam ke-{jam}: {tinggiGunung} Meter (turun 200 meter, jadi {tinggiGunung} Meter)")

print (f"Andi mencapai puncak dalam {jam} jam")