from PyQt5.QtWidgets import QDialog

from db.UsersDB import UsersDB
from db.exceptions import LoginAlreadyInUse
from ui_windows.generated.regauthdialog_ui import Ui_RegAuthDialog


class RegisterWindow(QDialog, Ui_RegAuthDialog):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setupUi(self)

        self.db = UsersDB()
        self.user = None

        self.pbOk.clicked.connect(self.register)
        self.pbCancel.clicked.connect(self.reject)

        self.setWindowTitle('Регистрация')
        self.pbOk.setText('Зарегистрироваться')

    def register(self):
        login = self.le_login.text()
        password = self.le_password.text()

        try:
            self.user = self.db.register(login, password)
            self.accept()
        except LoginAlreadyInUse as e:
            self.lbl_error.setText(str(e))
