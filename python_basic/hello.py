import sys
from PyQt5.QtWidgets import QApplication, QWidget
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())