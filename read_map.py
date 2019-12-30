import pygame, math
X = 0
Y = 1
Z = 2

def read_map(triangles, map_adresse, size = 20):
   f = open(map_adresse)
   cont = f.read()
   f.close

   colmax = 0
   col = 0
   line = 0

   for c in cont:
      if c == '1':
         new_cube(triangles, line, col, size)

      if c == '\n':
         if col > colmax:
            colmax = col
         col = 0
         line += 1
      else:
         col += 1

   bouger_points(triangles, (colmax * size) / -2, (line * size) / 2, 0)

def bouger_points(triangles, x, y, z):
   for points in triangles:
      for p in points:
         p[X] += x
         p[Y] += y
         p[Z] += z

def new_cube(triangles, line, col, size):
   d = size/2

   xm = (col * size)
   xp = (col + 1) * size

   yp = (line * size)
   ym = (line + 1) * size

   p1 = [xm, -yp, -d]
   p2 = [xp, -yp, -d]
   p3 = [xp, -yp, d]
   p4 = [xm, -yp, d]

   p5 = [xm, -ym, -d]
   p6 = [xp, -ym, -d]
   p7 = [xp, -ym, d]
   p8 = [xm, -ym, d]

   print(p1, p2, p3, p4, p5, p6, p7, p8)

   triangles.append([p1.copy(), p3.copy(), p4.copy()])
   triangles.append([p1.copy(), p3.copy(), p2.copy()])
   triangles.append([p1.copy(), p5.copy(), p6.copy()])
   triangles.append([p1.copy(), p2.copy(), p6.copy()])
   triangles.append([p3.copy(), p2.copy(), p6.copy()])
   triangles.append([p8.copy(), p5.copy(), p4.copy()])
   triangles.append([p8.copy(), p5.copy(), p7.copy()])
   triangles.append([p6.copy(), p5.copy(), p7.copy()])
   triangles.append([p4.copy(), p3.copy(), p8.copy()])
   triangles.append([p7.copy(), p3.copy(), p8.copy()])
   triangles.append([p1.copy(), p4.copy(), p8.copy()])
   triangles.append([p1.copy(), p5.copy(), p8.copy()])
