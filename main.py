if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Vote_Menu()  # Changed from QDialog() to Ui_Vote_Menu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
