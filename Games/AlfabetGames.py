import random

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QLabel, QGridLayout
from PyQt5 import QtCore

from ui_games.vow_con import Ui_Form_Vow_Con


class CorOrderGame(QWidget):
    game_closed = pyqtSignal()
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        self.balls = 0

    def initUI(self, args):
        self.setGeometry(410, 600, 410, 600)
        self.setWindowTitle('Буквы в правильном порядке')

        self.make_board()

    def make_board(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.orig_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.alphabet = [l for l in self.orig_alphabet]
        random.shuffle(self.alphabet)

        self.first_btn = None
        self.secnd_btn = None
        x, y = 1, 1
        self.alphabet_list = []
        for b in self.alphabet:
        #     if self.alphabet.index(b) == 29:
            self.letter_btn = QPushButton(b, self)
            self.letter_btn.resize(70, 70)
            self.letter_btn.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.letter_btn.clicked.connect(self.set_buttons)
            self.alphabet_list.append(self.letter_btn)
            self.grid.addWidget(self.letter_btn, x, y)
            y += 1
            if self.alphabet.index(b) % 3 == 2:
                x += 1
                y = 1



        self.check_btn = QPushButton('Готово', self)
        self.check_btn.resize(150, 70)
        self.grid.addWidget(self.check_btn, 12, 3)
        self.check_btn.setStyleSheet('QPushButton {background-color: violet; color: black;}')
        self.check_btn.clicked.connect(self.check_alphabet)

        self.lbl_cor = QLabel('              ', self)
        self.grid.addWidget(self.lbl_cor, 12, 1)
        # self.lbl_cor.move(50, 570)

    def set_buttons(self):
        if self.first_btn == None:
            self.first_btn = self.sender()
            self.first_btn.setStyleSheet('QPushButton {background-color: pink; color: white;}')
        elif self.first_btn != None and self.secnd_btn == None:
            self.secnd_btn = self.sender()
            FbtnText = self.first_btn.text()
            SbtnText = self.secnd_btn.text()
            self.first_btn.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.first_btn.setText(SbtnText)
            self.secnd_btn.setText(FbtnText)

            self.first_btn = None
            self.secnd_btn = None

    def check_alphabet(self):
        correct = True

        for i in range(len(self.alphabet)):
            if self.alphabet_list[i].text() != self.orig_alphabet[i]:
                correct = False
                break
        if correct:
            self.lbl_cor.setText('Верно')
            self.balls += 5
        else:
            self.lbl_cor.setText('Неверно')
            self.balls -= 5

    def closeEvent(self, event):
        self.game_closed.emit()


class VowConGame(QWidget, Ui_Form_Vow_Con):
    game_closed = pyqtSignal()

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.ost_alphabet = [l for l in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
        self.give_letter()
        self.make_board()

    def give_letter(self):
        if self.ost_alphabet:
            self.letter = random.choice(self.ost_alphabet)
            self.let_btn.setText(self.letter)
            # self.let_btn.setStyleSheet('QPushButton {background-color: None; color: black;}')
        else:
            self.lbl_won = QLabel(self, 'Молодец!')
            self.lbl_won.move()

    def make_board(self):
        self.balls = 0
        self.balls_btn.setStyleSheet('QPushButton {background-color: #fde910; color: black;}')

        self.ans_btn.clicked.connect(self.check)

    def check(self):
        if self.rb_glas.isChecked():
            if self.letter in 'ЁУЕЫАОЭЯИЮ':
                self.right_ans()
            else:
                self.wrong_ans()

        if self.rb_sogl.isChecked():
            if self.letter in 'ЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ':
                self.right_ans()
            else:
                self.wrong_ans()

        self.balls_btn.setText(str(self.balls))
        self.give_letter()

    def right_ans(self):
        self.let_btn.setStyleSheet('QPushButton {background-color: #98ff98; color: black;}')
        self.ost_alphabet.remove(self.letter)
        self.balls += 1

    def wrong_ans(self):
        self.let_btn.setStyleSheet('QPushButton {background-color: #ffa8af; color: black;}')
        self.balls -= 1

    def closeEvent(self, event):
        self.game_closed.emit()