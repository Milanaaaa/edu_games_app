# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compare.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Compare(object):
    def setupUi(self, Form):
        Form.setObjectName("Сравнение")
        Form.resize(395, 189)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(3, 0, 381, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_otr = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_otr.setObjectName("cb_otr")
        self.horizontalLayout.addWidget(self.cb_otr)
        self.cb_drb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_drb.setObjectName("cb_drb")
        self.horizontalLayout.addWidget(self.cb_drb)
        self.pb_make = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_make.setObjectName("pb_make")
        self.horizontalLayout.addWidget(self.pb_make)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_1.setObjectName("le_1")
        self.horizontalLayout_2.addWidget(self.le_1)
        self.pb_choice = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_choice.setObjectName("pb_choice")
        self.horizontalLayout_2.addWidget(self.pb_choice)
        self.le_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_2.setObjectName("le_2")
        self.horizontalLayout_2.addWidget(self.le_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pb_ans = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_ans.setObjectName("pb_ans")
        self.horizontalLayout_3.addWidget(self.pb_ans)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pb_balls = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_balls.setObjectName("pb_balls")
        self.horizontalLayout_3.addWidget(self.pb_balls)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Сравнение"))
        self.cb_otr.setText(_translate("Form", "Отрицательные числа"))
        self.cb_drb.setText(_translate("Form", "Дробные числа"))
        self.pb_make.setText(_translate("Form", "Составить"))
        self.pb_choice.setText(_translate("Form", ">"))
        self.pb_ans.setText(_translate("Form", "Ответить"))
        self.label.setText(_translate("Form", "Баллы: "))
        self.pb_balls.setText(_translate("Form", "0"))
