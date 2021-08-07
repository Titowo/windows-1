import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('App name LOL')
window.setGeometry(100, 100, 200, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello world!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())