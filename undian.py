import random

jumlah_pelanggan = int(input("Berapa pelanggan yang datang hari ini: "))

print("==== UNDIAN BERHADIAH TOKO RAME ====")
print(f"Jumlah pelanggan hari ini: {jumlah_pelanggan}")

print("\nNomor pelanggan yang menang: ")

pemenang = random.sample(range(1, jumlah_pelanggan + 1), 3)
for nomor in (pemenang):
    print(f"🎉 {nomor}")

print("Selamat kepada pemenang")
