angka_rahasia = 8

nama = input("Masukkan nama anda: ")
angka = int(input("Masukkan angka tebakan anda: "))

if angka > angka_rahasia :
    print ("Angka tebakan anda lebih besar dari angka rahasia")
elif angka < angka_rahasia :
    print ("Angka tebakan anda lebih kecil dari angka rahasia")
else :
    print ("Selamat ", nama, ", angka tebakan anda benar")