import random
from dino_runner.components.obstacles.obstacle import Obstacle

class CactusLarge(Obstacle):

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 300