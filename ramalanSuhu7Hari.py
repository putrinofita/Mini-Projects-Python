import random

suhu_list = []

for i in range(7):
    suhu = random.randint(20, 35)
    suhu_list.append(suhu)
    print(f"Hari ke-{i+1}: {suhu} derajat")

print("\nSemua suhu:", suhu_list)
print(f"Suhu tertinggi: {max(suhu_list)}°C")
print(f"Suhu terendah: {min(suhu_list)}°C")
print(f"Rata-rata suhu: {sum(suhu_list)/len(suhu_list):.1f}°C")