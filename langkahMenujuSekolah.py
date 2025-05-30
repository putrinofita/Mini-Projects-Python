# Jarak dari rumah Lina ke sekolah adalah 100 meter. Setiap langkah Lina menempuh 2 meter. Buat program yang menghitung berapa langkah yang diperlukan untuk sampai di sekolah, dan tampilkan setiap langkahnya.
# Tugas:
# Gunakan perulangan untuk menampilkan setiap langkah hingga Lina mencapai atau melebihi 100 meter.

# Contoh Output:
# Langkah ke-1: 2 meter
# Langkah ke-2: 4 meter
# ...
# Lina sampai di sekolah dalam 50 langkah.

jarak = 100
langkah = 0
jarak_tempuh = 0

while jarak_tempuh < jarak:
    langkah += 1
    jarak_tempuh += 2
    print(f"Langkah ke-{langkah}: {jarak_tempuh} meter")

print (f"Lina sampai di sekolah dalam {langkah} langkah.")