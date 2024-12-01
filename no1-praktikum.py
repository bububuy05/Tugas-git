def celcius_to_kelvin(c): return c + 273.15  # Konversi Celcius ke Kelvin
def celcius_to_farenheit(c): return (c * 9/5) + 32  # Konversi Celcius ke Farenheit
def celcius_to_reamur(c): return c * 4/5  # Konversi Celcius ke Reamur
def farenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15  # Konversi Farenheit ke Kelvin
def farenheit_to_celcius(f): return (f - 32) * 5/9  # Konversi Farenheit ke Celcius
def farenheit_to_reamur(f): return (f - 32) * 4/9  # Konversi Farenheit ke Reamur
def reamur_to_kelvin(r): return (r * 5/4) + 273.15  # Konversi Reamur ke Kelvin
def reamur_to_celcius(r): return r * 5/4  # Konversi Reamur ke Celcius
def reamur_to_farenheit(r): return (r * 9/4) + 32  # Konversi Reamur ke Farenheit
def kelvin_to_celcius(k): return k - 273.15  # Konversi Kelvin ke Celcius
def kelvin_to_farenheit(k): return (k - 273.15) * 9/5 + 32  # Konversi Kelvin ke Farenheit
def kelvin_to_reamur(k): return (k - 273.15) * 4/5  # Konversi Kelvin ke Reamur

def main():
    print("Konversi Suhu")  # Menampilkan judul
    print("Pilih jenis suhu yang ingin dikonversi:")  # Menampilkan pilihan
    print("1. Celcius")  # Pilihan 1
    print("2. Farenheit")  # Pilihan 2
    print("3. Reamur")  # Pilihan 3
    print("4. Kelvin")  # Pilihan 4

    pilihan = int(input("Masukkan pilihan (1-4): "))  # Mengambil input pilihan pengguna

    if pilihan == 1:  # Jika pilihan 1
        celcius = float(input("Masukkan suhu dalam Celcius: "))  # Input suhu Celcius
        print(f"{celcius} °C = {celcius_to_kelvin(celcius):.2f} K")  # Konversi ke Kelvin
        print(f"{celcius} °C = {celcius_to_farenheit(celcius):.2f} °F")  # Konversi ke Farenheit
        print(f"{celcius} °C = {celcius_to_reamur(celcius):.2f} °Re")  # Konversi ke Reamur

    elif pilihan == 2:  # Jika pilihan 2
        farenheit = float(input("Masukkan suhu dalam Farenheit: "))  # Input suhu Farenheit
        print(f"{farenheit} °F = {farenheit_to_kelvin(farenheit):.2f} K")  # Konversi ke Kelvin
        print(f"{farenheit} °F = {farenheit_to_celcius(farenheit):.2f} °C")  # Konversi ke Celcius
        print(f"{farenheit} °F = {farenheit_to_reamur(farenheit):.2f} °Re")  # Konversi ke Reamur

    elif pilihan == 3:  # Jika pilihan 3
        reamur = float(input("Masukkan suhu dalam Reamur: "))  # Input suhu Reamur
        print(f"{reamur} °Re = {reamur_to_kelvin(reamur):.2f} K")  # Konversi ke Kelvin
        print(f"{reamur} °Re = {reamur_to_celcius(reamur):.2f} °C")  # Konversi ke Celcius
        print(f"{reamur} °Re = {reamur_to_farenheit(reamur):.2f} °F")  # Konversi ke Farenheit

    elif pilihan == 4:  # Jika pilihan 4
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))  # Input suhu Kelvin
        print(f"{kelvin} K = {kelvin_to_celcius(kelvin):.2f} °C")  # Konversi ke Celcius
        print(f"{kelvin} K = {kelvin_to_farenheit(kelvin):.2f} °F")  # Konversi ke Farenheit
        print(f"{kelvin} K = {kelvin_to_reamur(kelvin):.2f} °Re")  # Konversi ke Reamur

    else:  # Jika pilihan tidak valid
        print("Pilihan tidak valid!")  # Menampilkan pesan kesalahan

if __name__ == "__main__":  # Jika script dijalankan secara langsung
    main()  # Memanggil fungsi utama