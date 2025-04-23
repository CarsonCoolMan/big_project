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
from PyQt6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Vote_Menu(object):
    def setupUi(self, Vote_Menu):
        if not Vote_Menu.objectName():
            Vote_Menu.setObjectName(u"Vote_Menu")
        Vote_Menu.resize(384, 241)
        self.Voting_booth = QLabel(Vote_Menu)
        self.Voting_booth.setObjectName(u"Voting_booth")
        self.Voting_booth.setGeometry(QRect(30, 10, 351, 71))
        self.Voting_booth.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.Voting_booth.setStyleSheet(u"\n"
"font: 700 16pt \"Script\";")
        self.Voting_booth.setFrameShadow(QFrame.Shadow.Sunken)
        self.Voting_booth.setTextFormat(Qt.TextFormat.RichText)
        self.Vote_button = QPushButton(Vote_Menu)
        self.Vote_button.setObjectName(u"Vote_button")
        self.Vote_button.setGeometry(QRect(180, 180, 111, 31))
        self.Vote_button.setStyleSheet(u"font: italic 15pt  \"Monotype Corsiva\" ;\n"
"background: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))\n"
"")
        self.label = QLabel(Vote_Menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 210, 91, 16))
        self.pushButton = QPushButton(Vote_Menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 200, 75, 41))
        self.pushButton.setStyleSheet(u"background: rgb(166, 0, 0)")
        self.widget = QWidget(Vote_Menu)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 131, 151))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.vote_carson = QPushButton(self.widget)
        self.vote_carson.setObjectName(u"vote_carson")
        self.vote_carson.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, \n"
"        x2:1, y2:1, \n"
"        stop:0 #ff4d4d, \n"
"        stop:1 #990000\n"
"    );\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.vote_carson)

        self.vote_george = QPushButton(self.widget)
        self.vote_george.setObjectName(u"vote_george")
        self.vote_george.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")

        self.verticalLayout.addWidget(self.vote_george)

        self.vote_abraham = QPushButton(self.widget)
        self.vote_abraham.setObjectName(u"vote_abraham")
        self.vote_abraham.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(10, 49, 97, 255))")

        self.verticalLayout.addWidget(self.vote_abraham)

        self.retranslateUi(Vote_Menu)

        QMetaObject.connectSlotsByName(Vote_Menu)
    # setupUi

    def retranslateUi(self, Vote_Menu):
        Vote_Menu.setWindowTitle(QCoreApplication.translate("Vote_Menu", u"Dialog", None))
        self.Voting_booth.setText(QCoreApplication.translate("Vote_Menu", u"Presidential Voting Booth", None))
        self.Vote_button.setText(QCoreApplication.translate("Vote_Menu", u"VOTE", None))
        self.label.setText(QCoreApplication.translate("Vote_Menu", u"Nobody selected", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Vote_Menu", u"<html><head/><body><p>END</p><p>ELECTION</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Vote_Menu", u"END VOTE", None))
        self.vote_carson.setText(QCoreApplication.translate("Vote_Menu", u"Carson Holmes", None))
        self.vote_george.setText(QCoreApplication.translate("Vote_Menu", u"George Washington", None))
        self.vote_abraham.setText(QCoreApplication.translate("Vote_Menu", u"Abraham Lincoln", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Vote_Menu()  # Changed from QDialog() to Ui_Vote_Menu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
