def konversi_suhu():
  """Fungsi untuk mengkonversi suhu antara Celcius, Reamur, Fahrenheit, dan Kelvin."""

  # Input suhu awal dan satuannya
  suhu_awal = float(input("Masukkan suhu awal: "))
  satuan_awal = input("Ketik c untuk Celcius, r untuk Reamur, f untuk Fahrenheit, k untuk Kelvin: ")

  # Input satuan tujuan
  satuan_tujuan = input("Ketik c untuk Celcius, r untuk Reamur, f untuk Fahrenheit, k untuk Kelvin: ")

  # Konversi suhu
  if satuan_awal == 'c':
    if satuan_tujuan == 'r':
      hasil = suhu_awal * 4 / 5
    elif satuan_tujuan == 'f':
      hasil = (suhu_awal * 9/5) + 32
    elif satuan_tujuan == 'k':
      hasil = suhu_awal + 273.15
    else:
      hasil = suhu_awal
  elif satuan_awal == 'r':
    if satuan_tujuan == 'c':
      hasil = suhu_awal * 5 / 4
    elif satuan_tujuan == 'f':
      hasil = (suhu_awal * 9/4) + 32
    elif satuan_tujuan == 'k':
      hasil = (suhu_awal * 5/4) + 273.15
    else:
      hasil = suhu_awal
  elif satuan_awal == 'f':
    if satuan_tujuan == 'c':
      hasil = (suhu_awal - 32) * 5/9
    elif satuan_tujuan == 'r':
      hasil = (suhu_awal - 32) * 4/9
    elif satuan_tujuan == 'k':
      hasil = (suhu_awal + 459.67) * 5/9
    else:
      hasil = suhu_awal
  elif satuan_awal == 'k':
    if satuan_tujuan == 'c':
      hasil = suhu_awal - 273.15
    elif satuan_tujuan == 'r':
      hasil = (suhu_awal - 273.15) * 4/5
    elif satuan_tujuan == 'f':
      hasil = (suhu_awal * 9/5) - 459.67
    else:
      hasil = suhu_awal
  else:
    print("Satuan yang Anda masukkan salah.")
    return

  # Cetak hasil konversi
  print("Suhu yang diinputkan adalah", suhu_awal, "derajat", satuan_awal)
  print("Hasil konversi ke", satuan_tujuan, "adalah", hasil, "derajat", satuan_tujuan)

konversi_suhu()
# Panggil fungsi konversi_suhu