# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ELection_guiCZbaJs.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Voting Booth")
        Dialog.resize(324, 259)
        Dialog.setMinimumSize(QSize(324, 259))
        Dialog.setMaximumSize(QSize(324, 259))
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName("label_title")
        self.label_title.setGeometry(QRect(-40, -20, 401, 91))
        self.label_title.setStyleSheet("font: 30pt \"Algerian\";")
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textedit_id = QTextEdit(Dialog)
        self.textedit_id.setObjectName("textedit_id")
        self.textedit_id.setGeometry(QRect(110, 60, 151, 31))
        self.label_voter_id = QLabel(Dialog)
        self.label_voter_id.setObjectName("label_voter_id")
        self.label_voter_id.setGeometry(QRect(40, 60, 81, 31))
        self.label_voter_id.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_voter_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_candidates = QLabel(Dialog)
        self.label_candidates.setObjectName("label_candidates")
        self.label_candidates.setGeometry(QRect(100, 100, 111, 31))
        self.label_candidates.setStyleSheet("font: 13pt \"Segoe UI\";")
        self.label_candidates.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.radiobutton_carson = QRadioButton(Dialog)
        self.radiobutton_carson.setObjectName("radiobutton_carson")
        self.radiobutton_carson.setGeometry(QRect(110, 130, 92, 20))
        self.radiobutton_john = QRadioButton(Dialog)
        self.radiobutton_john.setObjectName("radiobutton_john")
        self.radiobutton_john.setGeometry(QRect(110, 160, 92, 20))
        self.button_vote = QPushButton(Dialog)
        self.button_vote.setObjectName("button_vote")
        self.button_vote.setGeometry(QRect(80, 190, 151, 31))
        self.label_already_voted = QLabel(Dialog)
        self.label_already_voted.setObjectName("label_already_voted")
        self.label_already_voted.setGeometry(QRect(100, 230, 131, 16))
        self.label_already_voted.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(270, 60, 61, 41))
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Voting Booth", "Voting Booth"))
        self.label_title.setToolTip(_translate("Voting Booth", "<html><head/><body><p><br/></p></body></html>"))
        self.label_title.setText(_translate("Voting Booth", "VOTING FORM"))
        self.label_voter_id.setText(_translate("Voting Booth", "VOTER ID"))
        self.label_candidates.setText(_translate("Voting Booth", "CANDIDATES"))
        self.radiobutton_carson.setText(_translate("Voting Booth", "Carson"))
        self.radiobutton_john.setText(_translate("Voting Booth", "John"))
        self.button_vote.setText(_translate("Voting Booth", "VOTE"))
        self.label_already_voted.setText(_translate("Voting Booth", " "))
        self.label.setText(_translate("Voting Booth", " "))