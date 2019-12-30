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


def dessiner():
   for p in points:
      pygame.draw.circle(fenetre, BLEU, (int(p[0] + 400), int(300-p[1])), 4)

   for l in lignes:
      start = (points[l[0]][0] + 400, 300-points[l[0]][1])
      end = (points[l[1]][0] + 400, 300-points[l[1]][1])

      pygame.draw.line(fenetre, ROUGE, start, end, 2)

def bouger_points(dist):
   for p in points:
      p[Z] += dist

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

point0 = [-100, -100, -100];
point1 = [-100, -100,  100];
point2 = [-100,  100, -100];
point3 = [-100,  100,  100];
point4 = [ 100, -100, -100];
point5 = [ 100, -100,  100];
point6 = [ 100,  100, -100];
point7 = [ 100,  100,  100];
points = [point0, point1, point2, point3, point4, point5, point6, point7];

ligne0  = [0, 1];
ligne1  = [1, 3];
ligne2  = [3, 2];
ligne3  = [2, 0];
ligne4  = [4, 5];
ligne5  = [5, 7];
ligne6  = [7, 6];
ligne7  = [6, 4];
ligne8  = [0, 4];
ligne9  = [1, 5];
ligne10 = [2, 6];
ligne11 = [3, 7];
lignes  = [ligne0, ligne1, ligne2, ligne3, ligne4, ligne5, ligne6, ligne7, ligne8, ligne9, ligne10, ligne11];


fenetre.fill(BLANC)
pygame.display.flip()

while True:
   traiter_evenements()

   fenetre.fill(BLANC)
   dessiner()
   pygame.display.flip()
   pygame.time.Clock().tick(30)

