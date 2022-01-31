import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

import requestMaking

SCREEN_SIZE = [600, 450]
ZOOM = 2
TYPE = 'map'
COORDS = '37.530887 55.703118'


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.getImage()
        self.initUI()

    def getImage(self):
        response = requestMaking.Make_Map_Request(COORDS.split(), ZOOM, TYPE)

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
        global ZOOM
        if e.key() == Qt.Key_PageUp and ZOOM < 17:
            ZOOM += 1
        elif e.key() == Qt.Key_PageDown and ZOOM > 2:
            ZOOM -= 1
        self.update()

    def update(self):
        self.getImage()
        self.pixmap = QPixmap(self.map_file)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
