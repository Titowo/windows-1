import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import QVBoxLayout
# from PyQt5.QtWidgets import QHBoxLayout
# from PyQt5.QtWidgets import QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('App name LOL')

# LAYOUT HORIZONTAL
# layout = QHBoxLayout()
# layout.addWidget(QPushButton('Left'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Right'))
# window.setLayout(layout)

# LAYOUT VERTICAL
# layoutV = QVBoxLayout()
# layoutV.addWidget(QPushButton('Top'))
# layoutV.addWidget(QPushButton('Center'))
# layoutV.addWidget(QPushButton('Bot'))
# window.setLayout(layoutV)

window.show()
sys.exit(app.exec_())