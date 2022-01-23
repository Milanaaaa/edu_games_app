import random
import sqlite3
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from ui_games.nutr_type import Ui_Form_Nutr

from db.AnimalsDB import AnimalsDB


class NutrTupeGame(QWidget, Ui_Form_Nutr, AnimalsDB):
    game_closed = pyqtSignal()

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.initUI(self)

    def initUI(self, args):
        self.setWindowTitle('Животные по типу питания')

        self.pb_next = QPushButton(self)
        self.pb_next.setText('Дальше')
        self.pb_next.move(435, 510)
        self.pb_next.clicked.connect(self.load_image)
        self.pushButton.setStyleSheet('QPushButton {background-color: #fde910; color: black;}')

        self.balls = 0
        self.pb_ans.clicked.connect(self.check)

        self.pushButton.setText(str(self.balls))

        self.load_image()

        self.update()

    def load_image(self):
        self.pb_ans.setStyleSheet('QPushButton {background-color: None; color: black;}')
        image = QImage.fromData(self.get_image())
        pixmap = QPixmap.fromImage(image)

        self.label.setPixmap(pixmap.scaled(500, 500, Qt.KeepAspectRatio))
        self.label.resize(200, 200)

    def check(self):
        if self.rb_rast.isChecked():
            self.chosen_type = 'Растительноядные'
        elif self.rb_nasek.isChecked():
            self.chosen_type = 'Насекомоядные'
        elif self.rb_hish.isChecked():
            self.chosen_type = 'Хищники'
        elif self.rb_vse.isChecked():
            self.chosen_type = 'Всеядные'

        if self.check_type(self.chosen_type):
            self.pb_ans.setStyleSheet('QPushButton {background-color: #98ff98; color: black;}')
            self.balls += 1
        else:
            self.pb_ans.setStyleSheet('QPushButton {background-color: #ffa8af; color: black;}')
            self.balls -= 1

    def closeEvent(self, event):
        self.game_closed.emit()
