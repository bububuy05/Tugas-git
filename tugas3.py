print("Rekomendasi air harian\n")
umur = int(input("Masukan umur : "))
print("1.Laki-laki\n2.Perempuan")
gender = int(input("Pilih gender"))

if (umur >= 3) and (umur < 18):
    if(gender == 1) :
        print("Rekomendasi air : 1.6 Liter")
    else :
        print("Rekomendasi air : 1.4 Liter")
elif (umur >= 18) and (umur <= 64) :
    if (gender == 1) :
        print("Rekomendasi air : 2.5 Liter")
    else :
        print("Rekomendasi air : 2.0 Liter")
elif (umur >= 65) :
    if (gender == 1) :
        print("Rekomendasi air : 2.0 Liter")
    else :
        print("Rekomendasi air : 1.8 Liter")
else :
    print("masih diberi asi")

    #nama_pasien = []
while True:
    pasien = input("Masukkan nama pasien (ketik 'stop' untuk berhenti): ")
    if pasien.lower() == 'stop':
        break
    nama_pasien.append(pasien)

print("Daftar pasien:")
for pasien in nama_pasien:
    print(pasien)