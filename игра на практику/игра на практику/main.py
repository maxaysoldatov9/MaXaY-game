from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math

app = Ursina()

# ---------------- игра ----------------
player = None
weapon = None
bullets = []

def start_gameplay():
    global player, weapon

    # пол (простой куб вместо текстурного плана)
    Entity(model='cube', scale=(20,1,20), color=color.gray, collider='box', y=0)

    # игрок
    player = FirstPersonController()
    player.gravity = 1
    player.speed = 5
    player.jump_height = 2
    player.position = (0,1,0)

    weapon = Entity(
        model='models/shotgun.glb',  # уже со своей текстурой
        parent=camera,
        position=(1, -0.8, 1.5),
        rotation=(0, -90, 0),
        scale=3,
        always_on_top=True
    )
    weapon.start_pos = weapon.position


# ---------------- стрельба ----------------
def input(key):
    if player is None:
        return
    if key == 'left mouse down':
        shoot()

def shoot():
    bullet = Entity(
        model='sphere',
        scale=0.1,
        color=color.yellow,
        position=camera.world_position + camera.forward,
        collider='box'
    )
    bullet.forward_dir = camera.forward
    bullet.speed = 20
    bullet.life = 2
    bullets.append(bullet)

def update_bullets():
    for b in bullets[:]:
        b.position += b.forward_dir * b.speed * time.dt
        b.life -= time.dt
        if b.life <= 0:
            destroy(b)
            bullets.remove(b)


# ---------------- анимация оружия ----------------
walk_cycle = 0
speed_multiplier = 2
recoil = 0

def update():
    global walk_cycle, recoil

    if player is None:
        return

    # бег
    if held_keys['shift']:
        player.speed = 5 * speed_multiplier
    else:
        player.speed = 5

    # движение игрока и анимация оружия
    moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    if moving:
        walk_cycle += time.dt * 6
        ox = math.sin(walk_cycle) * 0.03
        oy = math.sin(walk_cycle * 2) * 0.02
        rx = math.sin(walk_cycle * 2) * 2
        rz = math.sin(walk_cycle * 1.5)
        weapon.position = weapon.start_pos + Vec3(ox, oy, 0)
        weapon.rotation = (rx, -90, rz)
    else:
        weapon.position = weapon.start_pos
        weapon.rotation = (0, -90, 0)

    # отдача оружия
    if recoil > 0:
        weapon.position += (0, 0, -0.01)
        recoil -= 0.3
    else:
        recoil = 0

    # обновление пуль
    update_bullets()


# ---------------- запуск ----------------
start_gameplay()
app.run()
