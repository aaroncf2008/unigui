# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("UniGUI")
        Form.resize(972, 636)
        self.TabSystem = QtWidgets.QTabWidget(Form)
        self.TabSystem.setGeometry(QtCore.QRect(0, 0, 1001, 641))
        self.TabSystem.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TabSystem.setMouseTracking(False)
        self.TabSystem.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.TabSystem.setObjectName("TabSystem")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 10, 751, 341))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 580, 971, 31))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.TabSystem.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(410, 50, 70, 17))
        self.checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(410, 70, 70, 17))
        self.checkBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(410, 90, 70, 17))
        self.checkBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(410, 110, 70, 17))
        self.checkBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(410, 130, 70, 17))
        self.checkBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(410, 150, 70, 17))
        self.checkBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_6.setObjectName("checkBox_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(310, 10, 241, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.TabSystem.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 111, 581))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(850, 10, 111, 581))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.TabSystem.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.TabSystem.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TabSystem.setTabText(self.TabSystem.indexOf(self.tab_2), _translate("Form", "Terminal"))
        self.checkBox.setText(_translate("Form", "-p-"))
        self.checkBox_2.setText(_translate("Form", "-Pn"))
        self.checkBox_3.setText(_translate("Form", "-T4"))
        self.checkBox_4.setText(_translate("Form", "-sV"))
        self.checkBox_5.setText(_translate("Form", "-sC"))
        self.checkBox_6.setText(_translate("Form", "--open"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">nmap</span></p></body></html>"))
        self.TabSystem.setTabText(self.TabSystem.indexOf(self.tab), _translate("Form", "NMAP"))
        self.TabSystem.setTabText(self.TabSystem.indexOf(self.tab_3), _translate("Form", "NMAP Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
