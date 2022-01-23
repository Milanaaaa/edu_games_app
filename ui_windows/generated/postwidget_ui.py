# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PostWidget(object):
    def setupUi(self, PostWidget):
        PostWidget.setObjectName("PostWidget")
        PostWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(PostWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_author = QtWidgets.QLabel(PostWidget)
        self.lbl_author.setObjectName("lbl_author")
        self.horizontalLayout.addWidget(self.lbl_author)
        self.pb_edit = QtWidgets.QPushButton(PostWidget)
        self.pb_edit.setObjectName("pb_edit")
        self.horizontalLayout.addWidget(self.pb_edit)
        self.pb_delete = QtWidgets.QPushButton(PostWidget)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout.addWidget(self.pb_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tb_post_text = QtWidgets.QTextBrowser(PostWidget)
        self.tb_post_text.setObjectName("tb_post_text")
        self.verticalLayout.addWidget(self.tb_post_text)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_likes = QtWidgets.QLabel(PostWidget)
        self.lbl_likes.setObjectName("lbl_likes")
        self.horizontalLayout_2.addWidget(self.lbl_likes)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_like = QtWidgets.QPushButton(PostWidget)
        self.pb_like.setObjectName("pb_like")
        self.horizontalLayout_2.addWidget(self.pb_like)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PostWidget)
        QtCore.QMetaObject.connectSlotsByName(PostWidget)

    def retranslateUi(self, PostWidget):
        _translate = QtCore.QCoreApplication.translate
        PostWidget.setWindowTitle(_translate("PostWidget", "Frame"))
        self.lbl_author.setText(_translate("PostWidget", "TextLabel"))
        self.pb_edit.setText(_translate("PostWidget", "Редактировать"))
        self.pb_delete.setText(_translate("PostWidget", "Удалить"))
        self.lbl_likes.setText(_translate("PostWidget", "TextLabel"))
        self.pb_like.setText(_translate("PostWidget", "Нравится!"))
