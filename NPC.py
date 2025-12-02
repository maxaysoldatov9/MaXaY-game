from ursina import *
from math import *


class NPC(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            # TODO: Добавить модельку для монстра
            model='models/monster/monster.fbx',
            scale=1.2,
            collider='box',
            **kwargs
        )
        self.hp = 3
        self.speed = 2
        self.state = 'patrol'
        self.patrol_dir = 1
        self.patrol_range = 4
        self.start_x = self.x


    def hit(self):
        self.hp -= 1
        self.color = color.rgb(255, 120, 120)
        if self.hp <= 0:
            destroy(self)
