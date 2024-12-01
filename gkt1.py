import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
  x_inc = dx / steps
  y_inc = dy / steps
  x = x1
  y = y1
  points = [(x, y)]
  for i in range(steps):
    x += x_inc
    y += y_inc
    points.append((round(x), round(y)))
  return points

# Titik awal dan akhir
x1, y1 = 2, 5
x2, y2 = 7, 12

# Hitung titik-titik garis
points = dda_line(x1, y1, x2, y2)

# Plot garis
x_coords, y_coords = zip(*points)
plt.plot(x_coords, y_coords, marker='o')
plt.grid(True)
plt.show()