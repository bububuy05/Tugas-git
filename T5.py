def hitung_IMT(berat, tinggi):  
    # Menghitung IMT  
    imt = berat / (tinggi ** 2)  
    return imt  
def kategori_kesehatan(imt):  
    # Menentukan kategori kesehatan berdasarkan IMT  
    if imt < 18.5:  
        return "Underweight"  
    elif 18.5 <= imt < 25:  
        return "Normal weight"  
    elif 25 <= imt < 30:  
        return "Overweight"  
    else:  # imt >= 30  
        return "Obesity"  
def main():  
    while True:  
        # Meminta user menginput 
        berat = float(input("Masukkan berat badan (kg): "))  
        tinggi = float(input("Masukkan tinggi badan (m): "))  
        # hitung IMT  
        imt = hitung_IMT(berat, tinggi)  
        # Menentukan kategori kesehatan  
        kategori = kategori_kesehatan(imt)  
        # Menampilkan hasil  
        print(f"IMT: {imt:.2f}, Kategori: {kategori}")  
        # ini untuk lanjut menghitung atau tidak 
        lagi = input("Ingin menghitung lagi? (ya/ga): ")  
        if lagi.lower() != 'ya':  
            break
if __name__ == "__main__":  
    main()  
        