from PyQt5.QtWidgets import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(0,0,0,0)
        self.setFixedSize(300, 200)
        self.lb = QLabel("I Love Pythin", self)
        self.lb.move(15, 15)

    
def window():
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()