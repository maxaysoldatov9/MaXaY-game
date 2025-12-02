from ursina import *
# TODO: удалить полностью настройки, оставить основным setting_panel.py
# ---------------- Настройки ----------------
settings = {
    'mouse_sensitivity': 1.0,
    'fullscreen': False,
    'music_enabled': True,
    'sound_enabled': True
}

# ---------------- Панель настроек ----------------
settings_panel = Entity(parent=camera.ui, enabled=False)


# Полупрозрачный фон
settings_bg = Panel(parent=settings_panel, scale=2, color=color.rgba(0,0,0,180))

# Заголовок
Text('Настройки', parent=settings_panel, y=0.35, scale=1.5)

# Слайдер чувствительности мыши
sens_slider = Slider(
    min=0.3,
    max=3,
    default=settings['mouse_sensitivity'],
    parent=settings_panel,
    y=0.1,
    step=0.1
)
Text('Чувствительность мыши', parent=settings_panel, y=0.18, scale=1)

# Кнопки
fullscreen_btn = Button(
    f"Полноэкранный: {'Вкл' if settings['fullscreen'] else 'Выкл'}",
    parent=settings_panel,
    scale=(0.5,0.12),
    y=-0.05
)

music_btn = Button(
    f"Музыка: {'Вкл' if settings['music_enabled'] else 'Выкл'}",
    parent=settings_panel,
    scale=(0.5,0.12),
    y=-0.18
)

sound_btn = Button(
    f"Звуки: {'Вкл' if settings['sound_enabled'] else 'Выкл'}",
    parent=settings_panel,
    scale=(0.5,0.12),
    y=-0.31
)

back_btn = Button(
    'Назад',
    parent=settings_panel,
    scale=(0.35,0.12),
    y=-0.45
)

# ---------------- Функции для кнопок ----------------
def toggle_fullscreen():
    settings['fullscreen'] = not settings['fullscreen']
    window.fullscreen = settings['fullscreen']
    fullscreen_btn.text = f"Полноэкранный: {'Вкл' if settings['fullscreen'] else 'Выкл'}"

def toggle_music():
    settings['music_enabled'] = not settings['music_enabled']
    music_btn.text = f"Музыка: {'Вкл' if settings['music_enabled'] else 'Выкл'}"

def toggle_sound():
    settings['sound_enabled'] = not settings['sound_enabled']
    sound_btn.text = f"Звуки: {'Вкл' if settings['sound_enabled'] else 'Выкл'}"

def update_sensitivity():
    settings['mouse_sensitivity'] = sens_slider.value

# Привязка функций к кнопкам/слайдеру
fullscreen_btn.on_click = toggle_fullscreen
music_btn.on_click = toggle_music
sound_btn.on_click = toggle_sound
sens_slider.on_value_changed = update_sensitivity
