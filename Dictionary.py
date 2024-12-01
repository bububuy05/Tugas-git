data_limbah = {
    'lokasi1' : {
        'nama_lokasi' : 'Area kota 1',
        'jumlah_limbah' : {
            'plastik' : 500,
            'organik' : 300,
            'logam' : 200
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Area kota 1',
        'jumlah_limbah' : {
            'plastik' : 700,
            'organik' : 400,
            'logam' : 250
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Area kota 1',
        'jumlah_limbah' : {
            'plastik' : 600,
            'organik' : 350,
            'logam' : 300
        }
    }
}

# Jumlah limbah lokasi 2
print(data_limbah['lokasi2']['jumlah_limbah']['plastik'])

# Lokasi 3
print(data_limbah['lokasi3']['nama_lokasi'])

# Masukkan jumlah limbah organik dan logam setiap lokasi ke variabel
for lokasi in data_limbah.values():
    jumlah_organik = lokasi['jumlah_limbah']['organik']
    jumlah_logam = lokasi['jumlah_limbah']['logam']

    # Buat percabangan
    if jumlah_organik > 400 or jumlah_logam > 250:
        print(f"Lokasi {lokasi['nama_lokasi']} memerlukan penanganan khusus.")
    else:
        print(f"Lokasi {lokasi['nama_lokasi']} dalam kondisi aman.")