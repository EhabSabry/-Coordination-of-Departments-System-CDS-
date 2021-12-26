

from PyQt5 import QtCore, QtGui, QtWidgets 
import mysql.connector as mc


class Ui_Form_3(object):
    def insert_data1(self):
        try:
            mydb = mc.connect(host="localhost",user="root",password="",database="fci")
            mycursor = mydb.cursor()
            name = self.lineEdit.text()
            email = self.lineEdit_2.text()
            address = self.lineEdit_3.text()
            phone = self.lineEdit_4.text()
            age = self.lineEdit_5.text()
            gpa = self.lineEdit_6.text()
            query = "INSERT INTO cs(Name, Email, Address, Phone, age, GPA) VALUES (%s,%s,%s,%s,%d,%d)"
            value = (name,email,address,phone,age,gpa)
            mycursor.execute(query,value)
            mydb.commit()
        
        
        
        except mc.Error as e:
            print("Error inserting")
    def setupUi(self, Form_3):
        Form_3.setObjectName("Form_3")
        Form_3.resize(1096, 831)
        self.pushButton_13 = QtWidgets.QPushButton(Form_3)
        self.pushButton_13.setGeometry(QtCore.QRect(740, 630, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form_3)
        self.pushButton_14.setGeometry(QtCore.QRect(70, 640, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.insert_data1)
        self.pushButton_12 = QtWidgets.QPushButton(Form_3)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 440, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(Form_3)
        self.pushButton_11.setGeometry(QtCore.QRect(740, 440, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_1 = QtWidgets.QLabel(Form_3)
        self.label_1.setGeometry(QtCore.QRect(-90, 30, 851, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_1.setObjectName("label_1")
        self.label = QtWidgets.QLabel(Form_3)
        self.label.setGeometry(QtCore.QRect(770, 560, 141, 31))
        self.label.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_3)
        self.label_2.setGeometry(QtCore.QRect(70, 570, 141, 31))
        self.label_2.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_3)
        self.label_3.setGeometry(QtCore.QRect(90, 760, 141, 31))
        self.label_3.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form_3)
        self.label_4.setGeometry(QtCore.QRect(770, 750, 141, 31))
        self.label_4.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form_3)
        self.lineEdit.setGeometry(QtCore.QRect(270, 140, 641, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 190, 641, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 240, 641, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 290, 641, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 340, 641, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(270, 390, 641, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(Form_3)
        self.label_8.setGeometry(QtCore.QRect(100, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("Color: rgba(0, 135, 141, 1)\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form_3)
        self.label_7.setGeometry(QtCore.QRect(100, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("Color: rgba(0, 135, 141, 1)\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Form_3)
        self.label_5.setGeometry(QtCore.QRect(100, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("Color: rgba(0, 135, 141, 1)\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form_3)
        self.label_6.setGeometry(QtCore.QRect(100, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("Color: rgba(0, 135, 141, 1)\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Form_3)
        self.label_9.setGeometry(QtCore.QRect(110, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("Color: rgba(0, 135, 141, 1)\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form_3)
        self.label_10.setGeometry(QtCore.QRect(110, 390, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("Color: rgba(0, 135, 141, 1)\n"
"")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form_3)
        QtCore.QMetaObject.connectSlotsByName(Form_3)

    def retranslateUi(self, Form_3):
        _translate = QtCore.QCoreApplication.translate
        Form_3.setWindowTitle(_translate("Form_3", "Form"))
        self.pushButton_13.setText(_translate("Form_3", "IT"))
        self.pushButton_14.setText(_translate("Form_3", "IS"))
        self.pushButton_12.setText(_translate("Form_3", "CS"))
        self.pushButton_11.setText(_translate("Form_3", "SE"))
        self.label_1.setText(_translate("Form_3", "الرغبة الاولي"))
        self.label.setText(_translate("Form_3", "<html><head/><body><p><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>"))
        self.label_2.setText(_translate("Form_3", "<html><head/><body><p><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>"))
        self.label_3.setText(_translate("Form_3", "<html><head/><body><p><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>"))
        self.label_4.setText(_translate("Form_3", "<html><head/><body><p><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>"))
        self.label_8.setText(_translate("Form_3", "name"))
        self.label_7.setText(_translate("Form_3", "email"))
        self.label_5.setText(_translate("Form_3", "address"))
        self.label_6.setText(_translate("Form_3", "phone"))
        self.label_9.setText(_translate("Form_3", "age"))
        self.label_10.setText(_translate("Form_3", "GPA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_3 = QtWidgets.QWidget()
    ui = Ui_Form_3()
    ui.setupUi(Form_3)
    Form_3.show()
    sys.exit(app.exec_())
