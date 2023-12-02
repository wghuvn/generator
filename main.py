from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.btn_generate.clicked.connect(self.generate)

    def example(self):
        print(2)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()