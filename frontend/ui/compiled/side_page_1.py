# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_page_1.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(284, 572)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.title.setFont(font)

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.working_directory_label = QLabel(Form)
        self.working_directory_label.setObjectName(u"working_directory_label")
        sizePolicy.setHeightForWidth(self.working_directory_label.sizePolicy().hasHeightForWidth())
        self.working_directory_label.setSizePolicy(sizePolicy)
        self.working_directory_label.setMinimumSize(QSize(110, 24))
        self.working_directory_label.setMaximumSize(QSize(110, 24))

        self.horizontalLayout_2.addWidget(self.working_directory_label)

        self.working_directory_line_edit = QLineEdit(Form)
        self.working_directory_line_edit.setObjectName(u"working_directory_line_edit")
        self.working_directory_line_edit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.working_directory_line_edit)

        self.working_directory_change_btn = QPushButton(Form)
        self.working_directory_change_btn.setObjectName(u"working_directory_change_btn")
        sizePolicy.setHeightForWidth(self.working_directory_change_btn.sizePolicy().hasHeightForWidth())
        self.working_directory_change_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.working_directory_change_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.file_explorer_tree = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.file_explorer_tree.setHeaderItem(__qtreewidgetitem)
        self.file_explorer_tree.setObjectName(u"file_explorer_tree")
        self.file_explorer_tree.header().setVisible(False)

        self.verticalLayout.addWidget(self.file_explorer_tree)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Properties", None))
        self.working_directory_label.setText(QCoreApplication.translate("Form", u"Working Directory", None))
        self.working_directory_change_btn.setText(QCoreApplication.translate("Form", u"Change", None))
    # retranslateUi

