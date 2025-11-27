from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math

app = Ursina()

# --- Карта ---
Entity(model='plane', scale=(50,1,50), color=color.gray, collider='box')

# --- Игрок ---
player = FirstPersonController()
player.gravity = 1
player.speed = 5
player.jump_height = 2
player.position = Vec3(0,2,0)

# --- Оружие ---
weapon_model = load_model(r"models\shotgun.glb")
weapon = Entity(
    model=weapon_model,
    parent=camera,
    position=Vec3(0.9, -0.9, 1.5),
    rotation=Vec3(0, -90, 0),
    scale=1.5,
    always_on_top=True
)

# --- Кубы для теста ---
for i in range(5):
    Entity(model='cube', color=color.red, scale=2, position=(i*3,1,5), collider='box')

# --- Параметры анимации ---
speed_multiplier = 2
walk_cycle = 0

def update():
    global walk_cycle

    # --- Бег через Shift ---
    if held_keys['shift']:
        player.speed = 5 * speed_multiplier
    else:
        player.speed = 5

    # --- Проверка движения ---
    is_moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']

    if is_moving:
        walk_cycle += time.dt * 6  # скорость шага
        # Плавное движение вперед-назад
        offset_x = math.sin(walk_cycle) * 0.03
        offset_y = math.sin(walk_cycle * 2) * 0.02
        # Плавное вращение: наклон вперед-назад и немного в стороны
        rot_x = math.sin(walk_cycle * 2) * 2
        rot_z = math.sin(walk_cycle) * 1.5

        weapon.position = Vec3(0.6 + offset_x, -0.4 + offset_y, 1)
        weapon.rotation = Vec3(rot_x, -90, rot_z)
    else:
        # Вернуть оружие в исходное положение
        weapon.position = Vec3(0.6, -0.4, 1)
        weapon.rotation = Vec3(0, -90, 0)

app.run()
