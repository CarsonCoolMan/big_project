from gui import *
from PyQt6.QtWidgets import QApplication, QDialog
import csv
import sys
import os

class VotingApp(QDialog):
    """
    APP that allows users to enter a voter ID and
    select a candidate using radio buttons and click
    the vote button to vote
    """
    def __init__(self):
        """
        Initializes the VotingApp Dialog
        sets up the UI and connects
        the vote button the the handle_vote
        function
        """
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        self.ui.textedit_id.textChanged.connect(self.clear_label_already_voted)
        self.ui.button_vote.clicked.connect(self.handle_vote)


    def clear_label_already_voted(self):
        self.ui.label_already_voted.setText("")
    def handle_vote(self):
        """
        Handle the voting submission process

        - checks if a candidate is selected
        - Checks if there is duplicates or letters, if so the code will not
        continue
        - Records the vote if its valid
        - updates labels
        """
        if (self.radiobutton_is_selected()):
            if(self.check_id()):
                self.record_vote()
                self.clear_app()
                self.ui.label_already_voted.setText("Voted!!")

    def radiobutton_is_selected(self):
        """
        checks if a radio button is selected
        if it is it sets text to " "

        Returns:
            :bool: True if one is selected False otherwise
            Updates already voted label if there is none
            selected
        """
        if self.ui.radiobutton_carson.isChecked() or self.ui.radiobutton_john.isChecked():
            self.ui.label_already_voted.setText(" ")
            return True
        else:
            self.ui.label_already_voted.setText("Must select one")
            return False

    def clear_app(self):
        """
        clears the textedit and both radio buttons
        """
        self.ui.textedit_id.clear()

        for rb in [self.ui.radiobutton_carson, self.ui.radiobutton_john]:
            rb.setAutoExclusive(False)
            rb.setChecked(False)
            rb.setAutoExclusive(True)

    def record_vote(self):
        """
        Records the user's vote to "voting_logs.csv:
        :return:
        """
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
        Checks if the voter ID is valid
        
        Checks if the ID is a number and not a duplicate reading
        from the CSV file "id_log.csv" 
        If the file does not exist it is created
        
        :return:
            :bool: True if ID is valid and not duplicated or is a number, False otherwise
        """

        if voter_id.isdigit():
            self.ui.label_enter_number.setText("")
            try:
                with open(filename, 'r', newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if int(voter_id) == int(row[0]):
                            self.ui.label_already_voted.setText("Already Voted")
                            return False

                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([int(voter_id)])
                    return True

            except FileNotFoundError:
                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([int(voter_id)])
                    return True
        else:
            self.ui.label_enter_number.setText("Enter a \n number")
            return False



