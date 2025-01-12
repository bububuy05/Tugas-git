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
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("data panen:")
for lokasi, data in data_panen.items():
    print(f"{lokasi}: Nama Lokasi: {data['nama_lokasi']}, Hasil Panen: {data['hasil_panen']}")

jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah hasil panen jagung dari lokasi2: {jagung_lokasi2}")

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama lokasi dari lokasi3: {nama_lokasi3}")

hasil_panen_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_panen_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print(f"\nJumlah hasil panen padi setiap lokasi: {hasil_panen_padi}")
print(f"Jumlah hasil panen kedelai setiap lokasi: {hasil_panen_kedelai}")

print("\nLokasi yang memerlukan perhatian khusus:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"- {data['nama_lokasi']} (Padi: {padi}, Jagung: {jagung})")
