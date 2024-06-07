# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_console_widget(object):
    def setupUi(self, console_widget):
        if not console_widget.objectName():
            console_widget.setObjectName(u"console_widget")
        console_widget.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(console_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.console_label = QLabel(console_widget)
        self.console_label.setObjectName(u"console_label")
        font = QFont()
        font.setPointSize(12)
        self.console_label.setFont(font)

        self.verticalLayout.addWidget(self.console_label)

        self.vertical_line = QFrame(console_widget)
        self.vertical_line.setObjectName(u"vertical_line")
        self.vertical_line.setFrameShape(QFrame.Shape.VLine)
        self.vertical_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.vertical_line)

        self.console_text = QTextEdit(console_widget)
        self.console_text.setObjectName(u"console_text")
        self.console_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.console_text.setReadOnly(True)

        self.verticalLayout.addWidget(self.console_text)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(console_widget)

        QMetaObject.connectSlotsByName(console_widget)
    # setupUi

    def retranslateUi(self, console_widget):
        console_widget.setWindowTitle(QCoreApplication.translate("console_widget", u"Form", None))
        self.console_label.setText(QCoreApplication.translate("console_widget", u"Console", None))
    # retranslateUi

