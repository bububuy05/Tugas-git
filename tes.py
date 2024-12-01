# Soal
# Anda bekerja sebagai pengembang perangkat lunak di sebuah klinik kesehatan yang ingin 
# membuat aplikasi sederhana untuk mencatat data 
# pasien dan menganalisis tekanan darah. Tugas Anda adalah membuat program yang dapat melakukan hal berikut:
# 1. Meminta pengguna untuk memasukkan jumlah pasien yang akan didaftarkan.
# 2. Untuk setiap pasien, minta pengguna memasukkan nama, tekanan darah sistolik, dan tekanan darah diastolik.
# 3. Simpan data setiap pasien dalam tiga list terpisah, satu untuk nama, satu untuk tekanan darah 
# sistolik, dan satu untuk tekanan darah diastolik.
# 4. Hitung dan tampilkan rata-rata tekanan darah sistolik dan diastolik dari semua pasien.
# 5. Tampilkan nama-nama pasien yang memiliki tekanan darah sistolik di atas 140 atau tekanan darah 
# diastolik di atas 90, yang menandakan hipertensi.
def data_pasien():
  #input jumlah pasien
  jumlah_pasien = int(input("Masukkan jumlah pasien: "))
  #list kosong untuk menyimpan data
  nama_pasien = []
  sistolik = []
  diastolik = []
  #input data untuk setiap pasien
  for i in range(jumlah_pasien):
    nama = input(f"Masukkan nama pasien ke-{i+1}: ")
    sistole = int(input("Masukan tekanan darah sistolik: "))
    diastole = int(input("Masukkan tekanan darah diastolik: "))

    nama_pasien.append(nama) #Jadi, data nama pasien akan ditambahkan ke dalam list.
    sistolik.append(sistole) #sebuah fungsi yang digunakan untuk menambahkan elemen ke list.
    diastolik.append(diastole)

  #rata-rata
  rata_sistolik = sum(sistolik) / jumlah_pasien #sum()fungsi digunakan untuk menjumlahkan elemen dalam sebuah list.
  rata_diastolik = sum(diastolik) / jumlah_pasien #

  print("Rata-rata sistolik:", rata_sistolik)
  print("Rata-rata diastolik:", rata_diastolik)
  print("Pasien hipertensi:")

# Memanggil fungsi
data_pasien()