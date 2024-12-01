def hitung_biaya_laundry():
  jenis_pakaian = input("Masukkan jenis pakaian: ")
  berat_pakaian = float(input("Masukkan berat pakaian (kg): "))
  harga_per_kg = float(input("Masukkan harga per kilogram: "))

  total_biaya = berat_pakaian * harga_per_kg

  print("\nRincian Pesanan:")
  print("Jenis Pakaian:", jenis_pakaian)
  print("Berat Pakaian:", berat_pakaian, "kg")
  print("Harga per Kilogram:", harga_per_kg)
  print("Total Biaya:", total_biaya)

hitung_biaya_laundry()