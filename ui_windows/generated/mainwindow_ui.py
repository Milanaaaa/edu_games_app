# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setObjectName("lbl_login")
        self.horizontalLayout.addWidget(self.lbl_login)
        self.pb_login = QtWidgets.QPushButton(self.centralwidget)
        self.pb_login.setObjectName("pb_login")
        self.horizontalLayout.addWidget(self.pb_login)
        self.pb_register = QtWidgets.QPushButton(self.centralwidget)
        self.pb_register.setObjectName("pb_register")
        self.horizontalLayout.addWidget(self.pb_register)
        self.pb_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pb_logout.setEnabled(True)
        self.pb_logout.setObjectName("pb_logout")
        self.horizontalLayout.addWidget(self.pb_logout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layout_scrollarea = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout_scrollarea.setObjectName("layout_scrollarea")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pb_post = QtWidgets.QPushButton(self.centralwidget)
        self.pb_post.setEnabled(False)
        self.pb_post.setObjectName("pb_post")
        self.verticalLayout.addWidget(self.pb_post)
        self.pb_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pb_refresh.setObjectName("pb_refresh")
        self.verticalLayout.addWidget(self.pb_refresh)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мини-твиттер"))
        self.lbl_login.setText(_translate("MainWindow", "Login"))
        self.pb_login.setText(_translate("MainWindow", "Войти"))
        self.pb_register.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pb_logout.setText(_translate("MainWindow", "Выйти"))
        self.pb_post.setText(_translate("MainWindow", "Сделать запись"))
        self.pb_refresh.setText(_translate("MainWindow", "Обновить"))
