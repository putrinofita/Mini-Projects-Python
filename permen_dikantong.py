# Seorang anak memiliki 50 permen dan membagikannya kepada teman-temannya satu per satu. Setiap detik ia memberikan 1 permen.
# Tugas:
# Buat program Python dengan perulangan untuk menampilkan:
# Jumlah permen yang tersisa setiap detik.
# Berhenti ketika semua permen habis.

# Contoh Output:
# Permen tersisa: 49
# Permen tersisa: 48
# ...
# Permen habis!

total_permen = 50
detik = 0

while total_permen > 0:
    print(f"Permen tersisa: {total_permen}")
    total_permen -= 1
    detik += 1

print (f"Permen habis dalam {detik} detik")