from PyQt5.QtWidgets import QDialog

from db.UsersDB import UsersDB
from db.exceptions import UserNotRegistered, PasswordIsWrong
from ui_windows.generated.regauthdialog_ui import Ui_RegAuthDialog


class LoginWindow(QDialog, Ui_RegAuthDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.db = UsersDB()
        self.user = None

        self.pbOk.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)

        self.setWindowTitle('Вход')
        self.pbOk.setText('Войти')


    def login(self):
        login = self.le_login.text()
        password = self.le_password.text()

        try:
            self.user = self.db.authenticate(login, password)
            self.accept()
        except UserNotRegistered as e:
            self.lbl_error.setText(str(e))
        except PasswordIsWrong as e:
            self.lbl_error.setText(str(e))