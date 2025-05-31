import random

jumlah_kuesioner = int(input("Berapa kali kuesioner akan dilakukan: "))
kuesioner_list = []

for i in range(jumlah_kuesioner):
    kuesioner = random.randint(1, 4)
    print(f"Kuesioner ke-{i+1}: {kuesioner}")
    kuesioner_list.append(kuesioner)

print("\nHasil kuesioner:", kuesioner_list)
print(f"\nTotal nilai: {sum(kuesioner_list)}")
print(f"Suhu tertinggi: {max(kuesioner_list)}")
print(f"Suhu terendah: {min(kuesioner_list)}")
print(f"Rata-rata: {sum(kuesioner_list)/len(kuesioner_list)}")
