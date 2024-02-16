import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from qt_material import apply_stylesheet

def show_warning():
    app = QApplication(sys.argv)
    window = QMainWindow()


    # Create a warning label
    warning_label = QLabel("Conference Calls Not Allowed",window)
    warning_label.setGeometry(50, 50, 300, 50)  # Adjust label position and size

    # Increase font size
    font = QFont("Arial", 100)  # Set font family and size
    warning_label.setFont(font)

    # Increase window size
    window.setGeometry(100, 100, 400, 200)  # Set window dimensions (x, y, width, height)
    apply_stylesheet(app, theme='dark_teal.xml')  # Apply the Material dark theme
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    show_warning()
