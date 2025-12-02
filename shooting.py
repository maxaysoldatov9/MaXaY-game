from ursina import *

bullets = []

def shoot():
    # TODO: Добавить стрельбу в игру
    bullet = Entity(
        model='sphere',
        scale=0.1,
        color=color.yellow,
        position=camera.world_position + camera.forward,
        collider='box'
    )
    bullet.forward_dir = camera.forward
    bullet.speed = 20
    bullet.life = 2  # жизнь пули в секундах
    bullets.append(bullet)


def update_bullets():
    # TODO:
    for b in bullets[:]:
        b.position += b.forward_dir * b.speed * time.dt
        b.life -= time.dt

        if b.life <= 0:
            destroy(b)
            bullets.remove(b)
