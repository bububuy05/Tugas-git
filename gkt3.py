import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar segitiga dengan titik puncak
def draw_triangle(image, vertices, color=1):
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    plt.plot(x + [x[0]], y + [y[0]], color="black")  # Gambar garis segitiga
    for i in range(len(vertices)):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % len(vertices)]
        line_points = get_line_points(x0, y0, x1, y1)
        for (px, py) in line_points:
            if 0 <= px < image.shape[1] and 0 <= py < image.shape[0]:
                image[py, px] = color

# Fungsi untuk algoritma garis Bresenham untuk menggambar sisi segitiga
def get_line_points(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

# Fungsi Flood Fill 4-Connected
def flood_fill_4(image, x, y, new_color, target_color=None):
    if target_color is None:
        target_color = image[y, x]
    if image[y, x] != target_color or image[y, x] == new_color:
        return
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < image.shape[1] and 0 <= cy < image.shape[0] and image[cy, cx] == target_color:
            image[cy, cx] = new_color
            stack.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])

# Ukuran kanvas
width, height = 20, 20
image = np.zeros((height, width), dtype=int)

# Koordinat segitiga
vertices = [(5, 5), (15, 5), (10, 15)]

# Gambar segitiga pada kanvas
draw_triangle(image, vertices)

# Koordinat titik awal pengisian dan warna baru
x_start, y_start = 10, 10
new_color = 2

# Lakukan flood fill
flood_fill_4(image, x_start, y_start, new_color)

# Tampilkan hasil
plt.imshow(image, cmap="Set3", origin="lower")
plt.title("Segitiga dengan Algoritma Flood Fill 4-Connected")
plt.show()