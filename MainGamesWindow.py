import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from windows.LoginWindow import LoginWindow
from windows.RegisterWindow import RegisterWindow

from db.UsersDB import UsersDB

from Games.AlfabetGames import CorOrderGame
from Games.AlfabetGames import VowConGame
from Games.AccountGames import ASMDGame
from Games.AccountGames import CompareGame
from Games.WorldGames import NutrTupeGame

from ui_games.mainwindow import Ui_MainWindow


class MainGameWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = UsersDB()
        self.user = None

        self.lbl_login.hide()

        self.pb_logout.hide()

        self.lbl_login.hide()

        self.pb_login.clicked.connect(self.login)
        self.pb_register.clicked.connect(self.register)
        self.pb_logout.clicked.connect(self.logout)

        self.lbl_balls.hide()
        self.balls = 0

        self.lbl_alf.setStyleSheet("QLineEdit { background: pink; selection-background-color: black; }")
        self.lbl_sch.setStyleSheet("QLineEdit { background: #7fc7ff; selection-background-color: black; }")
        self.lbl_mir.setStyleSheet("QLineEdit { background: #8ccb5e; selection-background-color: black; }")

        self.btn_cor_ord.clicked.connect(self.open_cor_order_game)
        self.btn_vow_col.clicked.connect(self.open_glas_sogl_game)
        self.btn_ASMD.clicked.connect(self.open_asmd_game)
        self.btn_compare.clicked.connect(self.open_compare_game)
        self.btn_nutr.clicked.connect(self.open_nutr_type_game)
        self.pushButton.hide()

        self.user_game_balls = 0

        self.nutr_tp_gm = None
        self.asmd_gm = None
        self.compare_gm = None
        self.cor_ord_gm = None
        self.glas_sogl_gm = None

    def open_nutr_type_game(self):
        self.nutr_tp_gm = NutrTupeGame(self)
        self.nutr_tp_gm.game_closed.connect(self.addBalls)
        self.nutr_tp_gm.show()

    def open_asmd_game(self):
        self.asmd_gm = ASMDGame(self)
        self.asmd_gm.game_closed.connect(self.addBalls)
        self.asmd_gm.show()

    def open_compare_game(self):
        self.compare_gm = CompareGame(self)
        self.compare_gm.game_closed.connect(self.addBalls)
        self.compare_gm.show()

    def open_cor_order_game(self):
        self.cor_ord_gm = CorOrderGame(self)
        self.cor_ord_gm.game_closed.connect(self.addBalls)
        self.cor_ord_gm.show()

    def open_glas_sogl_game(self):
        self.glas_sogl_gm = VowConGame(self, '')
        self.glas_sogl_gm.game_closed.connect(self.addBalls)
        self.glas_sogl_gm.show()

    def login(self):
        login_window = LoginWindow()
        result = login_window.exec()
        if result == QDialog.Accepted:
            self.set_user(login_window.user)

    def register(self):
        register_window = RegisterWindow()
        result = register_window.exec()
        if result == QDialog.Accepted:
            self.set_user(register_window.user)

    def set_user(self, user):
        self.user = user
        self.user_game_balls = user.get_balls()

        self.lbl_login.setText(self.user.login)
        self.lbl_login.show()
        self.pb_logout.show()
        self.lbl_balls.show()
        self.lbl_balls.setText('Баллы: ' + str(user.get_balls()))
        self.pb_login.hide()
        self.pb_register.hide()

    def logout(self):
        self.lbl_login.hide()
        self.pb_logout.hide()
        self.pb_login.show()
        self.pb_register.show()
        self.lbl_balls.hide()

        conn = sqlite3.connect('db/UsersDB.db')
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE User
                        SET balls = {self.user_game_balls}
                        WHERE login = '{self.user.login}'""")
        conn.commit()

        self.user = None

    def addBalls(self):
        if self.user is not None:
            self.user_game_balls += self.sender().balls
            self.lbl_balls.setText('Баллы: ' + str(self.user_game_balls))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainGameWindow()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
