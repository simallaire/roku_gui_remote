# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(276, 393)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        Dialog.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        icon = QtGui.QIcon.fromTheme("computer")
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(0.95)
        Dialog.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 276, 392))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonOn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonOn.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonOn.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.pushButtonOn.setObjectName("pushButtonOn")
        self.horizontalLayout_2.addWidget(self.pushButtonOn)
        self.pushButtonOff = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonOff.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonOff.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.pushButtonOff.setObjectName("pushButtonOff")
        self.horizontalLayout_2.addWidget(self.pushButtonOff)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonPlay = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonPlay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlay.setIcon(icon)
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.horizontalLayout.addWidget(self.pushButtonPlay)
        self.pushButtonPause = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonPause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/pause.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPause.setIcon(icon1)
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.horizontalLayout.addWidget(self.pushButtonPause)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonDown = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonDown.setMinimumSize(QtCore.QSize(0, 69))
        self.pushButtonDown.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButtonDown.setAutoFillBackground(True)
        self.pushButtonDown.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/down-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDown.setIcon(icon2)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.gridLayout.addWidget(self.pushButtonDown, 2, 1, 1, 1)
        self.pushButtonUp = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonUp.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonUp.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButtonUp.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Downloads/up-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonUp.setIcon(icon3)
        self.pushButtonUp.setObjectName("pushButtonUp")
        self.gridLayout.addWidget(self.pushButtonUp, 0, 1, 1, 1)
        self.pushButtonOk = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonOk.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.gridLayout.addWidget(self.pushButtonOk, 1, 1, 1, 1)
        self.pushButtonRight = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonRight.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButtonRight.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButtonRight.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Downloads/next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonRight.setIcon(icon4)
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.gridLayout.addWidget(self.pushButtonRight, 1, 2, 1, 1)
        self.pushButtonLeft = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLeft.sizePolicy().hasHeightForWidth())
        self.pushButtonLeft.setSizePolicy(sizePolicy)
        self.pushButtonLeft.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonLeft.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonLeft.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Downloads/left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonLeft.setIcon(icon5)
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.gridLayout.addWidget(self.pushButtonLeft, 1, 0, 1, 1)
        self.pushButtonVolUp = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonVolUp.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonVolUp.setText("")
        icon = QtGui.QIcon.fromTheme("audio-volume-high")
        self.pushButtonVolUp.setIcon(icon)
        self.pushButtonVolUp.setObjectName("pushButtonVolUp")
        self.gridLayout.addWidget(self.pushButtonVolUp, 2, 2, 1, 1)
        self.pushButtonVolDown = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonVolDown.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonVolDown.setText("")
        icon = QtGui.QIcon.fromTheme("audio-volume-low")
        self.pushButtonVolDown.setIcon(icon)
        self.pushButtonVolDown.setObjectName("pushButtonVolDown")
        self.gridLayout.addWidget(self.pushButtonVolDown, 2, 0, 1, 1)
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonBack.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../Downloads/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBack.setIcon(icon6)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.gridLayout.addWidget(self.pushButtonBack, 0, 0, 1, 1)
        self.pushButtonHome = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonHome.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButtonHome.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../Downloads/home2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHome.setIcon(icon7)
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.gridLayout.addWidget(self.pushButtonHome, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Roku remote"))
        self.pushButtonOn.setText(_translate("Dialog", "On"))
        self.pushButtonOff.setText(_translate("Dialog", "Off"))
        self.pushButtonOk.setText(_translate("Dialog", "OK"))
