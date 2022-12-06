import pygame

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacle = []

    def update(self,game):
        if len(self.obstacle) == 0:
            self.obstacle.append(Cactus(SMALL_CACTUS))
        
        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect():
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self ,screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)