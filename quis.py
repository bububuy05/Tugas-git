#input data
#minta pengguna untuk memasukan jumlah pasien
#untuk setiap pasien,minta pengguna memasukan nama dan suhu tubuh
#Penggunaan list
#simpan nama pasien dalam list
#simpan suhu tubuh dalam list dengan tipe data float

#analisis data:
#hitung rata-rata suhu tubuh semua pasien
#identifikasi pasien yang suhunya di atas ambang batas

#output
#Ambang batas suhu adalah 45 derajat celcius
#cetak suhu tubuh
#cetak daftar pasien yang memiliki tekanan suhu di atas ambang batas

def analisis_data/suhu():

# Ambang batas suhu
    ambang_batas = 45.0
    # untuk menyimpan nama dan suhu pasien
    nama_pasien = []
    suhu_pasien = []
    # memasukkan jumlah pasien
    jumlah_pasien = int(input("Masukkan jumlah pasien: "))
    # list nama dan suhu pasien
    for i in range(jumlah_pasien):
        nama = input(f"Masukkan nama pasien ke-{i+1}: ")
        suhu = float(input(f"Masukkan suhu tubuh pasien ke-{i+1}: "))
        nama_pasien.append(nama)
        suhu_pasien.append(suhu)
    # rata-rata suhu tubuh
    rata_rata_suhu = sum(suhu_pasien) / jumlah_pasien
    # hasil analisis
    print("\nHasil Analisis:")
    print(f"Rata-rata suhu tubuh pasien: derajat Celcius")
    print(f"Pasien dengan suhu di atas derajat Celcius:")
    
    for i in range(jumlah_pasien):
        if suhu_pasien[i] > ambang_batas:
            print(f"derajat Celcius)")

if __name__ == "__main__":
    analisis_data/suhu()    
 
