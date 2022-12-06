from dino_runner.components.obstacle.obstacle import Obstacle
import random

class Cactus(Obstacle):

    def __init(self, image):
        self.type = random.randit(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

