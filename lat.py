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
#semua data lokasi
for lokasi in data_limbah.values():
    print(lokasi)

#jumlah limbah lokasi2
print(data_limbah['lokasi2']['jumlah_limbah']['plastik'])

#lokasi3
print(data_limbah['lokasi3']['nama_lokasi'])

#masukan jumlah limbah organik dan logam setiap lokasi ke variabel
#buat percabangan jika jumlah limbah organik lebih dari 400
#atau jumlah limbah logam lebih dari 250,
#maka lokasi tersebut memerlukan penanganan khusus
#jika tidak, maka lokasi tersebut dalam kondisi aman

for lokasi in data_limbah.values():
    jumlah_organik = lokasi['jumlah_limbah']['organik']
    jumlah_logam = lokasi['jumlah_limbah']['logam']

    if jumlah_organik > 400 or jumlah_logam > 250:
        print(f"Lokasi {lokasi['nama_lokasi']} memerlukan penanganan khusus.")
    else:
        print(f"Lokasi {lokasi['nama_lokasi']} dalam kondisi aman.")