from ursina import *

class SettingsPanel(Entity):
    def __init__(self, on_back=None):
        super().__init__(parent=camera.ui, enabled=False)

        # фон
        # TODO: Изменить фон внутри настроек
        Entity(parent=self, model='quad', texture='image/bg main menu 2.jpg', scale=(2,1), z=0)
        overlay = Panel(parent=self, scale=(1.8,1), color=color.rgba(0,0,0,150), z=1)
        overlay.ignore_input = True
        # TODO: Изменить заголовок настройки на красивое изображение
        # заголовок
        Text('Настройки', parent=self, y=0.45, x=0, scale=1.5, color=color.white)
        # TODO: Добавить кнопку для управления музыкой
        # TODO: Добавить кнопку для управления музыкой чувствительностью

        # кнопка звуки
        self.sound_on = True
        self.sound_btn = Entity(
            parent=self,
            model='quad',
            # TODO: Изменить название файлов и переделать полностью путь.
            texture='image/sound_button_off-removebg-preview.png',
            scale=(0.4, 0.18),
            y=-0.22,
            z=-0.1,
            origin=(0, 0),
            collider='box',
            color=color.white
        )
        self.sound_btn.on_click = self.toggle_sound

        # кнопочка назад
        self.back_btn = Entity(
            parent=self,
            model='quad',
            texture='image/back_button-removebg-preview (1).png',
        # TODO: Подогнать по размерам
            scale=(0.4, 0.18),
            y=-0.4,
            z=-0.1,
            origin=(0, 0),
            collider='box',
            color=color.white
        )
        self.back_btn.on_click = lambda: (self.disable(), on_back() if on_back else None)

    # логика переключения звуков
    def toggle_sound(self):
        self.sound_on = not self.sound_on
        if self.sound_on:
            self.sound_btn.texture = 'image/sound_button_on-removebg-preview (1).png'
        else:
            self.sound_btn.texture = 'image/sound_button_off-removebg-preview.png'
