import math #digunakan untuk menghitung koordinat titik-titik yang membentuk gambar hati.
from turtle import *#Mengimpor semua fungsi dan variabel dari modul menggunakan konsep kura-kura (turtle).

def heart(k): # yang menggambarkan bagian atas dari bentuk hati.
              # Nilai kembalian dari fungsi ini adalah nilai y untuk suatu nilai x tertentu (diwakili oleh variabel k).
    return 15*math.sin(k)**3 

def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

speed(1000)
bgcolor('black')
for i in range(6000):
    goto(heart(i)*20,heart1(i)*20)
    for j in range(5):
        color('pink')

done()