from PyQt5 import QtCore, QtWidgets
import sys,os.path
from PyQt5 import QtGui
class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.docmodified=False
        self.doc_name="Untitled doc"
    def open_newfile_slot(self):
        filename,_=QtWidgets.QFileDialog(self,QtCore.Qt.Dialog)\
            .getOpenFileName(self,"Open a new file",'.','*.py')
        if filename!="":
            #self.label.setText("you have selected file :"+filename)
            QtWidgets.QMessageBox.information(self,"信息","您选择了文件:"+filename)
            self.statusBar().showMessage("Selected file: "+filename)
    def create_newfile(self):
        pass
    def write_file_content(self,filename,content):
        if os.path.isfile(filename):
            filemode='r+'
        else:
            filemode="w+"
        with open(filename,filemode, encoding='utf-8') as f:
            f.write(content)
    def save_file(self):
        if self.docmodified:
            doc_content = self.textEdit.toPlainText()
            if os.path.isfile(self.doc_name):
                self.write_file_content(self.doc_name,doc_content)
                self.docmodified=False
                self.setWindowTitle(self.doc_name)
            else:
                fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", ".",
                                                  "C/C++ Files (*.c *.cpp *.cxx);;C/C++ Header Files (*.h);;All Files (*)")
                if fileName:
                    self.doc_name=fileName
                    self.write_file_content(self.doc_name,doc_content)
                    self.docmodified=False
                    self.setWindowTitle(self.doc_name)
    def init_menus(self):
        ###########build menus##########
        self.menuBar = self.menuBar()
        menu_file = QtWidgets.QMenu("&File", self.menuBar)
        menu_edit = QtWidgets.QMenu("&Edit", self.menuBar)
        ###
        menu_file.addAction("&Open File", self.open_newfile_slot, "Ctrl+O")
        # menu_file_newfile=menu_file.addAction("&Open File",self,self.open_newfile_slot,"Ctrl+O")
        menu_file.addAction("&New File...", self.create_newfile, "Ctrl+N")
        menu_file.addAction("&Save", self.save_file, "Ctrl+S")
        menu_file.addSeparator()
        menu_file.addAction("&Exit", QtWidgets.qApp.exit, "Ctrl+E")
        # menu_file_save=QtWidgets.QMenu("&Save...",self.menuBar)
        # menu_file_saveas=QtWidgets.QMenu("Save As...",self.menuBar)
        menu_edit.addAction("About Qt",QtWidgets.QApplication.aboutQt)
        self.menuBar.addMenu(menu_file)
        self.menuBar.addMenu(menu_edit)
    def init_toolbars(self):
        ###build toolbar
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)
        actionExit = QtWidgets.QAction(QtGui.QIcon("exits.png"), "Exit", self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.toolbar.addAction(actionExit)
    def textchanged(self):
        self.docmodified=True
        self.setWindowTitle(self.doc_name+"*")
    def init_mainframe(self):
        self.mainframe=QtWidgets.QFrame(self)
        top_vbox_layout = QtWidgets.QVBoxLayout()
        bottom_hbox_layout = QtWidgets.QHBoxLayout()
        #top_vbox_layout.addWidget(bottom_hbox_layout)
        top_vbox_layout.addLayout(bottom_hbox_layout)
        self.textEdit=QtWidgets.QTextEdit(self)
        top_vbox_layout.addWidget(self.textEdit,1)
        self.textEdit.textChanged.connect(self.textchanged)
        #top_vbox_layout.setStretchFactor(textEdit,100)
        self.label = QtWidgets.QLabel("hahaha", self)
        btnExit = QtWidgets.QPushButton("Exit(&C)", self)
        btnExit.clicked.connect(self.btnClicked)

        bottom_hbox_layout.addWidget(self.label)
        bottom_hbox_layout.addWidget(btnExit)
        bottom_hbox_layout.addStretch(1)
        self.mainframe.setLayout(top_vbox_layout)
        self.setCentralWidget(self.mainframe)
    def initUi(self):
        self.resize(1200,800)
        self.setWindowTitle("中文测试")
        self.doc_name=self.windowTitle()
        self.init_menus()
        self.init_toolbars()
        self.init_mainframe()
        fr=self.frameGeometry()
        qp=QtWidgets.QDesktopWidget().availableGeometry().center()
        fr.moveCenter(qp)
        self.move(fr.topLeft())
        self.statusBar().showMessage("Ready")
        #self.statusBar().show()
        self.show()
    def btnClicked(self):
        fr = self.frameGeometry()
        qp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fr.moveCenter(qp)
        self.move(fr.topLeft())
        self.label.setText("you have selected file :")
    def closeEvent(self, QCloseEvent):
        from PyQt5.QtWidgets import QMessageBox
        if self.docmodified:
            answer=QMessageBox.question(self,'Message', "The document has been modified, do you want to save it?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer==QMessageBox.Yes:
                QCloseEvent.ignore()
                #QCloseEvent.accept()
            else:
                QCloseEvent.accept()

if __name__=="__main__":
    app=QtWidgets.QApplication(["hello world."])
    widget=MyWidget()
    sys.exit(app.exec_())