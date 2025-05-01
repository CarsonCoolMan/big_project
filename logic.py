from gui import *
from PyQt6.QtWidgets import QApplication, QDialog
import csv
import sys
import os

"""
put ID as said in minimum video
"""
class VotingApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.button_vote.clicked.connect(self.handle_vote)

    def handle_vote(self):
        """
        resets all the values if true
        """
        if(self.check_id() == False):
            self.record_vote()
            self.ui.label_already_voted.setText("Voted!!")

            self.ui.textedit_id.clear()

            for rb in [self.ui.radiobutton_carson, self.ui.radiobutton_john]:
                rb.setAutoExclusive(False)
                rb.setChecked(False)
                rb.setAutoExclusive(True)

    def record_vote(self):
        voter_id = self.ui.textedit_id.toPlainText()

        if self.ui.radiobutton_carson.isChecked():
            selected_vote = "carson"
        elif self.ui.radiobutton_john.isChecked():
            selected_vote = "john"
        else:
            selected_vote = "none"

        filename = "voting_logs.csv"

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, selected_vote])

    def check_id(self):
        voter_id = self.ui.textedit_id.toPlainText()
        filename = 'id_log.csv'
        duplicate_or_letter = False
        """
        :param: duplicate_or_letter is switched to true if it 
        is a duplicate or letter 
        this first round of open tests if it is a 
        duplicate or a letter
        it sets the label to must be a number if it 
        is not a number
        if it is a number it sets it to " " in order to 
        get rid of the label
        """
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if int(voter_id) == int(row[0]):
                        duplicate_or_letter = True
                        self.ui.label_already_voted.setText("Already Voted")
                        self.ui.label.setText(" ")
        except FileNotFoundError:
            with open(filename, 'w', newline='') as file:
                pass
        except Exception:
            duplicate_or_letter = True
            self.ui.label.setText(" ")
            self.ui.label_already_voted.setText(" ")
            self.ui.label.setText("Must be \n a number")
        """
        :param: voter_id is just the id text
        this is going to add the id too the csv file
        if it isnt already in there
        """
        try:
            if duplicate_or_letter == False:
                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([int(voter_id)])
        except Exception:
            duplicate_or_letter = True
            self.ui.label.setText(" ")
            self.ui.label_already_voted.setText(" ")
            self.ui.label.setText("Must be \n a number")
        return duplicate_or_letter


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec())
