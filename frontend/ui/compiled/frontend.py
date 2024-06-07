# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frontend.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 831)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.page_change_frame = QFrame(self.frame)
        self.page_change_frame.setObjectName(u"page_change_frame")
        self.page_change_frame.setFrameShape(QFrame.NoFrame)
        self.page_btn_layout = QVBoxLayout(self.page_change_frame)
        self.page_btn_layout.setObjectName(u"page_btn_layout")
        self.page_1_btn = QPushButton(self.page_change_frame)
        self.page_1_btn.setObjectName(u"page_1_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_1_btn.sizePolicy().hasHeightForWidth())
        self.page_1_btn.setSizePolicy(sizePolicy)
        self.page_1_btn.setMinimumSize(QSize(50, 50))
        self.page_1_btn.setMaximumSize(QSize(50, 50))

        self.page_btn_layout.addWidget(self.page_1_btn)

        self.page_2_btn = QPushButton(self.page_change_frame)
        self.page_2_btn.setObjectName(u"page_2_btn")
        sizePolicy.setHeightForWidth(self.page_2_btn.sizePolicy().hasHeightForWidth())
        self.page_2_btn.setSizePolicy(sizePolicy)
        self.page_2_btn.setMinimumSize(QSize(50, 50))
        self.page_2_btn.setMaximumSize(QSize(50, 50))

        self.page_btn_layout.addWidget(self.page_2_btn)

        self.page_3_btn = QPushButton(self.page_change_frame)
        self.page_3_btn.setObjectName(u"page_3_btn")
        sizePolicy.setHeightForWidth(self.page_3_btn.sizePolicy().hasHeightForWidth())
        self.page_3_btn.setSizePolicy(sizePolicy)
        self.page_3_btn.setMinimumSize(QSize(50, 50))
        self.page_3_btn.setMaximumSize(QSize(50, 50))

        self.page_btn_layout.addWidget(self.page_3_btn)

        self.page_4_btn = QPushButton(self.page_change_frame)
        self.page_4_btn.setObjectName(u"page_4_btn")
        sizePolicy.setHeightForWidth(self.page_4_btn.sizePolicy().hasHeightForWidth())
        self.page_4_btn.setSizePolicy(sizePolicy)
        self.page_4_btn.setMinimumSize(QSize(50, 50))
        self.page_4_btn.setMaximumSize(QSize(50, 50))

        self.page_btn_layout.addWidget(self.page_4_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page_btn_layout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.page_change_frame)

        self.screen_splitter = QSplitter(self.frame)
        self.screen_splitter.setObjectName(u"screen_splitter")
        self.screen_splitter.setLineWidth(1)
        self.screen_splitter.setOrientation(Qt.Horizontal)
        self.screen_splitter.setHandleWidth(10)
        self.side_widget = QStackedWidget(self.screen_splitter)
        self.side_widget.setObjectName(u"side_widget")
        self.side_widget.setFrameShape(QFrame.Box)
        self.side_page_1 = QWidget()
        self.side_page_1.setObjectName(u"side_page_1")
        self.side_page_1_layout = QVBoxLayout(self.side_page_1)
        self.side_page_1_layout.setObjectName(u"side_page_1_layout")
        self.side_widget.addWidget(self.side_page_1)
        self.side_page_2 = QWidget()
        self.side_page_2.setObjectName(u"side_page_2")
        self.side_page_2_layout = QVBoxLayout(self.side_page_2)
        self.side_page_2_layout.setObjectName(u"side_page_2_layout")
        self.side_widget.addWidget(self.side_page_2)
        self.side_page_3 = QWidget()
        self.side_page_3.setObjectName(u"side_page_3")
        self.side_page_3_layout = QVBoxLayout(self.side_page_3)
        self.side_page_3_layout.setObjectName(u"side_page_3_layout")
        self.side_widget.addWidget(self.side_page_3)
        self.side_page_4 = QWidget()
        self.side_page_4.setObjectName(u"side_page_4")
        self.side_page_4_layout = QVBoxLayout(self.side_page_4)
        self.side_page_4_layout.setObjectName(u"side_page_4_layout")
        self.side_widget.addWidget(self.side_page_4)
        self.screen_splitter.addWidget(self.side_widget)
        self.vert_splitter = QSplitter(self.screen_splitter)
        self.vert_splitter.setObjectName(u"vert_splitter")
        self.vert_splitter.setLineWidth(2)
        self.vert_splitter.setOrientation(Qt.Vertical)
        self.vert_splitter.setHandleWidth(10)
        self.top_widget = QStackedWidget(self.vert_splitter)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setFrameShape(QFrame.Box)
        self.top_page_1 = QWidget()
        self.top_page_1.setObjectName(u"top_page_1")
        self.top_page_1_layout = QVBoxLayout(self.top_page_1)
        self.top_page_1_layout.setObjectName(u"top_page_1_layout")
        self.top_widget.addWidget(self.top_page_1)
        self.top_page_2 = QWidget()
        self.top_page_2.setObjectName(u"top_page_2")
        self.top_page_2_layout = QVBoxLayout(self.top_page_2)
        self.top_page_2_layout.setObjectName(u"top_page_2_layout")
        self.top_widget.addWidget(self.top_page_2)
        self.top_page_3 = QWidget()
        self.top_page_3.setObjectName(u"top_page_3")
        self.top_page_3_layout = QVBoxLayout(self.top_page_3)
        self.top_page_3_layout.setObjectName(u"top_page_3_layout")
        self.top_widget.addWidget(self.top_page_3)
        self.top_page_4 = QWidget()
        self.top_page_4.setObjectName(u"top_page_4")
        self.top_page_4_layout = QVBoxLayout(self.top_page_4)
        self.top_page_4_layout.setObjectName(u"top_page_4_layout")
        self.top_widget.addWidget(self.top_page_4)
        self.vert_splitter.addWidget(self.top_widget)
        self.bottom_widget = QFrame(self.vert_splitter)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.bottom_widget.setFrameShape(QFrame.Box)
        self.bottom_widget.setFrameShadow(QFrame.Plain)
        self.bottom_widget.setLineWidth(1)
        self.bottom_widget_layout = QVBoxLayout(self.bottom_widget)
        self.bottom_widget_layout.setObjectName(u"bottom_widget_layout")
        self.vert_splitter.addWidget(self.bottom_widget)
        self.screen_splitter.addWidget(self.vert_splitter)

        self.horizontalLayout.addWidget(self.screen_splitter)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_file = QMenu(self.menuBar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menuBar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_view = QMenu(self.menuBar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_help = QMenu(self.menuBar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_edit.menuAction())
        self.menuBar.addAction(self.menu_view.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)

        self.side_widget.setCurrentIndex(3)
        self.top_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.page_1_btn.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.page_2_btn.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.page_3_btn.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.page_4_btn.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

