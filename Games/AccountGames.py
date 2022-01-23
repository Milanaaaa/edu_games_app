import random

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from ui_games.asmd import Ui_Form_ASMD
from ui_games.compare import Ui_Form_Compare


class ASMDGame(QWidget, Ui_Form_ASMD):
    game_closed = pyqtSignal()
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        # self.initUI(self)

        self.pb_make.clicked.connect(self.make_example)
        self.pb_answer.clicked.connect(self.check_ans)

        self.pb_balls.setStyleSheet('QPushButton {background-color: #fde910; color: black;}')
        self.balls = 0
        self.pb_balls.setText(str(self.balls))

    def make_example(self):
        self.znak = '+'
        self.nums = [str(random.randint(3, 25)) for i in range(int(self.spinBox.value()))]
        if self.rb_slozh.isChecked():
            self.znak = '+'
        elif self.rb_vych.isChecked():
            self.znak = '-'
        elif self.rb_umn.isChecked():
            self.znak = '*'
        elif self.rb_del.isChecked():
            self.znak = '/'

        self.example = self.znak.join(self.nums)
        self.lineEdit.setText(self.example)

    def check_ans(self):
        if self.lineEdit_2.text().isdigit():
            if round(eval(self.lineEdit.text()), 1) == float(self.lineEdit_2.text()):
                self.lineEdit_2.setStyleSheet("QLineEdit { background: #98ff98; selection-background-color: black; }")
                self.balls += 1
            else:
                self.lineEdit_2.setStyleSheet("QLineEdit { background: #ffa8af; selection-background-color: black; }")
                self.balls -= 1
        self.pb_balls.setText(str(self.balls))

    def closeEvent(self, event):
        self.game_closed.emit()


class CompareGame(QWidget, Ui_Form_Compare):
    game_closed = pyqtSignal()
    def __init__(self, *args):
        super().__init__()

        self.setupUi(self)
        self.initUI(args)

    def initUI(self, args):
        self.balls = 0

        self.pb_make.setStyleSheet('QPushButton {background-color: violet; color: black;}')
        self.pb_make.clicked.connect(self.make)

        self.pb_choice.setStyleSheet('QPushButton {background-color: pink; color: black;}')
        self.pb_choice.clicked.connect(self.change_znak)

        self.pb_ans.clicked.connect(self.check)

        self.pb_balls.setStyleSheet('QPushButton {background-color: #fde910; color: black;}')

    def make(self):
        diap = 80
        lev_gr = 0

        if self.cb_otr.isChecked() is True:
            lev_gr = -80
        prav_gran = lev_gr + diap

        if self.cb_drb.isChecked() is True:
            f = round(random.uniform(lev_gr, prav_gran), 1)
            s = round(random.uniform(lev_gr, prav_gran), 1)
        else:
            f = random.randint(lev_gr, prav_gran)
            s = random.randint(lev_gr, prav_gran)

        self.le_1.setText(str(f))
        self.le_2.setText(str(s))
        self.le_1.setStyleSheet("QLineEdit { background: white; selection-background-color: black; }")
        self.le_2.setStyleSheet("QLineEdit { background: white; selection-background-color: black; }")

    def change_znak(self):
        if self.pb_choice.text() == '=':
            self.pb_choice.setText('>')
        elif self.pb_choice.text() == '>':
            self.pb_choice.setText('<')
        elif self.pb_choice.text() == '<':
            self.pb_choice.setText('=')

    def check(self):
        if float(self.le_1.text()) == float(self.le_2.text()) and self.pb_choice.text() == '=':
            self.correct_ans()
        elif float(self.le_1.text()) > float(self.le_2.text()) and self.pb_choice.text() == '>':
            self.correct_ans()
        elif float(self.le_1.text()) < float(self.le_2.text()) and self.pb_choice.text() == '<':
            self.correct_ans()
        else:
            self.le_1.setStyleSheet("QLineEdit { background: #ffa8af; selection-background-color: black; }")
            self.le_2.setStyleSheet("QLineEdit { background: #ffa8af; selection-background-color: black; }")
            self.balls -= 1

        self.pb_balls.setText(str(self.balls))


    def correct_ans(self):
        self.le_1.setStyleSheet("QLineEdit { background: #98ff98; selection-background-color: black; }")
        self.le_2.setStyleSheet("QLineEdit { background: #98ff98; selection-background-color: black; }")
        self.balls += 1

    def closeEvent(self, event):
        self.game_closed.emit()