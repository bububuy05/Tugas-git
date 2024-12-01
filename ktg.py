import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk translasi titik
def translasi(titik, dx, dy):
    matriks_translasi = np.array([dx, dy])
    return titik + matriks_translasi

# Fungsi untuk rotasi titik
def rotasi(titik, sudut):
    sudut_radian = np.radians(sudut)
    matriks_rotasi = np.array([
        [np.cos(sudut_radian), -np.sin(sudut_radian)],
        [np.sin(sudut_radian), np.cos(sudut_radian)]
    ])
    return np.dot(titik, matriks_rotasi.T)

# Titik awal garis
garis_awal = np.array([
    [0, 0],  # Titik awal (x1, y1)
    [3, 2]   # Titik akhir (x2, y2)
])

# Translasi (dx, dy)
dx, dy = 2, 3
garis_tertranslasi = np.array([translasi(t, dx, dy) for t in garis_awal])

# Rotasi (sudut dalam derajat)
sudut = 45
garis_terrotasi = np.array([rotasi(t, sudut) for t in garis_tertranslasi])

# Plot hasil
plt.figure(figsize=(8, 8))

# Garis awal
plt.plot(garis_awal[:, 0], garis_awal[:, 1], 'b-o', label='Garis Awal')

# Garis setelah translasi
plt.plot(garis_tertranslasi[:, 0], garis_tertranslasi[:, 1], 'g-o', label='Setelah Translasi')

# Garis setelah rotasi
plt.plot(garis_terrotasi[:, 0], garis_terrotasi[:, 1], 'r-o', label='Setelah Rotasi')

# Pengaturan grafik
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Translasi dan Rotasi Garis")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.show()