import random

print("-"*70)
print ("Selamat datang di layanan pendeteksi film yang sedang viral saat ini")
# list harga
film_a = 40_000
film_b = 35_000
film_c = 30_000

print("-"*70)

# Variabel list digunakan untuk variabel yang berisi lebih dari 1 data
hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
list_film = ["Film A", "Film B", "Film C"]

# variabel ini gunakan untuk menyimpan data yang dibuat oleh program dengan import random
# variabel ini dapat diumpamakan sebagi lemari dari data
list_pendapatan = []
# list_pendapatan = [] digunakan untuk menyimpan data berapa banyak pendapatan pertiket film yang terjual
tiketA = []
tiketB = []
tiketC = []
# tiketA = [], tiketB = [], tiketC = [] digunakan untuk menyimpan data jumlah tiket Film yang terjual

for hari in hari_list:
    print(f"\n==== Hari {hari} ====")
    # Film A
    tiket = random.randint(10, 100)
    # random.randint(10, 100) artinya program akan memilih angka secara random antara angka 10 sampai dengan 100
    tiketA.append(tiket)
    # tiketA adalah variabel atau lemari yang akan menjadi tujuan dimana kita akan meletakkan data
    # dan .append lah yang digunakan untuk mengarahkan data ke variabel yang telah disiapkan agar disimpan
    # perumpamannya seperti ketika kita mau meletakkan data di lemari, nahh langkah yang kita lakukan itu sama seperti yang .append lakukan
    # lalu (tiket) adalah data yang akan kita simpan

    # just info: nama variabel dapat diubah sesuai dengan yang kita butuhkan, dan yang tidak bisa berubah itu .append
    
    total_filmA = film_a * tiket
    # total_filmA yang artinya total pendapatan dari film A berguna untuk mempermudah dalam menghitung total pendapatan keseluruhan yang di peroleh
    list_pendapatan.append(total_filmA)
    # list_pendapatan.append(total_filmA) digunakan untuk menyimpan data total_filmA ke varibel list_pendapatan
    print (f"Film A: {tiket} tiket ")


    # Film B
    tiket = random.randint(10, 100)
    tiketB.append(tiket)

    total_filmB = film_b * tiket
    list_pendapatan.append(total_filmB)
    print (f"Film B: {tiket} tiket ")

    # Film C
    tiket = random.randint(10, 100)
    tiketC.append(tiket)

    total_filmC = film_c * tiket
    list_pendapatan.append(total_filmC)
    print (f"Film C: {tiket} tiket ")

print("-"*70)

# sum berguna untuk menghitung semua data (int) yang ada di dalam variabel list 
# :, yang ada di variabel berguna untuk mempermudah pembacaan ribuan di akhir
print (f"Total tiket film A: {sum(tiketA)} tiket (Rp{total_filmA:,})")
print (f"Total tiket film B: {sum(tiketB)} tiket (Rp{total_filmB:,})")
print (f"Total tiket film C: {sum(tiketC)} tiket (Rp{total_filmC:,})")

print("-"*70)

# Pengingat: list_pendapatan berisi tentang semua pendapatan dari hasil tiket yang terjual
total = sum(list_pendapatan)
print (f"Total pendapatan minggu ini: Rp{total:,}")

total_list = [sum(tiketA), sum(tiketB), sum(tiketC)]
# total_list untuk menyimpan data penjualan seluruh tiket tapi tiket film A, film B, film C tetap terpisah
max_index = total_list.index(max(total_list))
# max_index dibuat untuk mencari posisi dari film yang memiliki penjualan tiket tertinggi
# dengan rincian:
# max(total_list) untuk mengambil nilai tertinggi yang ada di variabel total_list
# total_list.index() digunakan untuk mencari di urutan keberapa nilai tertinggi berada di total list

# kesimpulan:
# max_index berguna untuk mencari / menganalisis dimana nilai yang paling tinggi beda
film_terlaris = list_film[max_index]
# jadi max_index sangat berguna untuk bagian ini, misal max indexnya ada di posisi 2 
# maka variabel film_terlaris akan mencari data apa yang ada di list_film dengan posisi yang sama
print (f"Film dengan penjualan tertinggi: {film_terlaris} dengan penjualan tiket sebanyak {total_list[max_index]} tiket")

max_tiketA = max(tiketA)
hari_index = hari_list[tiketA.index(max(tiketA))]
print(f"Hari terbaik untuk penjualan tiket film A: {hari_index} dengan penjualan tiket sebanyak ({max_tiketA}) tiket")
print("-"*70)