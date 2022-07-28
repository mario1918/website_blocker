# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blocker.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


# Initialization
hostpath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

"""
# Reading from blacklisted sites and adding it into a list
# opening the file in read mode
my_file = open("block2.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
websites = data.split("\n")
#print(websites)
my_file.close()
"""
websites = ["www.xnxx.tv","www.xvideos2.com","www.xxx.com","www.ixxx.com","www.xnxx.com","www.xvideos.com","www.xvideos1.com","xvideosxnxx.org","www.pornhub.com","www.xxxbule.com","xnxxarabsex.com","sexalarab.com","www.xv-videos1.com","evexxx.com","ijavhd.com","www.xxxvideos247.com","xhamster.com","pornogramxxx.com","dewafilm.xyz","gizmoxxx.com","www.xxxlucah.com","ok.xxx","newsexxxx.com","bezsirot24.ru","theporndude.com","xnxx123.net","arbada.com",
            "youporn.com","spankbang.com","hot-sex-tube.com","www.milffox.com","www.arabxn.com","arbada.com",
            "gulfsexx.com", "www.arbada.com", "www.sexnarxnxx.com", "sex4arab.xxx", "trend-arabic.com", "zebawy.com", "pornogramxxx.com", "theporndude.com",
            "arabx.cam", "justporno.pro", "arabysexy.com", "aflamaljins.com", "arabysexy.mobi", "bezsirot24.ru"
            ,"gekso.org", "ar.selvagem.cyou", "arabsex1.com", "xxnxar.com", "kaskosv.com", "xnxxarab.cc", "bookmark.xxx", "kink.com", "YouJizz.com", "8Tube.xxx", "Redtube.com"]

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(547, 309)


        #Push Button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.block_it)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #5dc77a; border: 1px solid black; color: white")


        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 50, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Blocking button for blocking websites
    def block_it(self):
        flag = False
        def msgSuccess():
            # Message box of success
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting Message box window title
            msg.setWindowTitle("Success")

            # setting message for Message Box
            msg.setText("دلوقتي انت محمي من الصفحات المدمرة دي. Enjoy your life")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()

            print("Websites have been blocked successfully. ")

        def already():
            # Message box of success
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting Message box window title
            msg.setWindowTitle("You are already protected")

            # setting message for Message Box
            msg.setText("You are already protected and blocked from these websites")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()

        with open(hostpath, 'r+') as file:
            content = file.read()
            # Check if the user blocked these sites before or not

            for web in websites:
                if web in content:
                    break
                else:
                    file.write(redirect + " " + web + "\n")
                    flag = True

            if flag:
                msgSuccess()
            else:
                already()




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Blocker"))
        self.pushButton.setText(_translate("Dialog", "BLOCK"))
        self.label_4.setText(_translate("Dialog", "اهلاً، احنا فخورين بك و انت بتاخد الخطوة الرائعة دي"))
        self.label_5.setText(_translate("Dialog", " يلا دوس \'Block\'علشان نتخلص من الصفحات المدمرة دي"))
        self.label_6.setText(_translate("Dialog", "Hi, we are so proud of you for taking this awesome step."))
        self.label_7.setText(_translate("Dialog", "Yala click on \'BLOCK\' button to block these destructive websites"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

