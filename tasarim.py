

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Ikinci(object):
    def setupUi(self, Ikinci):
        Ikinci.setObjectName("Ikinci")
        Ikinci.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Ikinci)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 371, 261))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Ikinci)
        QtCore.QMetaObject.connectSlotsByName(Ikinci)

    def retranslateUi(self, Ikinci):
        _translate = QtCore.QCoreApplication.translate
        Ikinci.setWindowTitle(_translate("Ikinci", "Uygulama Info"))
        self.textBrowser.setHtml(_translate("Ikinci", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Raleway\'; font-size:12pt; font-weight:296; color:#524a58; background-color:#ffffff;\">Is bu kullanici sözlesmesi ve Web Sitesinde yer alan diger kurallar ... tarafindan sunulan hizmetlere iliskin sart ve kosullari ve Web Sitesinin kullanilmasina iliskin kurallari duzenlemektedir. Kullanicinin, Web Sitesi uzerinden Hizmet Talebi veya Meslek Profili olustururken isbu Sozlesmeyi onayladigi veya Web Sitesinden yararlanmaya basladigi andan itibaren isbu Sozlesmeye uymayi taahhut ettigi kabul edilir. Kosullarin sizin icin uygun olmamasi halinde lütfen Web Sitesini ve sunulan hizmetleri </span><span style=\" font-family:\'Raleway\'; font-size:12pt; font-weight:600; color:#524a58; background-color:#ffffff;\">kullanmayiniz.</span></p></body></html>"))

class Ui_MainWindow(object):        
    def setupUi(self, MainWindow,parent=None):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 680, 611, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bilgi2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(70)
        self.bilgi2.setFont(font)
        self.bilgi2.setAutoFillBackground(True)
        self.bilgi2.setText("")
        self.bilgi2.setScaledContents(False)
        self.bilgi2.setObjectName("bilgi2")
        self.bilgi2.setStyleSheet('QLabel#bilgi2 {color: red}')
        self.horizontalLayout.addWidget(self.bilgi2)
        self.kayitol = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kayitol.setFont(font)
        self.kayitol.setObjectName("kayitol")
        self.horizontalLayout.addWidget(self.kayitol)
        self.iptal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.iptal.setFont(font)
        self.iptal.setObjectName("iptal")
        self.horizontalLayout.addWidget(self.iptal)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 611, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.adLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adLabel.setFont(font)
        self.adLabel.setObjectName("adLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.adLabel)
        self.ad = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ad.setFont(font)
        self.ad.setObjectName("ad")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ad)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.soyad = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.soyad.setFont(font)
        self.soyad.setObjectName("soyad")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.soyad)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 169, 611, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.cinsiyet = QtWidgets.QGroupBox(self.layoutWidget_2)
        self.cinsiyet.setMinimumSize(QtCore.QSize(231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cinsiyet.setFont(font)
        self.cinsiyet.setTitle("")
        self.cinsiyet.setObjectName("cinsiyet")
        self.bayan = QtWidgets.QRadioButton(self.cinsiyet)
        self.bayan.setGeometry(QtCore.QRect(30, 10, 82, 21))
        self.bayan.setMinimumSize(QtCore.QSize(82, 17))
        self.bayan.setObjectName("bayan")
        self.bay = QtWidgets.QRadioButton(self.cinsiyet)
        self.bay.setGeometry(QtCore.QRect(110, 10, 82, 21))
        self.bay.setMinimumSize(QtCore.QSize(82, 17))
        self.bay.setObjectName("bay")
        self.diger = QtWidgets.QRadioButton(self.cinsiyet)
        self.diger.setGeometry(QtCore.QRect(180, 10, 82, 21))
        self.diger.setMinimumSize(QtCore.QSize(82, 17))
        self.diger.setObjectName("diger")
        self.gridLayout.addWidget(self.cinsiyet, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setMinimumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.medenidurum = QtWidgets.QGroupBox(self.layoutWidget_2)
        self.medenidurum.setMinimumSize(QtCore.QSize(231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.medenidurum.setFont(font)
        self.medenidurum.setTitle("")
        self.medenidurum.setObjectName("medenidurum")
        self.evli = QtWidgets.QRadioButton(self.medenidurum)
        self.evli.setGeometry(QtCore.QRect(30, 20, 82, 17))
        self.evli.setMinimumSize(QtCore.QSize(82, 17))
        self.evli.setObjectName("evli")
        self.bekar = QtWidgets.QRadioButton(self.medenidurum)
        self.bekar.setGeometry(QtCore.QRect(90, 20, 82, 17))
        self.bekar.setMinimumSize(QtCore.QSize(82, 17))
        self.bekar.setObjectName("bekar")
        self.dul = QtWidgets.QRadioButton(self.medenidurum)
        self.dul.setGeometry(QtCore.QRect(170, 20, 82, 17))
        self.dul.setMinimumSize(QtCore.QSize(82, 17))
        self.dul.setObjectName("dul")
        self.gridLayout.addWidget(self.medenidurum, 1, 1, 1, 1)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 300, 611, 371))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.mail = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mail.setFont(font)
        self.mail.setObjectName("mail")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mail)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.mailtekrar = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mailtekrar.setFont(font)
        self.mailtekrar.setObjectName("mailtekrar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mailtekrar)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sifre = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sifre.setFont(font)
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre.setObjectName("sifre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sifre)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.aciklama = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.aciklama.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aciklama.setFont(font)
        self.aciklama.setMouseTracking(False)
        self.aciklama.setTabChangesFocus(False)
        self.aciklama.setUndoRedoEnabled(True)
        self.aciklama.setAcceptRichText(False)
        self.aciklama.setOpenExternalLinks(False)
        self.aciklama.setObjectName("aciklama")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.aciklama)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.checkBox_okudum = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_okudum.setFont(font)
        self.checkBox_okudum.setObjectName("checkBox_okudum")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.checkBox_okudum)
        self.sifretekrar = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sifretekrar.setFont(font)
        self.sifretekrar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifretekrar.setObjectName("sifretekrar")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sifretekrar)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.bilgi = QtWidgets.QLabel(self.centralwidget)
        self.bilgi.setGeometry(QtCore.QRect(30, 280, 467, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        self.bilgi.setStyleSheet('QLabel#bilgi {color: red}')
        font.setWeight(75)
        self.bilgi.setFont(font)
        self.bilgi.setAutoFillBackground(True)
        self.bilgi.setText("")
        self.bilgi.setScaledContents(False)
        self.bilgi.setObjectName("bilgi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuGorunum = QtWidgets.QMenu(self.menubar)
        self.menuGorunum.setObjectName("menuGorunum")
        self.menuYardim = QtWidgets.QMenu(self.menubar)
        self.menuYardim.setObjectName("menuYardim")
        self.menuHakkinda = QtWidgets.QMenu(self.menuYardim)
        self.menuHakkinda.setObjectName("menuHakkinda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKayit_Ol = QtWidgets.QAction(MainWindow)
        self.actionKayit_Ol.setObjectName("actionKayit_Ol")
        self.actionIptal = QtWidgets.QAction(MainWindow)
        self.actionIptal.setObjectName("actionIptal")
        self.actionCikis = QtWidgets.QAction(MainWindow)
        self.actionCikis.setObjectName("actionCikis")
        self.actionYakinlastir = QtWidgets.QAction(MainWindow)
        self.actionYakinlastir.setObjectName("actionYakinlastir")
        self.actionUzaklastir = QtWidgets.QAction(MainWindow)
        self.actionUzaklastir.setObjectName("actionUzaklastir")
        self.actionUygulama_Info = QtWidgets.QAction(MainWindow)
        self.actionUygulama_Info.setObjectName("actionUygulama_Info")
        self.menuDosya.addAction(self.actionKayit_Ol)
        self.menuDosya.addAction(self.actionIptal)
        self.menuDosya.addAction(self.actionCikis)
        self.menuGorunum.addAction(self.actionYakinlastir)
        self.menuGorunum.addAction(self.actionUzaklastir)
        self.menuHakkinda.addAction(self.actionUygulama_Info)
        self.menuYardim.addAction(self.menuHakkinda.menuAction())
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuGorunum.menuAction())
        self.menubar.addAction(self.menuYardim.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kayitol.setText(_translate("MainWindow", "Kayit Ol"))
        self.iptal.setText(_translate("MainWindow", "Iptal"))
        self.adLabel.setText(_translate("MainWindow", "Adı:                    "))
        self.label_2.setText(_translate("MainWindow", "Soyadı:"))
        self.label.setText(_translate("MainWindow", "ÜCRETSİZ KAYIT OL VE  BAŞLA!"))
        self.label_3.setText(_translate("MainWindow", "Cinsiyet:"))
        self.bayan.setText(_translate("MainWindow", "Bayan"))
        self.bay.setText(_translate("MainWindow", "Bay"))
        self.diger.setText(_translate("MainWindow", "Diger"))
        self.label_4.setText(_translate("MainWindow", "Medeni Durum:"))
        self.evli.setText(_translate("MainWindow", "Evli"))
        self.bekar.setText(_translate("MainWindow", "Bekar"))
        self.dul.setText(_translate("MainWindow", "Dul"))
        self.label_5.setText(_translate("MainWindow", "Mail Adres:"))
        self.label_6.setText(_translate("MainWindow", "Mail Adres Tekrar:"))
        self.label_8.setText(_translate("MainWindow", "Şifre:"))
        self.aciklama.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Raleway\'; font-size:12pt; font-weight:296; color:#524a58; background-color:#ffffff;\">Is bu kullanici sözlesmesi ve Web Sitesinde yer alan diger kurallar ... tarafindan sunulan hizmetlere iliskin sart ve kosullari ve Web Sitesinin kullanilmasina iliskin kurallari duzenlemektedir. Kullanicinin, Web Sitesi uzerinden Hizmet Talebi veya Meslek Profili olustururken isbu Sozlesmeyi onayladigi veya Web Sitesinden yararlanmaya basladigi andan itibaren isbu Sozlesmeye uymayi taahhut ettigi kabul edilir. Kosullarin sizin icin uygun olmamasi halinde lütfen Web Sitesini ve sunulan hizmetleri </span><span style=\" font-family:\'Raleway\'; font-size:12pt; font-weight:600; color:#524a58; background-color:#ffffff;\">kullanmayiniz.</span></p></body></html>"))
        self.checkBox_okudum.setText(_translate("MainWindow", "Kullanıcı Sözleşmesini ve Davranış Kurallarını okudum ve kabul ediyorum."))
        self.label_7.setText(_translate("MainWindow", "Şifre Tekrar: "))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuGorunum.setTitle(_translate("MainWindow", "Gorunum"))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardim"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkinda"))
        self.actionKayit_Ol.setText(_translate("MainWindow", "Kayit Ol"))
        self.actionKayit_Ol.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionIptal.setText(_translate("MainWindow", "Iptal"))
        self.actionIptal.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionCikis.setText(_translate("MainWindow", "Cikis"))
        self.actionCikis.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionYakinlastir.setText(_translate("MainWindow", "Yakinlastir"))
        self.actionYakinlastir.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionUzaklastir.setText(_translate("MainWindow", "Uzaklastir"))
        self.actionUzaklastir.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionUygulama_Info.setText(_translate("MainWindow", "Uygulama Info"))

        self.kayitol.clicked.connect(self.kayit)
        self.iptal.clicked.connect(self.iptall)
        self.actionKayit_Ol.triggered.connect(self.kayit)
        self.actionIptal.triggered.connect(self.iptall)
        self.actionCikis.triggered.connect(self.cikis)
        self.actionUzaklastir.triggered.connect(self.uzaklas)
        self.actionYakinlastir.triggered.connect(self.yakinlas)
        self.actionUygulama_Info.triggered.connect(self.hakkinda)

        if self.checkBox_okudum.isChecked():
            self.aciklama.setReadOnly(False)
        else:
            self.aciklama.setReadOnly(True)
    def hakkinda(self):
        import sys
        self.app=QtWidgets.QApplication([])
        self.Ikinci = QtWidgets.QWidget()
        self.ui = Ui_Ikinci()
        self.ui.setupUi(self.Ikinci)
        self.Ikinci.show()
        self.app.exec_()

    def cikis(self):
        app.quit()
    def baglanti(self):
        vt = sqlite3.connect("database.db")
        self.cursor = vt.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kullanici (ad TEXT, soyad TEXT,cinsiyet TEXT, medenidurum TEXT, mail TEXT, sifre TEXT)")
        vt.commit()
    def kayit(self):
        
        self.bilgi.setText("")
        self.bilgi2.setText("")
        if self.bekar.isChecked()==True:
            self.medenihal="Bekar"
        elif self.evli.isChecked()==True:
            self.medenihal="Evli"
        elif self.dul.isChecked()==True:
            self.medenihal="Dul"
        else:
            self.medenihal="None"

        if self.bay.isChecked()==True:
            self.cins="Bay"
        elif self.bayan.isChecked()==True:
            self.cins="Bayan"
        elif self.diger.isChecked()==True:
            self.cins="Diger"
        else:
            self.cins="None"
        
        if self.mail.text()!= self.mailtekrar.text() and self.sifre.text()!=self.sifretekrar.text():
            self.bilgi.setText("* Mail Adresleri ve Sifreler Uyusmuyor")
        elif self.sifre.text()!=self.sifretekrar.text():
            self.bilgi.setText("* Sifreler Uyusmuyor")
        elif self.mail.text()!=self.mailtekrar.text():
            self.bilgi.setText("* Mail Adresleri Uyusmuyor")
        else:
            self.bilgi.setText("")
            if not self.checkBox_okudum.isChecked()==True:
                self.bilgi.setText("Kullanici sozlesmesini onaylamalisiniz.")
            else:
                self.bilgi.setText("")
        self.baglanti()
        self.cursor.execute("Select * From kullanici Where mail = ?", (self.mail.text(),))
        data = self.cursor.fetchall()
        if len(data) == 0 and len(self.bilgi.text())==0 and len(self.bilgi2.text())==0 and self.checkBox_okudum.isChecked()==True:  
            vt = sqlite3.connect("database.db")
            self.cursor = vt.cursor()
            self.cursor.execute("Insert into kullanici values (?,?,?,?,?,?)",(self.ad.text(),self.soyad.text(),self.cins,self.medenihal,self.mail.text(),self.sifre.text(),))
            self.bilgi2.setText("KAYIT BASARILI..")
            vt.commit()
            vt.close()
        elif len(data)>0:
            self.bilgi2.setText("KAYIT BASARISIZ..")
            self.bilgi.setText("* Bu mail daha once kullanilmis...")
    
    def iptall(self):
        self.bilgi.setText("")
        self.bilgi2.setText("")
        self.ad.clear()
        self.soyad.clear()
        self.mail.clear()
        self.mailtekrar.clear()
        self.sifretekrar.clear()
        self.sifre.clear()
        self.checkBox_okudum.setChecked(False)
        self.bay.setChecked(False)
        self.bayan.setChecked(False)
        self.diger.setChecked(False)
        self.evli.setChecked(False)
        self.bekar.setChecked(False)
        self.dul.setChecked(False)
 
    def uzaklas(self):
        MainWindow.resize(500,500)
    def yakinlas(self):
        MainWindow.resize(1000,1000)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle("KULLANICI KAYIT PENCERESI")
    ui.baglanti()
    sys.exit(app.exec_())