print("Pilih mau apa:")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("4. Pembagian")
pilih = input()

if pilih == "1":
   no1 = input("masukan no pertama: ")
   no2 = input("masukan no kedua: ")
   print("hasil " + str(int(no1) + int(no2))) 
elif pilih == "2":
   no1 = input("masukan no pertama: ")
   no2 = input("masukan no kedua: ")
   print("hasil " + str(int(no1) - int(no2)))
elif pilih == "3":
   no1 = input("masukan no pertama: ")
   no2 = input("masukan no kedua: ")
   print("hasil " + str(int(no1) * int(no2))) 
elif pilih == "4":
   no1 = input("masukan no pertama: ")
   no2 = input("masukan no kedua: ")
   print("hasil " + str(int(no1) / int(no2))) 
else:
    print("pilihan anda tidak bisa")