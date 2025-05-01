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
        self.radiobutton_is_selected() checks if a radio button is selected
        self.check_id() checks if the ID is a duplicate or not a number, and if it
        is it will return True causing the code not to continue
        """
        if (self.radiobutton_is_selected()):
            if(self.check_id() == False):
                self.record_vote()
                self.ui.label_already_voted.setText("Voted!!")
                self.clear_app()

    def radiobutton_is_selected(self):
        """
        If either radio button is selected
        :return: True

        If both radio buttons are not selected then
        already voted label changes to Must select one
        :return: False
        """
        if self.ui.radiobutton_carson.isChecked() or self.ui.radiobutton_john.isChecked():
            return True
        else:
            self.ui.label_already_voted.setText("Must select one")
            return False

    def clear_app(self):
        """
        clears the textedit

        :arg: rb in [a,b]
        unselected both radio buttons
        """
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
        """
        :param: voter_id if that is a digit then it creates either a new file if there 
        isnt one or it reads a file and decides if it is a dupliccate or not
        the else just returns True because it is a letter 
        :return: returns True if there is a duplicate or if the input is not a decimal
        """

        if voter_id.isdigit():
            self.ui.label.setText("")
            try:
                with open(filename, 'r', newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if int(voter_id) == int(row[0]):
                            self.ui.label_already_voted.setText("Already Voted")
                            self.ui.label.setText(" ")
                            return True

                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([int(voter_id)])
                    return False

            except FileNotFoundError:
                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([int(voter_id)])
                    return False
        else:
            self.ui.label.setText("Enter a \n number")
            return True



