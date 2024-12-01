def hitung_total_harga(kategori_film, jumlah_tiket, anggota_vip):
    # Harga dasar tiket
    harga = 0
    match kategori_film:
        case 'A':
            harga = 50000
        case 'B':
            harga = 75000
        case 'C':
            harga = 100000
        case _:
            print("Kategori film tidak valid!")
            return 0

    # Menghitung total harga sebelum diskon
    total_harga = harga * jumlah_tiket

    # Diskon untuk anggota VIP
    if anggota_vip:
        total_harga *= 0.8  # Diskon 20%

    # Diskon tambahan untuk pembelian lebih dari 5 tiket
    if jumlah_tiket > 5:
        total_harga *= 0.9  # Diskon tambahan 10%

    return total_harga


# Input dari pengguna
kategori_film = input("Pilih kategori film (A, B, C): ").strip().upper()
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
anggota_vip = input("Apakah Anda anggota VIP? (ya/tidak): ").strip().lower() == 'ya'

# Hitung total harga
total_harga = hitung_total_harga(kategori_film, jumlah_tiket, anggota_vip)

# Tampilkan total harga
if total_harga > 0:
    print(f"Total harga yang harus dibayar: Rp {total_harga:.2f}")
