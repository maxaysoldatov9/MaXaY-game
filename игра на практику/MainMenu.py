from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings_panel import SettingsPanel
from loading_screen import LoadingScreen
import math

class MainMenu:
    def __init__(self):
        self.menu_parent = Entity(parent=camera.ui, enabled=True)

        mouse.locked = False
        mouse.visible = True
        camera.ui_enabled = True

        # Фон
        self.bg = Entity(
            parent=self.menu_parent,
            model='quad',
            texture='image/bg main menu 2.jpg',
            scale=(2, 1),
            z=1,
            collider=None
        )
        # TODO: Добавить заголовок красивый, что это главное меню

        # кнопка играть
        self.play_btn = Entity(
            parent=self.menu_parent,
            model='quad',
            texture='image/play_button.png',
            scale=(0.35, 0.15),
            y=0.17,
            z=0,
            origin=(0, 0),
            collider='box',
            color=color.white
        )
        self.play_btn.on_click = self.on_play

        # кнопка настройки
        self.settings_btn = Entity(
            parent=self.menu_parent,
            model='quad',
            texture='image/settings_button-removebg-preview (1).png',
            scale=(0.45, 0.30),
            y=0.0,
            z=-0.1,
            origin=(0, 0),
            collider='box',
            color=color.white
        )
        self.settings_btn.on_click = self.show_settings

        # кнопка выход
        self.exit_btn = Entity(
            parent=self.menu_parent,
            model='quad',
            texture='image\exit_button-removebg-preview-removebg-preview-removebg-preview.png',
            scale=(0.372, 0.145),  # пропорции подогнаны
            y=-0.15,
            z=0,
            origin=(0, 0),
            collider='box',
            color=color.white
        )
        self.exit_btn.on_click = application.quit

        # Панель настроек и экран загрузки
        self.settings_panel = SettingsPanel(on_back=self.hide_settings)
        self.loading_screen = LoadingScreen()

    # кнопки
    def on_play(self):
        self.hide_menu()
        self.loading_screen.show(duration=0.6)
        invoke(lambda: self.loading_screen.hide(callback=self.start_gameplay, duration=0.6), delay=3)

    def show_settings(self):
        self.menu_parent.disable()
        self.settings_panel.enable()

    def hide_settings(self):
        self.settings_panel.disable()
        self.menu_parent.enable()

    def hide_menu(self):
        self.menu_parent.disable()

    # TODO: Перенести игровую сцену в отдельный файл
    # игровая сцена
    def start_gameplay(self):
        mouse.locked = True
        mouse.visible = False
        camera.ui_enabled = False

        # Пол
        Entity(model='plane', scale=(50, 1, 50), color=color.gray, collider='box')

        # Игрок
        self.player = FirstPersonController()
        self.player.gravity = 1
        self.player.speed = 5
        self.player.jump_height = 2
        self.player.position = (0, 2, 0)

        # Оружие
        weapon_model = load_model(r"models/shotgun.glb")
        self.weapon = Entity(
            model=weapon_model,
            parent=camera,
            position=(0.6, -0.4, 1),
            rotation=(0, -90, 0),
            scale=1.5,
            always_on_top=True
        )

        # Кубы окружения
        for i in range(5):
            Entity(model='cube', color=color.red, scale=2, position=(i * 3, 1, 5), collider='box')

        # Анимация оружия
        self.walk_cycle = 0
        def update():
            if held_keys['shift']:
                self.player.speed = 10
            else:
                self.player.speed = 5

            moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
            if moving:
                self.walk_cycle += time.dt * 6
                ox = math.sin(self.walk_cycle) * 0.03
                oy = math.sin(self.walk_cycle * 2) * 0.02
                rx = math.sin(self.walk_cycle * 2) * 2
                rz = math.sin(self.walk_cycle * 1.5)
                self.weapon.position = (0.6 + ox, -0.4 + oy, 1)
                self.weapon.rotation = (rx, -90, rz)
            else:
                self.weapon.position = (0.6, -0.4, 1)
                self.weapon.rotation = (0, -90, 0)

        self.update = update
