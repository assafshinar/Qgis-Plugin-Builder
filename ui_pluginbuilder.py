# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pluginbuilder.ui'
#
# Created: Tue Jul 31 07:16:11 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PluginBuilder(object):
    def setupUi(self, PluginBuilder):
        PluginBuilder.setObjectName(_fromUtf8("PluginBuilder"))
        PluginBuilder.resize(893, 601)
        PluginBuilder.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(PluginBuilder)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(PluginBuilder)
        self.webView.setMinimumSize(QtCore.QSize(380, 390))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(",Verdana,sans"))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.webView.setFont(font)
        self.webView.setStyleSheet(_fromUtf8("QWebView{\n"
"    font: Georgia, Verdana, sans;\n"
"    font-size:1.0em;\n"
"    background-color: rgb(210, 255, 217);\n"
"    border-left: solid 2px black;\n"
"}"))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 15, 1)
        self.line = QtGui.QFrame(PluginBuilder)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 15, 2)
        self.label_10 = QtGui.QLabel(PluginBuilder)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(PluginBuilder)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_class_name = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_class_name.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_class_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_class_name.setText(_fromUtf8(""))
        self.lineEdit_class_name.setObjectName(_fromUtf8("lineEdit_class_name"))
        self.horizontalLayout.addWidget(self.lineEdit_class_name)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(PluginBuilder)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_title = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_title.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_title.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_title.setText(_fromUtf8(""))
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.horizontalLayout_2.addWidget(self.lineEdit_title)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(PluginBuilder)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_description = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_description.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_description.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_description.setText(_fromUtf8(""))
        self.lineEdit_description.setObjectName(_fromUtf8("lineEdit_description"))
        self.horizontalLayout_3.addWidget(self.lineEdit_description)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(PluginBuilder)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_version_no = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_version_no.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_version_no.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_version_no.setObjectName(_fromUtf8("lineEdit_version_no"))
        self.horizontalLayout_4.addWidget(self.lineEdit_version_no)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 2, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(PluginBuilder)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_min_version_no = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_min_version_no.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_min_version_no.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_min_version_no.setObjectName(_fromUtf8("lineEdit_min_version_no"))
        self.horizontalLayout_5.addWidget(self.lineEdit_min_version_no)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 2, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(PluginBuilder)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_menu_text = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_menu_text.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_menu_text.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_menu_text.setText(_fromUtf8(""))
        self.lineEdit_menu_text.setObjectName(_fromUtf8("lineEdit_menu_text"))
        self.horizontalLayout_6.addWidget(self.lineEdit_menu_text)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 2, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(PluginBuilder)
        self.label_7.setMinimumSize(QtCore.QSize(150, 0))
        self.label_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_company_name = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_company_name.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_company_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_company_name.setText(_fromUtf8(""))
        self.lineEdit_company_name.setObjectName(_fromUtf8("lineEdit_company_name"))
        self.horizontalLayout_7.addWidget(self.lineEdit_company_name)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 2, 1, 2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(PluginBuilder)
        self.label_8.setMinimumSize(QtCore.QSize(150, 0))
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_email_address = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_email_address.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_email_address.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_email_address.setText(_fromUtf8(""))
        self.lineEdit_email_address.setObjectName(_fromUtf8("lineEdit_email_address"))
        self.horizontalLayout_8.addWidget(self.lineEdit_email_address)
        self.gridLayout.addLayout(self.horizontalLayout_8, 8, 2, 1, 2)
        self.label_14 = QtGui.QLabel(PluginBuilder)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 9, 3, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(PluginBuilder)
        self.label_9.setMinimumSize(QtCore.QSize(150, 0))
        self.label_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_tracker = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_tracker.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_tracker.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_tracker.setObjectName(_fromUtf8("lineEdit_tracker"))
        self.horizontalLayout_9.addWidget(self.lineEdit_tracker)
        self.gridLayout.addLayout(self.horizontalLayout_9, 10, 3, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtGui.QLabel(PluginBuilder)
        self.label_11.setMinimumSize(QtCore.QSize(150, 0))
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.lineEdit_homepage = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_homepage.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_homepage.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_homepage.setObjectName(_fromUtf8("lineEdit_homepage"))
        self.horizontalLayout_10.addWidget(self.lineEdit_homepage)
        self.gridLayout.addLayout(self.horizontalLayout_10, 11, 3, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtGui.QLabel(PluginBuilder)
        self.label_13.setMinimumSize(QtCore.QSize(150, 0))
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        self.lineEdit_repository = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_repository.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_repository.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_repository.setObjectName(_fromUtf8("lineEdit_repository"))
        self.horizontalLayout_12.addWidget(self.lineEdit_repository)
        self.gridLayout.addLayout(self.horizontalLayout_12, 12, 3, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(PluginBuilder)
        self.label_12.setMinimumSize(QtCore.QSize(150, 0))
        self.label_12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.lineEdit_tags = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_tags.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_tags.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_tags.setObjectName(_fromUtf8("lineEdit_tags"))
        self.horizontalLayout_11.addWidget(self.lineEdit_tags)
        self.gridLayout.addLayout(self.horizontalLayout_11, 13, 3, 1, 1)
        self.checkBox_experimental = QtGui.QCheckBox(PluginBuilder)
        self.checkBox_experimental.setObjectName(_fromUtf8("checkBox_experimental"))
        self.gridLayout.addWidget(self.checkBox_experimental, 14, 3, 1, 1)
        self.line_2 = QtGui.QFrame(PluginBuilder)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 15, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PluginBuilder)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 15, 3, 1, 1)

        self.retranslateUi(PluginBuilder)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PluginBuilder.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginBuilder)

    def retranslateUi(self, PluginBuilder):
        PluginBuilder.setWindowTitle(QtGui.QApplication.translate("PluginBuilder", "QGIS Plugin Builder 1.8.4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("PluginBuilder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">QGIS Plugin Builder</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PluginBuilder", "Class name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PluginBuilder", "Descriptive title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PluginBuilder", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PluginBuilder", "Version number", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_version_no.setText(QtGui.QApplication.translate("PluginBuilder", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PluginBuilder", "Minimum QGIS version", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_min_version_no.setText(QtGui.QApplication.translate("PluginBuilder", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PluginBuilder", "Text for the menu item", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PluginBuilder", "Author/Company", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PluginBuilder", "Email address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("PluginBuilder", "Optional Items", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("PluginBuilder", "Bug tracker", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("PluginBuilder", "Home page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("PluginBuilder", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("PluginBuilder", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_experimental.setText(QtGui.QApplication.translate("PluginBuilder", "Flag the plugin as experimental", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
