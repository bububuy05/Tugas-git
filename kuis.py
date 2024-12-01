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

def tulis_data_pasien(): #Fungsi untuk mencatat data pasien.

    #input pasien
    jumlah_pasien = int(input("Masukkan jumlah pasien: "))

    #untuk menyimpan data
    nama_pasien = []
    sistolik = []
    diastolik = []

    # Melakukan input data untuk setiap pasien
    for i in range(jumlah_pasien):
        nama = input(f"Masukkan nama pasien ke-{i+1}: ")
        sistolik = int(input(f"Masukkan tekanan darah sistolik pasien ke-{i+1}: "))
        diastolik = int(input(f"Masukkan tekanan darah diastolik pasien ke-{i+1}: "))

        nama_pasien.append(nama)
        tekanan_sistolik.append(sistolik)
        tekanan_diastolik.append(diastolik)

tulis_data_pasien()