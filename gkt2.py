import turtle
# Membuat objek turtle
t = turtle.Turtle()
# Mengatur kecepatan gerak turtle
t.speed(1)
# Mengatur ukuran pena
t.pensize(3)
# Mengatur warna pena
t.color("black")
# Jari-jari lingkaran
r = 8
# Menggambar lingkaran
for i in range(360):
  t.forward(2*r*3.14/360)
  t.left(1)
turtle.done()