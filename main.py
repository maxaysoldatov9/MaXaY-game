from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
from MainMenu import MainMenu

app = Ursina()


#Глобальные переменные
player = None
weapon = None
speed_multiplier = 2
walk_cycle = 0

# TODO: Добавить, чтобы работала пауза
# Пауза
paused = False
pause_ui = None

# Функция запуска игры
def start_gameplay():
    global player, weapon

    # Пол
    Entity(model='plane', scale=(50,1,50), color=color.gray, collider='box')

    # Игрок
    player = FirstPersonController()
    player.gravity = 1
    player.speed = 5
    player.jump_height = 2
    player.position = Vec3(0,2,0)

    # Оружие
    weapon_model = load_model(r"models\shotgun.glb")
    weapon = Entity(
        model=weapon_model,
        parent=camera,
        position=Vec3(0.6, -0.4, 1),
        rotation=Vec3(0, -90, 0),
        scale=1.5,
        always_on_top=True
    )

    # Несколько кубов для окружения
    for i in range(5):
        Entity(model='cube', color=color.red, scale=2, position=(i*3,1,5), collider='box')

#Пауза
def toggle_pause():
    global paused, pause_ui

    # пауза работает только если игрок создан
    if player is None:
        return

    if not paused:
        paused = True
        mouse.locked = False
        mouse.visible = True

        # UI паузы
        pause_ui = Entity(parent=camera.ui)

        # Полупрозрачный фон
        Panel(parent=pause_ui, scale=2, color=color.rgba(0,0,0,180))

        # Текст
        Text('ПАУЗА', parent=pause_ui, scale=2, y=0.3)

        # Кнопка "Продолжить"
        Button('Продолжить', parent=pause_ui, scale=(0.5,0.1), y=0.1, on_click=resume_game)

        # Кнопка "Выход в меню"
        Button('Выход в меню', parent=pause_ui, scale=(0.5,0.1), y=-0.1, on_click=exit_to_menu)
    else:
        resume_game()

def resume_game():
    global paused, pause_ui
    paused = False
    mouse.locked = True
    mouse.visible = False

    if pause_ui:
        destroy(pause_ui)
        pause_ui = None

def exit_to_menu():
    global paused
    resume_game()
    MainMenu()  # возвращаемся в главное меню

# Обработка ввода
def input(key):
    if key == 'escape' and player is not None:
        toggle_pause()

# Обновление
def update():
    global walk_cycle

    if player is None or paused:
        return  # если пауза — не обновляем игрока

    # скорость
    if held_keys['shift']:
        player.speed = 5 * speed_multiplier
    else:
        player.speed = 5

    # анимация оружия
    is_moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    if is_moving:
        walk_cycle += time.dt * 6
        offset_x = math.sin(walk_cycle) * 0.03
        offset_y = math.sin(walk_cycle * 2) * 0.02
        rot_x = math.sin(walk_cycle * 2) * 2
        rot_z = math.sin(walk_cycle) * 1.5
        weapon.position = Vec3(0.6 + offset_x, -0.4 + offset_y, 1)
        weapon.rotation = Vec3(rot_x, -90, rot_z)
    else:
        weapon.position = Vec3(0.6, -0.4, 1)
        weapon.rotation = Vec3(0, -90, 0)

# Главное меню
MainMenu()  # сначала открывается меню
app.run()
