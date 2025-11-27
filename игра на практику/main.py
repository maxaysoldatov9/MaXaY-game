from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(
    model='plane',
    scale=(50,1,50),
    texture='white_cube',
    texture_scale=(50,50),
    collider='box'
)

player = FirstPersonController()
player.gravity = 1
player.speed = 5
player.jump_height = 2

for i in range(5):
    Entity(model='cube', color=color.red, scale=2, position=(i*3,1,5), collider='box')

weapon = Entity(
    model=r"C:\Users\solda\Desktop\игра на практику\models\shotgun.glb",
    parent=camera,
    position=Vec3(0.5, -0.5, 1),
    rotation=Vec3(0,180,0),
    scale=0.2
)

speed_multiplier = 2

def update():
    # Бег через Shift
    if held_keys['shift']:
        player.speed = 5 * speed_multiplier
    else:
        player.speed = 5

app.run()
