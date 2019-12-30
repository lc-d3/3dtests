import pygame, math
from read_map import *

FENETRE = (800, 600)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

X = 0
Y = 1
Z = 2

clic_start = [0, 0]
clic_actif = False
obs = [0, 0, -500]

def traiter_evenements():
   global clic_actif, clic_start
   for evenement in pygame.event.get():
      if evenement.type == pygame.QUIT:
         pygame.display.quit()
         exit()
      elif evenement.type == pygame.MOUSEBUTTONDOWN:
         if evenement.button == 1:
            clic_actif = True
            clic_start[X] = evenement.pos[X]
            clic_start[Y] = evenement.pos[Y]
         elif evenement.button == 4:
            bouger_points(triangles, 0, 0, 10)
         elif evenement.button == 5:
            bouger_points(triangles, 0, 0, -10)
      elif evenement.type == pygame.MOUSEBUTTONUP:
         if evenement.button == 1:
            clic_actif = False
      elif evenement.type == pygame.MOUSEMOTION:
         if clic_actif:
            diff_x = evenement.pos[X] - clic_start[X]
            diff_y = evenement.pos[Y] - clic_start[Y]
            rotationY(-2*diff_x / FENETRE[X])
            rotationX(2*diff_y / FENETRE[Y])
            clic_start[X] = evenement.pos[X]
            clic_start[Y] = evenement.pos[Y]

def dessiner_ligne(a, b):
   dist = obs[Z]

   start_x = dist * a[X] / (a[Z] + dist)
   start_y = dist * a[Y] / (a[Z] + dist)

   end_x = dist * b[X] / (b[Z] + dist)
   end_y = dist * b[Y] / (b[Z] + dist)

   start = (start_x + 400, 300-start_y)
   end = (end_x + 400, 300-end_y)
   pygame.draw.line(fenetre, ROUGE, start, end, 2)


def dessiner():
   dist = obs[Z]

   for points in triangles:
      for p in points:
         x = dist * p[X] / (p[Z] + dist)
         y = dist * p[Y] / (p[Z] + dist)
         pygame.draw.circle(fenetre, BLEU, (int(x) + 400, 300-int(y)), 4)

      dessiner_ligne(points[0], points[1])
      dessiner_ligne(points[1], points[2])
      dessiner_ligne(points[2], points[0])

def rotationZ(angle):
   sin = math.sin(angle)
   cos = math.cos(angle)

   for points in triangles:
      for p in points:
         x = p[X]
         y = p[Y]

         p[X] = x * cos - y * sin
         p[Y] = y * cos + x * sin

def rotationY(angle):
   sin = math.sin(angle)
   cos = math.cos(angle)

   for points in triangles:
      for p in points:
         x = p[X]
         z = p[Z]

         p[X] = x * cos - z * sin
         p[Z] = z * cos + x * sin

def rotationX(angle):
   sin = math.sin(angle)
   cos = math.cos(angle)

   for points in triangles:
      for p in points:
         y = p[Y]
         z = p[Z]

         p[Y] = y * cos - z * sin
         p[Z] = z * cos + y * sin

triangles = []
read_map(triangles, "map.txt", 50)

pygame.init()
fenetre = pygame.display.set_mode(FENETRE)

fenetre.fill(BLANC)
pygame.display.flip()

while True:
   traiter_evenements()

   fenetre.fill(BLANC)
   dessiner()
   pygame.display.flip()
   pygame.time.Clock().tick(30)

