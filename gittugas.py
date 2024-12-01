data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Tampilkan seluruh data dari data_panen
print("Seluruh Data Panen:")
for lokasi, detail in data_panen.items():
    print(f"{lokasi}:")
    print(f"  Nama Lokasi: {detail['nama_lokasi']}")
    print("  Hasil Panen:")
    for komoditas, jumlah in detail['hasil_panen'].items():
        print(f"    {komoditas}: {jumlah}")
    print()

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
print("Jumlah Hasil Panen Jagung dari Lokasi2:")
print(data_panen['lokasi2']['hasil_panen']['jagung'])

# 3. Tampilkan nama lokasi dari lokasi3
print("\nNama Lokasi dari Lokasi3:")
print(data_panen['lokasi3']['nama_lokasi'])

# 4. Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda
hasil_panen_padi = {}
hasil_panen_kedelai = {}

for lokasi, detail in data_panen.items():
    hasil_panen_padi[lokasi] = detail['hasil_panen']['padi']
    hasil_panen_kedelai[lokasi] = detail['hasil_panen']['kedelai']

print("\nHasil Panen Padi:")
print(hasil_panen_padi)
print("\nHasil Panen Kedelai:")
print(hasil_panen_kedelai)

# 5. Percabangan untuk menentukan status lokasi
print("\nStatus Lokasi:")
for lokasi, detail in data_panen.items():
    padi = detail['hasil_panen']['padi']
    jagung = detail['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        status = "Memerlukan Perhatian Khusus"
    else:
        status = "Dalam Kondisi Baik"
    
    print(f"{lokasi} - {detail['nama_lokasi']}: {status}")