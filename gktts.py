#include <graphics.h>
#include <iostream>

using namespace std;

// Deklarasi prosedur
void rectangle(int x, int y, int width, int height);
void circle(int x, int y, int radius);
void ellipse(int x, int y, int stangle, int endangle, int xradius, int yradius);
void drawpoly(int numpoints, int *polypoints);
void fillellipse(int x, int y, int xradius, int yradius);
void fillpoly(int numpoints, int *polypoints);

// Fungsi untuk menggambar dan mengarsir objek
void drawAndFill(int x, int y, int type, string fillPattern);

int main() {
    // Inisialisasi grafik
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Contoh pemanggilan fungsi untuk menggambar beberapa objek
    drawAndFill(100, 100, 1, "solidfill"); // Persegi solid
    drawAndFill(250, 150, 2, "hatchfill"); // Lingkaran hatch
    // ... dan seterusnya

    getch();
    closegraph();
    return 0;
}

// Implementasi prosedur-prosedur
// ... (isi dengan implementasi prosedur sesuai dengan library grafik yang digunakan)

// Fungsi drawAndFill
void drawAndFill(int x, int y, int type, string fillPattern) {
    // Logika untuk menentukan jenis objek, menggambar, dan mengarsir
    // ... (gunakan switch-case untuk memilih jenis objek dan prosedur yang sesuai)
    // ... (gunakan setfillstyle untuk mengatur pola arsiran)
    // ... (gunakan floodfill untuk mengisi objek dengan arsiran)
    // ... (gunakan outtextxy untuk menuliskan nama arsiran)
}