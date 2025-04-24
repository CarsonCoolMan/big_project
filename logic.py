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
        self.update_winner()

    def update_winner(self):
        count_carson = int(self.ui.vote_count_carson.text())
        count_george = int(self.ui.vote_count_george.text())
        count_abraham = int(self.ui.vote_count_abraham.text())

        if count_carson == count_george == count_abraham:
            self.ui.winner_label.setText("Winner: All Tie")
        elif count_carson > count_george and count_carson > count_abraham:
            self.ui.winner_label.setText("Winner: Carson")
        elif count_george > count_carson and count_george > count_abraham:
            self.ui.winner_label.setText("Winner: George")
        elif count_abraham > count_george and count_abraham > count_carson:
            self.ui.winner_label.setText("Winner: Abraham")
        elif count_carson == count_george:
            self.ui.winner_label.setText("Winner: Carson & George Tie")
        elif count_carson == count_abraham:
            self.ui.winner_label.setText("Winner: Carson & Abraham Tie")
        elif count_george == count_abraham:
            self.ui.winner_label.setText("Winner: George & Abraham Tie")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = VoteApp()
    dialog.show()
    sys.exit(app.exec())
