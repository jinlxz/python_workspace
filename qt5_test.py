from PyQt5 import QtCore, QtWidgets
import sys
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.resize(500,300)
        self.move(200,200)
        self.setWindowTitle("中文测试")
        label=QtWidgets.QLabel("hahaha",self)
        label.move(20,10)
        #label.move()
        btnExit=QtWidgets.QPushButton("Exit(&C)",self)
        btnExit.move(80,10)
        btnExit.clicked.connect(self.btnClicked)
        #btnExit.
        self.show()
    def btnClicked(self):
        self.closeEvent()
    def closeEvent(self, QCloseEvent):
        from PyQt5.QtWidgets import QMessageBox
        answer=QMessageBox.question(self,'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__=="__main__":
    app=QtWidgets.QApplication(["hello world."])
    widget=MyWidget()
    sys.exit(app.exec_())