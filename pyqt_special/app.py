# from PyQt6.QtWidgets import QApplication, QWidget
# import sys

# app = QApplication(sys.argv)

# window = QMainWindow("Push Me")
# window.show()

# app.exec()

#--------------------------Testint QPushButton ------------
# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton

# app = QApplication(sys.argv)

# window = QPushButton("Push Me")
# window.show()

# app.exec()

#-----------------------testing QMainWindow------------------
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow

# app = QApplication(sys.argv)

# window = QMainWindow()
# window.show()

# # Start the event loop.
# app.exec()

#------------------------------testing custom window---------------------
# import sys

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Ma fenêtre")
#         button = QPushButton("Press Me!")

#         # Set the central widget of the Window.
#         self.setCentralWidget(button)

# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()
#--------------------------testing resizable-------------------
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(800, 650)
        self.setMaximumSize(1920, 1080)

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()