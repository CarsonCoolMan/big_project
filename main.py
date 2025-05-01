from PyQt6.QtWidgets import QApplication, QDialog
import sys
from logic import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec())
