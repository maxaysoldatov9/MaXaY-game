from ursina import *

class LoadingScreen(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, enabled=False, **kwargs)

        # Полупрозрачный фон сзади
        self.bg = Entity(
            parent=self,
            model='quad',
            texture='image/loading_bg.jpg',
            scale=(2, 1),
            color=color.rgba(0, 0, 0, 0),
            z=-1
        )

        # Текст и индикатор точек спереди
        self.text = Text("Загрузка", parent=self, y=0.1, scale=2, color=color.white, z=1)
        self.dots = Text("", parent=self, y=-0.05, scale=1.5, color=color.azure, z=1)
        
        # Простая полоска прогресса (для живости)
        self.progress_bg = Entity(parent=self, model='quad', color=color.rgba(255, 255, 255, 40),
                                  scale=(0.6, 0.03), y=-0.2, z=1)
        self.progress_fill = Entity(parent=self, model='quad', color=color.azure,
                                    scale=(0.0, 0.03), y=-0.2, x=-0.3, origin_x=-0.5, z=2)

        self._dot_index = 0
        self._running = False
        self._progress = 0.0

    def _animate_dots(self):
        if not self._running:
            return
        self._dot_index = (self._dot_index + 1) % 4
        self.dots.text = "." * self._dot_index
        invoke(self._animate_dots, delay=0.5)

    def _animate_progress(self):
        if not self._running:
            return
        # Плавное заполнение до 100% за ~3 сек (регулируется шагом)
        self._progress = min(1.0, self._progress + 0.04)
        self.progress_fill.scale_x = 0.6 * self._progress
        self.progress_fill.x = -0.3 + (0.3 * self._progress)
        if self._progress < 1.0:
            invoke(self._animate_progress, delay=0.12)

    def show(self, duration=1.0):
        self.enabled = True
        self._running = True
        self._progress = 0.0

        # Фон плавно затемняется, но остаётся полупрозрачным
        self.bg.animate_color(color.rgba(0, 0, 0, 255), duration=duration)
        self._animate_dots()
        self._animate_progress()

    def hide(self, callback=None, duration=1.0):
        # Останавливаем анимации и плавно убираем фон
        self._running = False
        self.bg.animate_color(color.rgba(0, 0, 0, 0), duration=duration)
        invoke(self._finish_hide, delay=duration, callback=callback)

    def _finish_hide(self, callback=None):
        self.enabled = False
        if callback:
            callback()
