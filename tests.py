import pygame, math

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
   global clic_actif, clic_start, obs
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
            bouger_points(10)
         elif evenement.button == 5:
            bouger_points(-10)
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
      pygame.draw.circle(fenetre, BLEU, (int(x) + 400, 300-int(y)), 4)
      # pygame.draw.circle(fenetre, BLEU, (int(p[0] + 400), int(300-p[1])), 4)

   for l in lignes:
      start_x = dist * points[l[0]][X] / (points[l[0]][Z] + dist)
      start_y = dist * points[l[0]][Y] / (points[l[0]][Z] + dist)

      end_x = dist * points[l[1]][X] / (points[l[1]][Z] + dist)
      end_y = dist * points[l[1]][Y] / (points[l[1]][Z] + dist)

      start = (start_x + 400, 300-start_y)
      end = (end_x + 400, 300-end_y)

      # start = (points[l[0]][0] + 400, 300-points[l[0]][1])
      # end = (points[l[1]][0] + 400, 300-points[l[1]][1])


      pygame.draw.line(fenetre, ROUGE, start, end, 2)

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

points = [
[0, 50, -25.0], [50, 50, -25.0], [50, 50, 25.0], [0, 50, 25.0] ,[0, 0, -25.0], [50, 0, -25.0], [50, 0, 25.0], [0, 0, 25.0]]

lignes=[]

fenetre.fill(BLANC)
pygame.display.flip()

while True:
   traiter_evenements()

   # rotationY(0.03)
   fenetre.fill(BLANC)
   dessiner()
   pygame.display.flip()
   pygame.time.Clock().tick(30)

