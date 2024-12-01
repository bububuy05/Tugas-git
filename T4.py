def cek_tekanan_darah(nama, sistolik, diastolik, denyut_nadi):
  print("Nama:", nama)
  
  if sistolik > 180 or diastolik > 120:
    print("Krisis hipertensi! Segera cari bantuan medis.")
  else:
    if sistolik > 140 or diastolik > 90:
      print("Konsultasikan dengan dokter mengenai hipertensi.")
    elif sistolik >= 120 and sistolik <= 139 or diastolik >= 80 and diastolik <= 89:
      print("Anda berada dalam kategori prehipertensi.")
    else:
      print("Tekanan darah Anda normal.")

    if denyut_nadi > 100:
      print("Periksa kondisi kesehatan jantung Anda.")
    elif denyut_nadi < 60:
      print("Periksa apakah ada gejala lain yang mengiringi bradikardia.")
    else:
      print("Denyut nadi Anda normal.")

for i in range(3):
  nama = input("Masukkan nama: ")
  sistolik = int(input("Masukkan tekanan darah sistolik (mmHg): "))
  diastolik = int(input("Masukkan tekanan darah diastolik (mmHg): "))
  denyut_nadi = int(input("Masukkan denyut nadi (bpm): "))
  
  cek_tekanan_darah(nama, sistolik, diastolik, denyut_nadi)
  