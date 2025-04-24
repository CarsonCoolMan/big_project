from gui import *
from PyQt6.QtWidgets import QApplication, QDialog
import sys

class VoteApp(QDialog):
    def __init__(self):
        super().__init__()
        """
        Sets the object UI_Vote_Menu to self.ui
        sets up the window
        """
        self.ui = Ui_Vote_Menu()
        self.ui.setupUi(self)

        """
        connects all the buttons to the vote methods
        that then change the selected label to the 
        selected candadit
        """
        self.ui.vote_carson.clicked.connect(self.vote_carson)
        self.ui.vote_george.clicked.connect(self.vote_george)
        self.ui.vote_abraham.clicked.connect(self.vote_abraham)

        """
        :param: self.selected is set to nobody selected in
        order to not cause error when nobody is selected
        """
        self.selected = "Nobody Selected"
        """
        once the vote button is selected it changed whatever 
        vote_label it is assiciated with to plus one of the 
        original value
        """
        self.ui.Vote_button.clicked.connect(self.vote_select)
    def vote_carson(self):
        self.selected = "Carson"
        self.ui.selection_label.setText("Selected: Carson")

    def vote_george(self):
        self.selected = "George"
        self.ui.selection_label.setText("Selected: George")

    def vote_abraham(self):
        self.selected = "Abraham"
        self.ui.selection_label.setText("Selected: Abraham")

    def vote_select(self):
        print(self.selected)
        if self.selected == "Carson":
            total = int(self.ui.vote_count_carson.text())
            self.ui.vote_count_carson.setText(str(total + 1))
        elif self.selected == "George":
            total = int(self.ui.vote_count_george.text())
            self.ui.vote_count_george.setText(str(total + 1))
        elif self.selected == "Abraham":
            total = int(self.ui.vote_count_abraham.text())
            self.ui.vote_count_abraham.setText(str(total + 1))
        self.check_winner()
    def check_winner(self):
        print(self.ui.winner_label.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = VoteApp()
    dialog.show()
    sys.exit(app.exec())
