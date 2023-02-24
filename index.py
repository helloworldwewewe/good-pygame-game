import pygame
from sys import exit
pygame.init()
WIDTH = 400
HEIGHT = 400
player_W = 20
player_H = 20
game = pygame.display.set_mode((WIDTH, HEIGHT))
cookie = pygame.Rect((0, 0, player_W, player_H))
game.fill(255,255, 255)
game_over = False
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
  game.fill((255, 255, 255))
  pygame.draw.rect(game, (255, 0, 0), cookie)
  pygame.display.update()
  if pygame.mouse.get_pressed()[0] and cookie.collidepoint(pygame.mouse.get_pos()):
    print(1)
