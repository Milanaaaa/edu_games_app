# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/regauthdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegAuthDialog(object):
    def setupUi(self, RegAuthDialog):
        RegAuthDialog.setObjectName("RegAuthDialog")
        RegAuthDialog.resize(263, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(RegAuthDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_login = QtWidgets.QLabel(RegAuthDialog)
        self.lbl_login.setObjectName("lbl_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_login)
        self.lbl_password = QtWidgets.QLabel(RegAuthDialog)
        self.lbl_password.setObjectName("lbl_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.le_login = QtWidgets.QLineEdit(RegAuthDialog)
        self.le_login.setObjectName("le_login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_login)
        self.le_password = QtWidgets.QLineEdit(RegAuthDialog)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_password)
        self.verticalLayout.addLayout(self.formLayout)
        self.lbl_error = QtWidgets.QLabel(RegAuthDialog)
        self.lbl_error.setText("")
        self.lbl_error.setWordWrap(True)
        self.lbl_error.setObjectName("lbl_error")
        self.verticalLayout.addWidget(self.lbl_error)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbOk = QtWidgets.QPushButton(RegAuthDialog)
        self.pbOk.setObjectName("pbOk")
        self.horizontalLayout.addWidget(self.pbOk)
        self.pbCancel = QtWidgets.QPushButton(RegAuthDialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout.addWidget(self.pbCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RegAuthDialog)
        QtCore.QMetaObject.connectSlotsByName(RegAuthDialog)

    def retranslateUi(self, RegAuthDialog):
        _translate = QtCore.QCoreApplication.translate
        RegAuthDialog.setWindowTitle(_translate("RegAuthDialog", "Dialog"))
        self.lbl_login.setText(_translate("RegAuthDialog", "Логин"))
        self.lbl_password.setText(_translate("RegAuthDialog", "Пароль"))
        self.pbOk.setText(_translate("RegAuthDialog", "Ok"))
        self.pbCancel.setText(_translate("RegAuthDialog", "Отмена"))
