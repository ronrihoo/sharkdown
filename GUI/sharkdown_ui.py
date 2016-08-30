# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sharkdown.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Sharkdown(object):
    def setupUi(self, Sharkdown):
        Sharkdown.setObjectName(_fromUtf8("Sharkdown"))
        Sharkdown.resize(899, 600)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        Sharkdown.setFont(font)
        self.centralwidget = QtGui.QWidget(Sharkdown)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontal_layout = QtGui.QHBoxLayout()
        self.horizontal_layout.setObjectName(_fromUtf8("horizontal_layout"))
        self.Markdown = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setKerning(False)
        self.Markdown.setFont(font)
        self.Markdown.setMouseTracking(True)
        self.Markdown.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Markdown.setObjectName(_fromUtf8("Markdown"))
        self.horizontal_layout.addWidget(self.Markdown)
        self.HtmlViewer = QtGui.QTextBrowser(self.centralwidget)
        self.HtmlViewer.setObjectName(_fromUtf8("HtmlViewer"))
        self.horizontal_layout.addWidget(self.HtmlViewer)
        self.horizontalLayout.addLayout(self.horizontal_layout)
        Sharkdown.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Sharkdown)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFormat = QtGui.QMenu(self.menubar)
        self.menuFormat.setObjectName(_fromUtf8("menuFormat"))
        self.menuCommand = QtGui.QMenu(self.menuFormat)
        self.menuCommand.setObjectName(_fromUtf8("menuCommand"))
        self.menuCode = QtGui.QMenu(self.menuFormat)
        self.menuCode.setObjectName(_fromUtf8("menuCode"))
        self.menuVariable = QtGui.QMenu(self.menuFormat)
        self.menuVariable.setObjectName(_fromUtf8("menuVariable"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        Sharkdown.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Sharkdown)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Sharkdown.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Sharkdown)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Sharkdown.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEditor_Viewer = QtGui.QAction(Sharkdown)
        self.actionEditor_Viewer.setObjectName(_fromUtf8("actionEditor_Viewer"))
        self.actionEditor_Only = QtGui.QAction(Sharkdown)
        self.actionEditor_Only.setObjectName(_fromUtf8("actionEditor_Only"))
        self.actionViewer_Only = QtGui.QAction(Sharkdown)
        self.actionViewer_Only.setObjectName(_fromUtf8("actionViewer_Only"))
        self.actionNew = QtGui.QAction(Sharkdown)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(Sharkdown)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(Sharkdown)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionExit = QtGui.QAction(Sharkdown)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDocs = QtGui.QAction(Sharkdown)
        self.actionDocs.setObjectName(_fromUtf8("actionDocs"))
        self.actionAbout = QtGui.QAction(Sharkdown)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLoad = QtGui.QAction(Sharkdown)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionH1 = QtGui.QAction(Sharkdown)
        self.actionH1.setCheckable(False)
        self.actionH1.setObjectName(_fromUtf8("actionH1"))
        self.actionH2 = QtGui.QAction(Sharkdown)
        self.actionH2.setObjectName(_fromUtf8("actionH2"))
        self.actionH3 = QtGui.QAction(Sharkdown)
        self.actionH3.setObjectName(_fromUtf8("actionH3"))
        self.actionToolbar = QtGui.QAction(Sharkdown)
        self.actionToolbar.setObjectName(_fromUtf8("actionToolbar"))
        self.actionBold = QtGui.QAction(Sharkdown)
        self.actionBold.setObjectName(_fromUtf8("actionBold"))
        self.actionItalic = QtGui.QAction(Sharkdown)
        self.actionItalic.setObjectName(_fromUtf8("actionItalic"))
        self.actionInline_Code = QtGui.QAction(Sharkdown)
        self.actionInline_Code.setObjectName(_fromUtf8("actionInline_Code"))
        self.actionCode_Block = QtGui.QAction(Sharkdown)
        self.actionCode_Block.setObjectName(_fromUtf8("actionCode_Block"))
        self.actionNote_Block = QtGui.QAction(Sharkdown)
        self.actionNote_Block.setObjectName(_fromUtf8("actionNote_Block"))
        self.actionURL = QtGui.QAction(Sharkdown)
        self.actionURL.setObjectName(_fromUtf8("actionURL"))
        self.actionImage = QtGui.QAction(Sharkdown)
        self.actionImage.setObjectName(_fromUtf8("actionImage"))
        self.actionCommand_Nonroot = QtGui.QAction(Sharkdown)
        self.actionCommand_Nonroot.setObjectName(_fromUtf8("actionCommand_Nonroot"))
        self.actionCommand_Root = QtGui.QAction(Sharkdown)
        self.actionCommand_Root.setObjectName(_fromUtf8("actionCommand_Root"))
        self.actionCommand_Custom = QtGui.QAction(Sharkdown)
        self.actionCommand_Custom.setObjectName(_fromUtf8("actionCommand_Custom"))
        self.actionWarning_Block = QtGui.QAction(Sharkdown)
        self.actionWarning_Block.setObjectName(_fromUtf8("actionWarning_Block"))
        self.actionEm_Dash = QtGui.QAction(Sharkdown)
        self.actionEm_Dash.setObjectName(_fromUtf8("actionEm_Dash"))
        self.actionList = QtGui.QAction(Sharkdown)
        self.actionList.setObjectName(_fromUtf8("actionList"))
        self.actionLabeled_Code = QtGui.QAction(Sharkdown)
        self.actionLabeled_Code.setObjectName(_fromUtf8("actionLabeled_Code"))
        self.actionSecondary_Label_Code = QtGui.QAction(Sharkdown)
        self.actionSecondary_Label_Code.setObjectName(_fromUtf8("actionSecondary_Label_Code"))
        self.actionVariable_2 = QtGui.QAction(Sharkdown)
        self.actionVariable_2.setObjectName(_fromUtf8("actionVariable_2"))
        self.actionInline_Variable = QtGui.QAction(Sharkdown)
        self.actionInline_Variable.setObjectName(_fromUtf8("actionInline_Variable"))
        self.actionUndo = QtGui.QAction(Sharkdown)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionCopy = QtGui.QAction(Sharkdown)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(Sharkdown)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionSkip = QtGui.QAction(Sharkdown)
        self.actionSkip.setObjectName(_fromUtf8("actionSkip"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionEditor_Viewer)
        self.menuView.addAction(self.actionEditor_Only)
        self.menuView.addAction(self.actionViewer_Only)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToolbar)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuCommand.addAction(self.actionCommand_Nonroot)
        self.menuCommand.addAction(self.actionCommand_Root)
        self.menuCommand.addAction(self.actionCommand_Custom)
        self.menuCode.addAction(self.actionInline_Code)
        self.menuCode.addAction(self.actionCode_Block)
        self.menuCode.addSeparator()
        self.menuCode.addAction(self.actionLabeled_Code)
        self.menuCode.addAction(self.actionSecondary_Label_Code)
        self.menuVariable.addAction(self.actionVariable_2)
        self.menuVariable.addAction(self.actionInline_Variable)
        self.menuFormat.addAction(self.actionH1)
        self.menuFormat.addAction(self.actionH2)
        self.menuFormat.addAction(self.actionH3)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionList)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.menuCommand.menuAction())
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.menuCode.menuAction())
        self.menuFormat.addAction(self.menuVariable.menuAction())
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionNote_Block)
        self.menuFormat.addAction(self.actionWarning_Block)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionURL)
        self.menuFormat.addAction(self.actionImage)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionEm_Dash)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSkip)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionH1)
        self.toolBar.addAction(self.actionH2)
        self.toolBar.addAction(self.actionH3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionList)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInline_Code)
        self.toolBar.addAction(self.actionCode_Block)
        self.toolBar.addAction(self.actionLabeled_Code)
        self.toolBar.addAction(self.actionSecondary_Label_Code)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionVariable_2)
        self.toolBar.addAction(self.actionInline_Variable)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCommand_Nonroot)
        self.toolBar.addAction(self.actionCommand_Root)
        self.toolBar.addAction(self.actionCommand_Custom)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNote_Block)
        self.toolBar.addAction(self.actionWarning_Block)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionURL)
        self.toolBar.addAction(self.actionImage)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEm_Dash)

        self.retranslateUi(Sharkdown)
        QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Markdown.copy)
        QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Markdown.paste)
        QtCore.QObject.connect(self.actionUndo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Markdown.undo)
        QtCore.QMetaObject.connectSlotsByName(Sharkdown)

    def retranslateUi(self, Sharkdown):
        Sharkdown.setWindowTitle(_translate("Sharkdown", "Sharkdown", None))
        self.menuFile.setTitle(_translate("Sharkdown", "File", None))
        self.menuView.setTitle(_translate("Sharkdown", "View", None))
        self.menuHelp.setTitle(_translate("Sharkdown", "Help", None))
        self.menuFormat.setTitle(_translate("Sharkdown", "Format", None))
        self.menuCommand.setTitle(_translate("Sharkdown", "Command", None))
        self.menuCode.setTitle(_translate("Sharkdown", "Code", None))
        self.menuVariable.setTitle(_translate("Sharkdown", "Variable", None))
        self.menuEdit.setTitle(_translate("Sharkdown", "Edit", None))
        self.toolBar.setWindowTitle(_translate("Sharkdown", "toolBar", None))
        self.actionEditor_Viewer.setText(_translate("Sharkdown", "Editor - Viewer", None))
        self.actionEditor_Viewer.setShortcut(_translate("Sharkdown", "Ctrl+1", None))
        self.actionEditor_Only.setText(_translate("Sharkdown", "Editor Only", None))
        self.actionEditor_Only.setShortcut(_translate("Sharkdown", "Ctrl+2", None))
        self.actionViewer_Only.setText(_translate("Sharkdown", "Viewer Only", None))
        self.actionViewer_Only.setShortcut(_translate("Sharkdown", "Ctrl+3", None))
        self.actionNew.setText(_translate("Sharkdown", "New", None))
        self.actionNew.setShortcut(_translate("Sharkdown", "Ctrl+N", None))
        self.actionSave.setText(_translate("Sharkdown", "Save", None))
        self.actionSave.setShortcut(_translate("Sharkdown", "Ctrl+S", None))
        self.actionSave_As.setText(_translate("Sharkdown", "Save As", None))
        self.actionSave_As.setShortcut(_translate("Sharkdown", "Ctrl+Shift+S", None))
        self.actionExit.setText(_translate("Sharkdown", "Exit", None))
        self.actionExit.setShortcut(_translate("Sharkdown", "Ctrl+Q", None))
        self.actionDocs.setText(_translate("Sharkdown", "Docs", None))
        self.actionAbout.setText(_translate("Sharkdown", "About", None))
        self.actionLoad.setText(_translate("Sharkdown", "Open", None))
        self.actionLoad.setToolTip(_translate("Sharkdown", "Open", None))
        self.actionLoad.setShortcut(_translate("Sharkdown", "Ctrl+O", None))
        self.actionH1.setText(_translate("Sharkdown", "H1", None))
        self.actionH1.setShortcut(_translate("Sharkdown", "Alt+1", None))
        self.actionH2.setText(_translate("Sharkdown", "H2", None))
        self.actionH2.setShortcut(_translate("Sharkdown", "Alt+2", None))
        self.actionH3.setText(_translate("Sharkdown", "H3", None))
        self.actionH3.setShortcut(_translate("Sharkdown", "Alt+3", None))
        self.actionToolbar.setText(_translate("Sharkdown", "Toolbar", None))
        self.actionToolbar.setShortcut(_translate("Sharkdown", "Ctrl+T", None))
        self.actionBold.setText(_translate("Sharkdown", "Bold", None))
        self.actionBold.setIconText(_translate("Sharkdown", "B", None))
        self.actionBold.setShortcut(_translate("Sharkdown", "Alt+B", None))
        self.actionItalic.setText(_translate("Sharkdown", "Italic", None))
        self.actionItalic.setIconText(_translate("Sharkdown", "I", None))
        self.actionItalic.setShortcut(_translate("Sharkdown", "Alt+I", None))
        self.actionInline_Code.setText(_translate("Sharkdown", "Inline Code", None))
        self.actionInline_Code.setIconText(_translate("Sharkdown", "`C`", None))
        self.actionInline_Code.setShortcut(_translate("Sharkdown", "Alt+Shift+C", None))
        self.actionCode_Block.setText(_translate("Sharkdown", "Code Block", None))
        self.actionCode_Block.setIconText(_translate("Sharkdown", "```C```", None))
        self.actionCode_Block.setShortcut(_translate("Sharkdown", "Alt+C", None))
        self.actionNote_Block.setText(_translate("Sharkdown", "Note Block", None))
        self.actionNote_Block.setIconText(_translate("Sharkdown", "Note", None))
        self.actionNote_Block.setShortcut(_translate("Sharkdown", "Alt+N", None))
        self.actionURL.setText(_translate("Sharkdown", "URL", None))
        self.actionURL.setShortcut(_translate("Sharkdown", "Alt+U", None))
        self.actionImage.setText(_translate("Sharkdown", "Image", None))
        self.actionImage.setIconText(_translate("Sharkdown", "Img", None))
        self.actionImage.setShortcut(_translate("Sharkdown", "Alt+M", None))
        self.actionCommand_Nonroot.setText(_translate("Sharkdown", "Command - Nonroot", None))
        self.actionCommand_Nonroot.setIconText(_translate("Sharkdown", "$", None))
        self.actionCommand_Nonroot.setShortcut(_translate("Sharkdown", "Alt+D", None))
        self.actionCommand_Root.setText(_translate("Sharkdown", "Command - Root", None))
        self.actionCommand_Root.setIconText(_translate("Sharkdown", "#", None))
        self.actionCommand_Root.setShortcut(_translate("Sharkdown", "Alt+S", None))
        self.actionCommand_Custom.setText(_translate("Sharkdown", "Command - Custom", None))
        self.actionCommand_Custom.setIconText(_translate("Sharkdown", "Custom", None))
        self.actionCommand_Custom.setShortcut(_translate("Sharkdown", "Alt+A", None))
        self.actionWarning_Block.setText(_translate("Sharkdown", "Warning Block", None))
        self.actionWarning_Block.setIconText(_translate("Sharkdown", "Warning", None))
        self.actionWarning_Block.setToolTip(_translate("Sharkdown", "Warning Block", None))
        self.actionWarning_Block.setShortcut(_translate("Sharkdown", "Alt+W", None))
        self.actionEm_Dash.setText(_translate("Sharkdown", "Em Dash", None))
        self.actionEm_Dash.setIconText(_translate("Sharkdown", "—", None))
        self.actionEm_Dash.setToolTip(_translate("Sharkdown", "Em Dash", None))
        self.actionEm_Dash.setShortcut(_translate("Sharkdown", "Alt+-", None))
        self.actionList.setText(_translate("Sharkdown", "List", None))
        self.actionList.setToolTip(_translate("Sharkdown", "List", None))
        self.actionList.setShortcut(_translate("Sharkdown", "Alt+L", None))
        self.actionLabeled_Code.setText(_translate("Sharkdown", "Labeled Code", None))
        self.actionLabeled_Code.setIconText(_translate("Sharkdown", "[labeled]Code", None))
        self.actionLabeled_Code.setToolTip(_translate("Sharkdown", "Labeled Code", None))
        self.actionSecondary_Label_Code.setText(_translate("Sharkdown", "Secondary Labeled Code", None))
        self.actionSecondary_Label_Code.setIconText(_translate("Sharkdown", "[2nd_labeled]Code", None))
        self.actionSecondary_Label_Code.setToolTip(_translate("Sharkdown", "Secondary Labeled Code", None))
        self.actionVariable_2.setText(_translate("Sharkdown", "Variable", None))
        self.actionVariable_2.setIconText(_translate("Sharkdown", "Var", None))
        self.actionVariable_2.setShortcut(_translate("Sharkdown", "Alt+V", None))
        self.actionInline_Variable.setText(_translate("Sharkdown", "Inline Variable", None))
        self.actionInline_Variable.setIconText(_translate("Sharkdown", "`Var`", None))
        self.actionInline_Variable.setShortcut(_translate("Sharkdown", "Alt+Shift+V", None))
        self.actionUndo.setText(_translate("Sharkdown", "Undo", None))
        self.actionUndo.setShortcut(_translate("Sharkdown", "Ctrl+Z", None))
        self.actionCopy.setText(_translate("Sharkdown", "Copy", None))
        self.actionCopy.setShortcut(_translate("Sharkdown", "Ctrl+C", None))
        self.actionPaste.setText(_translate("Sharkdown", "Paste", None))
        self.actionPaste.setShortcut(_translate("Sharkdown", "Ctrl+V", None))
        self.actionSkip.setText(_translate("Sharkdown", "Skip", None))
        self.actionSkip.setToolTip(_translate("Sharkdown", "Skip over remaining markdown code", None))
        self.actionSkip.setShortcut(_translate("Sharkdown", "Alt+Return", None))

