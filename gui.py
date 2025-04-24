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

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Vote_Menu(object):
    def setupUi(self, Vote_Menu):
        if not Vote_Menu.objectName():
            Vote_Menu.setObjectName("Vote_Menu")
        Vote_Menu.resize(384, 241)
        self.Voting_booth = QLabel(Vote_Menu)
        self.Voting_booth.setObjectName("Voting_booth")
        self.Voting_booth.setGeometry(QRect(30, 10, 351, 71))
        self.Voting_booth.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.Voting_booth.setStyleSheet("font: 700 16pt 'Script';")
        self.Voting_booth.setFrameShadow(QFrame.Shadow.Sunken)
        self.Voting_booth.setTextFormat(Qt.TextFormat.RichText)

        self.Vote_button = QPushButton(Vote_Menu)
        self.Vote_button.setObjectName("Vote_button")
        self.Vote_button.setGeometry(QRect(180, 180, 111, 31))
        self.Vote_button.setStyleSheet(
            "font: italic 15pt 'Monotype Corsiva';"
            "background: qconicalgradient(cx:0.5, cy:0.5, angle:0, "
            "stop:0 rgba(35, 40, 3, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))"
        )

        self.selection_label = QLabel(Vote_Menu)
        self.selection_label.setObjectName("selection_label")
        self.selection_label.setGeometry(QRect(190, 210, 91, 16))

        self.end_vote = QPushButton(Vote_Menu)
        self.end_vote.setObjectName("end_vote")
        self.end_vote.setGeometry(QRect(310, 200, 75, 41))
        self.end_vote.setStyleSheet("background: rgb(166, 0, 0)")

        self.layoutWidget = QWidget(Vote_Menu)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 70, 131, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.vote_carson = QPushButton(self.layoutWidget)
        self.vote_carson.setObjectName("vote_carson")
        self.vote_carson.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff4d4d, stop:1 #990000);"
        )
        self.verticalLayout.addWidget(self.vote_carson)

        self.vote_george = QPushButton(self.layoutWidget)
        self.vote_george.setObjectName("vote_george")
        self.vote_george.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 black, stop:1 white);"
        )
        self.verticalLayout.addWidget(self.vote_george)

        self.vote_abraham = QPushButton(self.layoutWidget)
        self.vote_abraham.setObjectName("vote_abraham")
        self.vote_abraham.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 black, stop:1 #0a3161);"
        )
        self.verticalLayout.addWidget(self.vote_abraham)

        self.winner_label = QLabel(Vote_Menu)
        self.winner_label.setObjectName("winner_label")
        self.winner_label.setGeometry(QRect(220, 140, 61, 16))
        self.winner_label.setStyleSheet("font: 9pt 'Segoe Print';")

        self.widget = QWidget(Vote_Menu)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(200, 80, 140, 18))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_carson = QLabel(self.widget)
        self.label_carson.setObjectName("label_carson")
        self.horizontalLayout.addWidget(self.label_carson)

        self.label_george = QLabel(self.widget)
        self.label_george.setObjectName("label_george")
        self.horizontalLayout.addWidget(self.label_george)

        self.label_abraham = QLabel(self.widget)
        self.label_abraham.setObjectName("label_abraham")
        self.horizontalLayout.addWidget(self.label_abraham)

        self.widget1 = QWidget(Vote_Menu)
        self.widget1.setObjectName("widget1")
        self.widget1.setGeometry(QRect(200, 100, 131, 18))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.vote_count_carson = QLabel(self.widget1)
        self.vote_count_carson.setObjectName("vote_count_carson")
        self.horizontalLayout_2.addWidget(self.vote_count_carson)

        self.vote_count_george = QLabel(self.widget1)
        self.vote_count_george.setObjectName("vote_count_george")
        self.horizontalLayout_2.addWidget(self.vote_count_george)

        self.vote_count_abraham = QLabel(self.widget1)
        self.vote_count_abraham.setObjectName("vote_count_abraham")
        self.horizontalLayout_2.addWidget(self.vote_count_abraham)

        self.retranslateUi(Vote_Menu)
        QMetaObject.connectSlotsByName(Vote_Menu)

    def retranslateUi(self, Vote_Menu):
        _translate = QCoreApplication.translate
        Vote_Menu.setWindowTitle(_translate("Vote_Menu", "Dialog"))
        self.Voting_booth.setText(_translate("Vote_Menu", "Presidential Voting Booth"))
        self.Vote_button.setText(_translate("Vote_Menu", "VOTE"))
        self.selection_label.setText(_translate("Vote_Menu", "Nobody selected"))
        self.end_vote.setToolTip(_translate("Vote_Menu", "<html><head/><body><p>END</p><p>ELECTION</p></body></html>"))
        self.end_vote.setText(_translate("Vote_Menu", "END VOTE"))
        self.vote_carson.setText(_translate("Vote_Menu", "Carson Holmes"))
        self.vote_george.setText(_translate("Vote_Menu", "George Washington"))
        self.vote_abraham.setText(_translate("Vote_Menu", "Abraham Lincoln"))
        self.winner_label.setText(_translate("Vote_Menu", "Winner is:"))
        self.label_carson.setText(_translate("Vote_Menu", "Carson"))
        self.label_george.setText(_translate("Vote_Menu", "George"))
        self.label_abraham.setText(_translate("Vote_Menu", "Abraham"))
        self.vote_count_carson.setText(_translate("Vote_Menu", "0"))
        self.vote_count_george.setText(_translate("Vote_Menu", "0"))
        self.vote_count_abraham.setText(_translate("Vote_Menu", "0"))

