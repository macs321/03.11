from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


App = QApplication([])

window = QWidget()


text= QLabel("Hello world")

line = QVBoxLayout()

line.addWidget(text)

window.setLayout(line)

window.show()

app.exec()
