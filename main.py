import os
import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.staric_api_server = "http://static-maps.yandex.ru/1.x/"
        self.lon = 37.530887
        self.lat = 55.703118
        self.delta = 0.002
        self.static_params = {
            "ll": f'{self.lon},{self.lat}',
            "spn": f'{self.delta},{self.delta}',
            "l": "map"
        }
        self.getImage()
        self.initUI()

    def getImage(self):
        response = requests.get(self.staric_api_server, params=self.static_params)

        if not response:
            print('Ошибка')
            print()
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        # Изображение
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.move_top()
        elif e.key() == Qt.Key_Down:
            self.move_button()
        elif e.key() == Qt.Key_Left:
            self.move_left()
        else:
            self.move_right()

    def move_top(self):
        try:
            self.lat += self.delta
            self.static_params = {
                "ll": f'{self.lon},{self.lat}',
                "spn": f'{self.delta},{self.delta}',
                "l": "map"
            }
            self.getImage()
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        except Exception:
            pass

    def move_button(self):
        try:
            self.lat -= self.delta
            self.static_params = {
                "ll": f'{self.lon},{self.lat}',
                "spn": f'{self.delta},{self.delta}',
                "l": "map"
            }
            self.getImage()
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        except Exception:
            pass

    def move_left(self):
        try:
            self.lon -= self.delta
            self.static_params = {
                "ll": f'{self.lon},{self.lat}',
                "spn": f'{self.delta},{self.delta}',
                "l": "map"
            }
            self.getImage()
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        except Exception:
            pass

    def move_right(self):
        try:
            self.lon += self.delta
            self.static_params = {
                "ll": f'{self.lon},{self.lat}',
                "spn": f'{self.delta},{self.delta}',
                "l": "map"
            }
            self.getImage()
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        except Exception:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
