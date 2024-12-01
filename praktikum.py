print("Pilih Barang:")
print("1. Barang A (Rp. 200.000)")
print("2. Barang B (Rp. 500.000)")
print("3. Barang C (Rp. 1.000.000)")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
   no1 = input("masukan jumlah barang yang ingin dibeli: ")
   print("hasil 1 ") 
elif pilihan == "2":
   no2 = input("masukan jumlah barang yang ingin dibeli: ")
   print("hasil 2 ")
elif pilihan == "3":
   no3 = input("masukan jumlah barang yang ingin dibeli: ")
   print("hasil 3 ") 

else:
    print("pilihan anda tidak bisa")