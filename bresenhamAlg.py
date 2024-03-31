import pygame, sys

def bresenhamLinha(x1, y1, x2, y2):
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  erro = dx - dy
  x = x1
  y = y1

  if (x1 < x2):
    xIncremento = 1
  else:
    xIncremento = -1

  if (y1 < y2):
    yIncremento = 1
  else:
    yIncremento = -1
  desenhaPixel(x, y)

  while ((x != x2) or (y != y2)):
    erro2 = 2 * erro
    if (erro2 > -dy):
      erro = erro - dy
      x = x + xIncremento

    if (erro2 < dx):
      erro = erro + dx
      y = y + yIncremento
    desenhaPixel(x, y)

def bresenhamCircunferencia(xCentro, yCentro, raio):
  x = 0
  y = raio
  delta = 3 - 2 * raio

  while (x <= y):
    desenhaCircunferencia(xCentro, yCentro, x, y)

    if (delta < 0):
      delta = delta + (4 * x) + 6
    else:
      delta = delta + (4 * (x - y)) + 10
      y = y - 1
    x = x + 1

def desenhaCircunferencia(xCentro, yCentro, x, y):
  desenhaPixel(xCentro + x, yCentro + y)
  desenhaPixel(xCentro - x, yCentro + y)
  desenhaPixel(xCentro + x, yCentro - y)
  desenhaPixel(xCentro - x, yCentro - y)
  desenhaPixel(xCentro + y, yCentro + x)
  desenhaPixel(xCentro - y, yCentro + x)
  desenhaPixel(xCentro + y, yCentro - x)
  desenhaPixel(xCentro - y, yCentro - x)

def desenhaPixel(x, y):
  screen.set_at((round(x), round(y)), (255, 255, 255))

pygame.init()

screen = pygame.display.set_mode((50, 50))
screen.fill((0, 0, 0))

bresenhamLinha(0, 30, 50, 50)
bresenhamLinha(10, 35, 50, 0)
bresenhamLinha(20, 0, 20, 50)
bresenhamCircunferencia(35, 25, 8)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()