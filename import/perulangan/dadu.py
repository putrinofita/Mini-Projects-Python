import random

jumlah_dadu = int(input("Berapa kali dadu akan dilemparkan: "))
dadu_list = []

for i in range(jumlah_dadu):
    dadu = random.randint(1, 6)
    print(f"Dadu ke-{i+1}: {dadu}")
    dadu_list.append(dadu)

print("\nHasil lemparan:", dadu_list)
print(f"\nTotal nilai: {sum(dadu_list)}")
print(f"Suhu tertinggi: {max(dadu_list)}")
print(f"Suhu terendah: {min(dadu_list)}")
print(f"Rata-rata: {sum(dadu_list)/len(dadu_list)}")
# len berfungsi untuk menghitung jumlah elemen pada list