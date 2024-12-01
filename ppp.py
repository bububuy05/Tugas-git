def catat_data_pasien():
    """Fungsi untuk mencatat data pasien dan menganalisis tekanan darah."""

    # Meminta input jumlah pasien
    jumlah_pasien = int(input("Masukkan jumlah pasien: "))

    # Membuat list kosong untuk menyimpan data
    nama_pasien = []
    tekanan_sistolik = []
    tekanan_diastolik = []

    # Melakukan input data untuk setiap pasien
    for i in range(jumlah_pasien):
        nama = input(f"Masukkan nama pasien ke-{i+1}: ")
        sistolik = int(input(f"Masukkan tekanan darah sistolik pasien ke-{i+1}: "))
        diastolik = int(input(f"Masukkan tekanan darah diastolik pasien ke-{i+1}: "))

        nama_pasien.append(nama)
        tekanan_sistolik.append(sistolik)
        tekanan_diastolik.append(diastolik)

    # Menghitung rata-rata
    rata_sistolik = sum(tekanan_sistolik) / jumlah_pasien
    rata_diastolik = sum(tekanan_diastolik) / jumlah_pasien

    # Menampilkan hasil
    print("\nRata-rata tekanan darah:")
    print(f"Sistolik: {rata_sistolik:.2f}")
    print(f"Diastolik: {rata_diastolik:.2f}")

    print("\nPasien dengan hipertensi:")
    for i in range(jumlah_pasien):
        if tekanan_sistolik[i] > 140 or tekanan_diastolik[i] > 90:
            print(nama_pasien[i])

# Memanggil fungsi utama
catat_data_pasien()