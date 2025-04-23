# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerNDAOJB.ui'
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
from PyQt6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Vote_Menu(object):
    def setupUi(self, Vote_Menu):
        if not Vote_Menu.objectName():
            Vote_Menu.setObjectName(u"Vote_Menu")
        Vote_Menu.resize(384, 241)
        self.label = QLabel(Vote_Menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 171, 51))
        self.label.setStyleSheet(u"\n"
"font: 700 9pt \"Script\";")
        self.label.setFrameShadow(QFrame.Shadow.Sunken)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.widget = QWidget(Vote_Menu)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 191, 141))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.vote_carson = QCheckBox(self.widget)
        self.vote_carson.setObjectName(u"vote_carson")

        self.verticalLayout.addWidget(self.vote_carson)

        self.vote_abraham = QCheckBox(self.widget)
        self.vote_abraham.setObjectName(u"vote_abraham")

        self.verticalLayout.addWidget(self.vote_abraham)

        self.vote_george = QCheckBox(self.widget)
        self.vote_george.setObjectName(u"vote_george")

        self.verticalLayout.addWidget(self.vote_george)

        self.vote_theodore = QCheckBox(self.widget)
        self.vote_theodore.setObjectName(u"vote_theodore")

        self.verticalLayout.addWidget(self.vote_theodore)

        self.vote_abraham.raise_()
        self.vote_george.raise_()
        self.vote_theodore.raise_()
        self.vote_carson.raise_()

        self.retranslateUi(Vote_Menu)

        QMetaObject.connectSlotsByName(Vote_Menu)
    # setupUi

    def retranslateUi(self, Vote_Menu):
        Vote_Menu.setWindowTitle(QCoreApplication.translate("Vote_Menu", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Vote_Menu", u"Voting Booth", None))
        self.vote_carson.setText(QCoreApplication.translate("Vote_Menu", u"Carson Holmes", None))
        self.vote_abraham.setText(QCoreApplication.translate("Vote_Menu", u"Abraham Lincoln", None))
        self.vote_george.setText(QCoreApplication.translate("Vote_Menu", u"George Washington", None))
        self.vote_theodore.setText(QCoreApplication.translate("Vote_Menu", u"Theodore Roosevelt", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Vote_Menu()  # Changed from QDialog() to Ui_Vote_Menu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
