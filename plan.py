import pygame, math

FENETRE = (1600, 900)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

X = 0
Y = 1
Z = 2

clic_start = [0, 0]
clic_actif = False
redessiner = True

obs = [0, 0, -1400]

def traiter_evenements():
   global clic_actif, clic_start, obs, redessiner
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
            redessiner = True
            bouger_points(10)
         elif evenement.button == 5:
            redessiner = True
            bouger_points(-10)
      elif evenement.type == pygame.MOUSEBUTTONUP:
         if evenement.button == 1:
            clic_actif = False
      elif evenement.type == pygame.MOUSEMOTION:
         if clic_actif:
            redessiner = True
            diff_x = evenement.pos[X] - clic_start[X]
            diff_y = evenement.pos[Y] - clic_start[Y]
            rotationY(-2*diff_x / FENETRE[X])
            rotationX(2*diff_y / FENETRE[Y])
            clic_start[X] = evenement.pos[X]
            clic_start[Y] = evenement.pos[Y]


def distance(v1, v2):
   dist_carre = 0
   for i in range(len(v1)):
      dist_carre += (v1[i] - v2[i]) ** 2

   return math.sqrt(dist_carre)

def bouger_points(dist):
   for p in points:
      p[Z] += dist

def dessiner():
   dist = obs[Z]
   for p in points:
      x = dist * p[X] / (p[Z] + dist)
      y = dist * p[Y] / (p[Z] + dist)
      pygame.draw.circle(fenetre, BLEU, (int(x) + (FENETRE[X] // 2), (FENETRE[Y] // 2)-int(y)), 4)
      # pygame.draw.circle(fenetre, BLEU, (int(p[0] + 400), int(300-p[1])), 4)

   for l in lignes:
      start_x = dist * points[l[0]][X] / (points[l[0]][Z] + dist)
      start_y = dist * points[l[0]][Y] / (points[l[0]][Z] + dist)

      end_x = dist * points[l[1]][X] / (points[l[1]][Z] + dist)
      end_y = dist * points[l[1]][Y] / (points[l[1]][Z] + dist)

      start = (start_x + (FENETRE[X] // 2), (FENETRE[Y] // 2)-start_y)
      end = (end_x + (FENETRE[X] // 2), (FENETRE[Y] // 2)-end_y)

      # start = (points[l[0]][0] + 400, 300-points[l[0]][1])
      # end = (points[l[1]][0] + 400, 300-points[l[1]][1])

      couleur = l[2];

      largeur = 4 if couleur == VERT else 2
      pygame.draw.line(fenetre, couleur, start, end, largeur)

def rotationZ(angle):
   sin = math.sin(angle)
   cos = math.cos(angle)

   for p in points:
      x = p[X]
      y = p[Y]

      p[X] = x * cos - y * sin
      p[Y] = y * cos + x * sin

def rotationY(angle):
   sin = math.sin(angle)
   cos = math.cos(angle)

   for p in points:
      x = p[X]
      z = p[Z]

      p[X] = x * cos - z * sin
      p[Z] = z * cos + x * sin

def rotationX(angle):
   sin = math.sin(angle)
   cos = math.cos(angle)

   for p in points:
      y = p[Y]
      z = p[Z]

      p[Y] = y * cos - z * sin
      p[Z] = z * cos + y * sin


pygame.init()
fenetre = pygame.display.set_mode(FENETRE)

points = []
lignes = []

zt = 1000
dist = 40
for i in range(0, zt//dist):
   points.append([dist*i, 0, -zt])
   points.append([dist*i, 0, zt])
   points.append([-dist*i, 0, -zt])
   points.append([-dist*i, 0, zt])

   points.append([-zt, 0, dist*i])
   points.append([zt, 0, dist*i])
   points.append([-zt, 0, -dist*i])
   points.append([zt, 0, -dist*i])

   lignes.append([8*i, 8*i+1, ROUGE])
   lignes.append([8*i+2, 8*i+3, ROUGE])
   lignes.append([8*i+4, 8*i+5, ROUGE])
   lignes.append([8*i+6, 8*i+7, ROUGE])

points.append([0, zt, 0])
points.append([0, -zt, 0])
lignes.append([(8 * (zt // dist)),(8 * (zt // dist) + 1), VERT])
# rotationX(0.2)
# rotationY(0.1)

fenetre.fill(BLANC)
pygame.display.flip()

while True:
   traiter_evenements()

   fenetre.fill(BLANC)
   dessiner()
   pygame.display.flip()
   redessiner = False
   pygame.time.Clock().tick(30)

