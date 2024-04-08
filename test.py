from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class PianoApp(App):
    def build(self):
        # Создаем основной контейнер, в котором будут два больших контейнера
        main_layout = BoxLayout(orientation='horizontal')

        # Создаем контейнер для кнопок
        button_layout = BoxLayout(orientation='vertical')

        # Создаем контейнер для слайдера и надписи
        slider_layout = BoxLayout(orientation='vertical')

        # Создаем надпись для слайдера
        label = Label(text="Громкость", font_size=20, size_hint=(None, None), size=(dp(200), dp(50)), halign='center', valign='middle')

        # Создаем вертикальный слайдер
        slider = Slider(min=0, max=100, value=50, orientation='vertical')

        # Добавляем надпись и слайдер в контейнер слайдера
        slider_layout.add_widget(label)
        slider_layout.add_widget(slider)

        # Оставляем существующие кнопки на своих местах
        for i in range(1, 16):
            button = Button(text=str(i), font_size=40)
            button_layout.add_widget(button)

        # Добавляем контейнеры в основной контейнер
        main_layout.add_widget(button_layout)
        main_layout.add_widget(slider_layout)

        return main_layout

if __name__ == "__main__":
    PianoApp().run()
