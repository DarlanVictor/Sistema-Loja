# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 719)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(60, 60))
        self.btn_home.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon = QIcon()
        icon.addFile(u"imags/diagram-06_24511.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(60, 60))
        self.btn_pg_cadastro.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.btn_pg_cadastro.setFont(font1)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"imags/business_application_addmale_useradd_insert_add_user_client_2312 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pg_cadastro.setIcon(icon1)
        self.btn_pg_cadastro.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_pg_cadastro)

        self.btn_pg_produtos = QPushButton(self.centralwidget)
        self.btn_pg_produtos.setObjectName(u"btn_pg_produtos")
        self.btn_pg_produtos.setMinimumSize(QSize(60, 60))
        self.btn_pg_produtos.setFont(font)
        self.btn_pg_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_produtos.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"imags/businesspackage_downloadpackage_box_dowload_negoci_2336.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pg_produtos.setIcon(icon2)
        self.btn_pg_produtos.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_pg_produtos)

        self.btn_clientes = QPushButton(self.centralwidget)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(60, 60))
        self.btn_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clientes.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"imags/11547449341548234989-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clientes.setIcon(icon3)
        self.btn_clientes.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_clientes)

        self.btn_fornecedores = QPushButton(self.centralwidget)
        self.btn_fornecedores.setObjectName(u"btn_fornecedores")
        self.btn_fornecedores.setMinimumSize(QSize(60, 60))
        self.btn_fornecedores.setFont(font)
        self.btn_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fornecedores.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"imags/diagram-64_24453.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fornecedores.setIcon(icon4)
        self.btn_fornecedores.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_fornecedores)

        self.btn_sobre = QPushButton(self.centralwidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(60, 60))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"imags/information_info_1565.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sobre.setIcon(icon5)
        self.btn_sobre.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.centralwidget)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(60, 60))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 127);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"imags/diagram-07_24510.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_contato.setIcon(icon6)
        self.btn_contato.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.pg_fornecedores = QWidget()
        self.pg_fornecedores.setObjectName(u"pg_fornecedores")
        self.verticalLayout_8 = QVBoxLayout(self.pg_fornecedores)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_fornecedores)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.tabWidget.setFont(font2)
        self.pg_fornecedores_2 = QWidget()
        self.pg_fornecedores_2.setObjectName(u"pg_fornecedores_2")
        self.verticalLayout_7 = QVBoxLayout(self.pg_fornecedores_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.pg_fornecedores_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.table_fornec = QTableWidget(self.pg_fornecedores_2)
        if (self.table_fornec.columnCount() < 11):
            self.table_fornec.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_fornec.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_fornec.setObjectName(u"table_fornec")

        self.verticalLayout_5.addWidget(self.table_fornec)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame = QFrame(self.pg_fornecedores_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar_excel = QPushButton(self.frame)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(100, 30))
        self.btn_gerar_excel.setFont(font2)
        self.btn_gerar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 255, 127);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_gerar_excel)

        self.btn_alterar_for = QPushButton(self.frame)
        self.btn_alterar_for.setObjectName(u"btn_alterar_for")
        self.btn_alterar_for.setMinimumSize(QSize(100, 30))
        self.btn_alterar_for.setFont(font2)
        self.btn_alterar_for.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_for.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_alterar_for)

        self.btn_excluir_for = QPushButton(self.frame)
        self.btn_excluir_for.setObjectName(u"btn_excluir_for")
        self.btn_excluir_for.setMinimumSize(QSize(100, 30))
        self.btn_excluir_for.setFont(font2)
        self.btn_excluir_for.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_for.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_excluir_for)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.pg_fornecedores_2, "")
        self.pg_cadfornecedores = QWidget()
        self.pg_cadfornecedores.setObjectName(u"pg_cadfornecedores")
        self.verticalLayout_11 = QVBoxLayout(self.pg_cadfornecedores)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_17 = QLabel(self.pg_cadfornecedores)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.label_17)

        self.frame_2 = QFrame(self.pg_cadfornecedores)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(300, -1, 300, -1)
        self.txt_cnpj_contr = QLineEdit(self.frame_2)
        self.txt_cnpj_contr.setObjectName(u"txt_cnpj_contr")
        self.txt_cnpj_contr.setMinimumSize(QSize(0, 25))
        self.txt_cnpj_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cnpj_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj_contr, 4, 0, 1, 1)

        self.txt_nome_contr = QLineEdit(self.frame_2)
        self.txt_nome_contr.setObjectName(u"txt_nome_contr")
        self.txt_nome_contr.setMinimumSize(QSize(0, 25))
        self.txt_nome_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_nome_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome_contr, 4, 1, 1, 2)

        self.txt_logradouro_contr = QLineEdit(self.frame_2)
        self.txt_logradouro_contr.setObjectName(u"txt_logradouro_contr")
        self.txt_logradouro_contr.setMinimumSize(QSize(0, 25))
        self.txt_logradouro_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_logradouro_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro_contr, 5, 0, 1, 3)

        self.txt_num_contr = QLineEdit(self.frame_2)
        self.txt_num_contr.setObjectName(u"txt_num_contr")
        self.txt_num_contr.setMinimumSize(QSize(0, 25))
        self.txt_num_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_num_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_num_contr, 6, 0, 1, 1)

        self.txt_complemento_contr = QLineEdit(self.frame_2)
        self.txt_complemento_contr.setObjectName(u"txt_complemento_contr")
        self.txt_complemento_contr.setMinimumSize(QSize(0, 25))
        self.txt_complemento_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_complemento_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento_contr, 6, 1, 1, 1)

        self.txt_cep_contr = QLineEdit(self.frame_2)
        self.txt_cep_contr.setObjectName(u"txt_cep_contr")
        self.txt_cep_contr.setMinimumSize(QSize(0, 25))
        self.txt_cep_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cep_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep_contr, 7, 2, 1, 1)

        self.txt_telefone_contr = QLineEdit(self.frame_2)
        self.txt_telefone_contr.setObjectName(u"txt_telefone_contr")
        self.txt_telefone_contr.setMinimumSize(QSize(0, 25))
        self.txt_telefone_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_telefone_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone_contr, 9, 0, 1, 1)

        self.txt_bairro_contr = QLineEdit(self.frame_2)
        self.txt_bairro_contr.setObjectName(u"txt_bairro_contr")
        self.txt_bairro_contr.setMinimumSize(QSize(0, 25))
        self.txt_bairro_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.txt_bairro_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro_contr, 6, 2, 1, 1)

        self.txt_municipio_contr = QLineEdit(self.frame_2)
        self.txt_municipio_contr.setObjectName(u"txt_municipio_contr")
        self.txt_municipio_contr.setMinimumSize(QSize(0, 25))
        self.txt_municipio_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_municipio_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio_contr, 7, 0, 1, 1)

        self.txt_uf_contr = QLineEdit(self.frame_2)
        self.txt_uf_contr.setObjectName(u"txt_uf_contr")
        self.txt_uf_contr.setMinimumSize(QSize(0, 25))
        self.txt_uf_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_uf_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf_contr, 7, 1, 1, 1)

        self.txt_email_contr = QLineEdit(self.frame_2)
        self.txt_email_contr.setObjectName(u"txt_email_contr")
        self.txt_email_contr.setMinimumSize(QSize(0, 25))
        self.txt_email_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_email_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email_contr, 9, 1, 1, 2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 27))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.btn_cadforn = QPushButton(self.frame_2)
        self.btn_cadforn.setObjectName(u"btn_cadforn")
        self.btn_cadforn.setMinimumSize(QSize(0, 25))
        self.btn_cadforn.setMaximumSize(QSize(300, 28))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_cadforn.setFont(font3)
        self.btn_cadforn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadforn.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadforn.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.gridLayout.addWidget(self.btn_cadforn, 10, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.tabWidget.addTab(self.pg_cadfornecedores, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_fornecedores)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.verticalLayout.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_cad_produto = QWidget()
        self.pg_cad_produto.setObjectName(u"pg_cad_produto")
        self.horizontalLayout_2 = QHBoxLayout(self.pg_cad_produto)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_cad_produto = QTabWidget(self.pg_cad_produto)
        self.tb_cad_produto.setObjectName(u"tb_cad_produto")
        self.tb_cad_produto.setFont(font2)
        self.pg_list_produto = QWidget()
        self.pg_list_produto.setObjectName(u"pg_list_produto")
        self.verticalLayout_10 = QVBoxLayout(self.pg_list_produto)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_16 = QLabel(self.pg_list_produto)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_21.addWidget(self.label_16)

        self.table_produtos = QTableWidget(self.pg_list_produto)
        if (self.table_produtos.columnCount() < 9):
            self.table_produtos.setColumnCount(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        self.table_produtos.setObjectName(u"table_produtos")

        self.verticalLayout_21.addWidget(self.table_produtos)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.verticalLayout_20.addLayout(self.verticalLayout_22)


        self.horizontalLayout_11.addLayout(self.verticalLayout_20)

        self.frame_4 = QFrame(self.pg_list_produto)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.btn_excel_produto = QPushButton(self.frame_4)
        self.btn_excel_produto.setObjectName(u"btn_excel_produto")
        self.btn_excel_produto.setMinimumSize(QSize(100, 30))
        self.btn_excel_produto.setFont(font2)
        self.btn_excel_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_produto.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 255, 127);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_23.addWidget(self.btn_excel_produto)

        self.btn_alterar_produto = QPushButton(self.frame_4)
        self.btn_alterar_produto.setObjectName(u"btn_alterar_produto")
        self.btn_alterar_produto.setMinimumSize(QSize(100, 30))
        self.btn_alterar_produto.setFont(font2)
        self.btn_alterar_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_produto.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_23.addWidget(self.btn_alterar_produto)

        self.btn_excluir_produto = QPushButton(self.frame_4)
        self.btn_excluir_produto.setObjectName(u"btn_excluir_produto")
        self.btn_excluir_produto.setMinimumSize(QSize(100, 30))
        self.btn_excluir_produto.setFont(font2)
        self.btn_excluir_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_produto.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_23.addWidget(self.btn_excluir_produto)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_3)


        self.horizontalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.tb_cad_produto.addTab(self.pg_list_produto, "")
        self.pg_cad_produtos = QWidget()
        self.pg_cad_produtos.setObjectName(u"pg_cad_produtos")
        self.verticalLayout_24 = QVBoxLayout(self.pg_cad_produtos)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_25 = QLabel(self.pg_cad_produtos)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 50))
        self.label_25.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_24.addWidget(self.label_25)

        self.frame_5 = QFrame(self.pg_cad_produtos)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(300, -1, 300, -1)
        self.txt_forn_produto = QLineEdit(self.frame_5)
        self.txt_forn_produto.setObjectName(u"txt_forn_produto")
        self.txt_forn_produto.setMinimumSize(QSize(0, 25))
        self.txt_forn_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_forn_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_forn_produto, 7, 2, 1, 1)

        self.txt_desc_produto = QLineEdit(self.frame_5)
        self.txt_desc_produto.setObjectName(u"txt_desc_produto")
        self.txt_desc_produto.setMinimumSize(QSize(0, 25))
        self.txt_desc_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_desc_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_desc_produto, 5, 0, 1, 3)

        self.txt_quant_produto = QLineEdit(self.frame_5)
        self.txt_quant_produto.setObjectName(u"txt_quant_produto")
        self.txt_quant_produto.setMinimumSize(QSize(0, 25))
        self.txt_quant_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_quant_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_quant_produto, 6, 0, 1, 1)

        self.txt_custo_produto = QLineEdit(self.frame_5)
        self.txt_custo_produto.setObjectName(u"txt_custo_produto")
        self.txt_custo_produto.setMinimumSize(QSize(0, 25))
        self.txt_custo_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_custo_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_custo_produto, 6, 1, 1, 1)

        self.txt_venda_prod = QLineEdit(self.frame_5)
        self.txt_venda_prod.setObjectName(u"txt_venda_prod")
        self.txt_venda_prod.setMinimumSize(QSize(0, 25))
        self.txt_venda_prod.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.txt_venda_prod.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_venda_prod, 6, 2, 1, 1)

        self.txt_cat_produto = QLineEdit(self.frame_5)
        self.txt_cat_produto.setObjectName(u"txt_cat_produto")
        self.txt_cat_produto.setMinimumSize(QSize(0, 25))
        self.txt_cat_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cat_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_cat_produto, 7, 0, 1, 1)

        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 27))

        self.gridLayout_3.addWidget(self.label_26, 0, 1, 1, 1)

        self.btn_cad_produto = QPushButton(self.frame_5)
        self.btn_cad_produto.setObjectName(u"btn_cad_produto")
        self.btn_cad_produto.setMinimumSize(QSize(0, 25))
        self.btn_cad_produto.setMaximumSize(QSize(300, 28))
        self.btn_cad_produto.setFont(font3)
        self.btn_cad_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cad_produto.setLayoutDirection(Qt.LeftToRight)
        self.btn_cad_produto.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_cad_produto, 9, 1, 1, 1)

        self.cb_unid_produto = QComboBox(self.frame_5)
        self.cb_unid_produto.addItem("")
        self.cb_unid_produto.addItem("")
        self.cb_unid_produto.addItem("")
        self.cb_unid_produto.setObjectName(u"cb_unid_produto")
        self.cb_unid_produto.setMinimumSize(QSize(0, 25))
        self.cb_unid_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cb_unid_produto, 7, 1, 1, 1)

        self.txt_nome_produto = QLineEdit(self.frame_5)
        self.txt_nome_produto.setObjectName(u"txt_nome_produto")
        self.txt_nome_produto.setMinimumSize(QSize(0, 25))
        self.txt_nome_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_nome_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_nome_produto, 4, 0, 1, 3)


        self.verticalLayout_24.addWidget(self.frame_5)

        self.tb_cad_produto.addTab(self.pg_cad_produtos, "")

        self.horizontalLayout_2.addWidget(self.tb_cad_produto)

        self.Pages.addWidget(self.pg_cad_produto)
        self.page_cliente = QWidget()
        self.page_cliente.setObjectName(u"page_cliente")
        self.horizontalLayout_12 = QHBoxLayout(self.page_cliente)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tabWidget_2 = QTabWidget(self.page_cliente)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font2)
        self.tabWidget_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab_cad_cliente = QWidget()
        self.tab_cad_cliente.setObjectName(u"tab_cad_cliente")
        self.verticalLayout_14 = QVBoxLayout(self.tab_cad_cliente)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_24 = QLabel(self.tab_cad_cliente)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 50))
        self.label_24.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.label_24)

        self.frame_cliente = QFrame(self.tab_cad_cliente)
        self.frame_cliente.setObjectName(u"frame_cliente")
        self.frame_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_cliente.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_cliente)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(300, -1, 300, -1)
        self.txt_nome_cliente = QLineEdit(self.frame_cliente)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setMinimumSize(QSize(0, 25))
        self.txt_nome_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_nome_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nome_cliente, 4, 1, 1, 2)

        self.txt_cpf_cliente = QLineEdit(self.frame_cliente)
        self.txt_cpf_cliente.setObjectName(u"txt_cpf_cliente")
        self.txt_cpf_cliente.setMinimumSize(QSize(0, 25))
        self.txt_cpf_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cpf_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cpf_cliente, 4, 0, 1, 1)

        self.txt_cep_cliente = QLineEdit(self.frame_cliente)
        self.txt_cep_cliente.setObjectName(u"txt_cep_cliente")
        self.txt_cep_cliente.setMinimumSize(QSize(0, 25))
        self.txt_cep_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_cep_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cep_cliente, 7, 2, 1, 1)

        self.txt_endereco_cliente = QLineEdit(self.frame_cliente)
        self.txt_endereco_cliente.setObjectName(u"txt_endereco_cliente")
        self.txt_endereco_cliente.setMinimumSize(QSize(0, 25))
        self.txt_endereco_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_endereco_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_endereco_cliente, 5, 0, 1, 3)

        self.txt_complemento_cliente = QLineEdit(self.frame_cliente)
        self.txt_complemento_cliente.setObjectName(u"txt_complemento_cliente")
        self.txt_complemento_cliente.setMinimumSize(QSize(0, 25))
        self.txt_complemento_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_complemento_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_complemento_cliente, 6, 1, 1, 1)

        self.txt_num_cliente = QLineEdit(self.frame_cliente)
        self.txt_num_cliente.setObjectName(u"txt_num_cliente")
        self.txt_num_cliente.setMinimumSize(QSize(0, 25))
        self.txt_num_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_num_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_num_cliente, 6, 0, 1, 1)

        self.txt_bairro_cliente = QLineEdit(self.frame_cliente)
        self.txt_bairro_cliente.setObjectName(u"txt_bairro_cliente")
        self.txt_bairro_cliente.setMinimumSize(QSize(0, 25))
        self.txt_bairro_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.txt_bairro_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_bairro_cliente, 6, 2, 1, 1)

        self.txt_municipio_cliente = QLineEdit(self.frame_cliente)
        self.txt_municipio_cliente.setObjectName(u"txt_municipio_cliente")
        self.txt_municipio_cliente.setMinimumSize(QSize(0, 25))
        self.txt_municipio_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_municipio_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_municipio_cliente, 7, 0, 1, 1)

        self.txt_uf_cliente = QLineEdit(self.frame_cliente)
        self.txt_uf_cliente.setObjectName(u"txt_uf_cliente")
        self.txt_uf_cliente.setMinimumSize(QSize(0, 25))
        self.txt_uf_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_uf_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_uf_cliente, 7, 1, 1, 1)

        self.txt_telefone_cliente = QLineEdit(self.frame_cliente)
        self.txt_telefone_cliente.setObjectName(u"txt_telefone_cliente")
        self.txt_telefone_cliente.setMinimumSize(QSize(0, 25))
        self.txt_telefone_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_telefone_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_telefone_cliente, 9, 0, 1, 1)

        self.label_4 = QLabel(self.frame_cliente)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 27))

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.btn_cad_cliente = QPushButton(self.frame_cliente)
        self.btn_cad_cliente.setObjectName(u"btn_cad_cliente")
        self.btn_cad_cliente.setMinimumSize(QSize(0, 25))
        self.btn_cad_cliente.setMaximumSize(QSize(300, 28))
        self.btn_cad_cliente.setFont(font3)
        self.btn_cad_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cad_cliente.setLayoutDirection(Qt.LeftToRight)
        self.btn_cad_cliente.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.gridLayout_2.addWidget(self.btn_cad_cliente, 10, 1, 1, 1)

        self.txt_email_cliente = QLineEdit(self.frame_cliente)
        self.txt_email_cliente.setObjectName(u"txt_email_cliente")
        self.txt_email_cliente.setMinimumSize(QSize(0, 25))
        self.txt_email_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_email_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_email_cliente, 9, 1, 1, 2)


        self.verticalLayout_14.addWidget(self.frame_cliente)

        self.tabWidget_2.addTab(self.tab_cad_cliente, "")
        self.tab_list_cliente = QWidget()
        self.tab_list_cliente.setObjectName(u"tab_list_cliente")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_list_cliente)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_5 = QLabel(self.tab_list_cliente)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_17.addWidget(self.label_5)

        self.table_cliente = QTableWidget(self.tab_list_cliente)
        if (self.table_cliente.columnCount() < 12):
            self.table_cliente.setColumnCount(12)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(8, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(9, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(10, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_cliente.setHorizontalHeaderItem(11, __qtablewidgetitem31)
        self.table_cliente.setObjectName(u"table_cliente")

        self.verticalLayout_17.addWidget(self.table_cliente)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.verticalLayout_16.addLayout(self.verticalLayout_18)


        self.horizontalLayout_4.addLayout(self.verticalLayout_16)

        self.frame_3 = QFrame(self.tab_list_cliente)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.btn_excel_cliente = QPushButton(self.frame_3)
        self.btn_excel_cliente.setObjectName(u"btn_excel_cliente")
        self.btn_excel_cliente.setMinimumSize(QSize(100, 30))
        self.btn_excel_cliente.setFont(font2)
        self.btn_excel_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_cliente.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 255, 127);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_excel_cliente)

        self.btn_alterar_cliente = QPushButton(self.frame_3)
        self.btn_alterar_cliente.setObjectName(u"btn_alterar_cliente")
        self.btn_alterar_cliente.setMinimumSize(QSize(100, 30))
        self.btn_alterar_cliente.setFont(font2)
        self.btn_alterar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_cliente.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_alterar_cliente)

        self.btn_excluir_cliente = QPushButton(self.frame_3)
        self.btn_excluir_cliente.setObjectName(u"btn_excluir_cliente")
        self.btn_excluir_cliente.setMinimumSize(QSize(100, 30))
        self.btn_excluir_cliente.setFont(font2)
        self.btn_excluir_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_cliente.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_excluir_cliente)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)

        self.tabWidget_2.addTab(self.tab_list_cliente, "")

        self.horizontalLayout_12.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.page_cliente)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(300, 20, 300, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 25))
        font5 = QFont()
        font5.setPointSize(10)
        self.txt_nome.setFont(font5)
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(300, 20, 300, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMinimumSize(QSize(0, 25))
        self.txt_usuario.setFont(font5)
        self.txt_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(300, 20, 300, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 25))
        self.txt_senha.setFont(font5)
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(300, 20, 300, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.txt_confirmar = QLineEdit(self.pg_cadastro)
        self.txt_confirmar.setObjectName(u"txt_confirmar")
        self.txt_confirmar.setMinimumSize(QSize(0, 25))
        self.txt_confirmar.setMaximumSize(QSize(16777215, 16777215))
        self.txt_confirmar.setFont(font5)
        self.txt_confirmar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.txt_confirmar.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_confirmar)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 5, 0, 0)
        self.label_32 = QLabel(self.pg_cadastro)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_9.addWidget(self.label_32)

        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))
        self.label_11.setMaximumSize(QSize(50, 100))
        self.label_11.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy1)
        self.cb_perfil.setMinimumSize(QSize(200, 25))
        self.cb_perfil.setMaximumSize(QSize(200, 25))
        self.cb_perfil.setFont(font1)
        self.cb_perfil.setCursor(QCursor(Qt.BlankCursor))
        self.cb_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cb_perfil)

        self.label_31 = QLabel(self.pg_cadastro)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_9.addWidget(self.label_31)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 25))
        self.btn_cadastrar.setMaximumSize(QSize(150, 30))
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	border-width: 2px;\n"
"	border-style: outset;\n"
"	border-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"		\n"
"}\n"
"QPushButton:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_13 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_23 = QLabel(self.pg_contato)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_13.addWidget(self.label_23)

        self.label_14 = QLabel(self.pg_contato)
        self.label_14.setObjectName(u"label_14")
        font6 = QFont()
        font6.setPointSize(20)
        self.label_14.setFont(font6)

        self.verticalLayout_13.addWidget(self.label_14)

        self.label_19 = QLabel(self.pg_contato)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_13.addWidget(self.label_19)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_13.addWidget(self.label_21)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.pg_sobre)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 200))
        self.label_15.setFont(font6)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_18 = QLabel(self.pg_sobre)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setBold(False)
        self.label_18.setFont(font7)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setMargin(0)

        self.verticalLayout_12.addWidget(self.label_18)

        self.label_22 = QLabel(self.pg_sobre)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_12.addWidget(self.label_22)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.btn_cadforn.setDefault(False)
        self.tb_cad_produto.setCurrentIndex(1)
        self.btn_cad_produto.setDefault(False)
        self.tabWidget_2.setCurrentIndex(1)
        self.btn_cad_cliente.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText("")
        self.btn_pg_cadastro.setText("")
        self.btn_pg_produtos.setText("")
        self.btn_clientes.setText("")
        self.btn_fornecedores.setText("")
        self.btn_sobre.setText("")
        self.btn_contato.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Fornecedores</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_fornec.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.table_fornec.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.table_fornec.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.table_fornec.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.table_fornec.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.table_fornec.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.table_fornec.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.table_fornec.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.table_fornec.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.table_fornec.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.table_fornec.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_for.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_for.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_fornecedores_2), QCoreApplication.translate("MainWindow", u"Lista de Fornecedores", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CADASTRAR FORNECEDOR</span></p></body></html>", None))
        self.txt_cnpj_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.txt_logradouro_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_num_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_complemento_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_cep_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_bairro_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_municipio_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_uf_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_email_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">FORNECEDOR</span></p></body></html>", None))
        self.btn_cadforn.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pg_cadfornecedores), QCoreApplication.translate("MainWindow", u"Cadastrar Fornecedor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imags/logo_system\"/></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Sistema de Cadastro</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PRODUTOS</span></p></body></html>", None))
        ___qtablewidgetitem11 = self.table_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem12 = self.table_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"NOME E MARCA", None));
        ___qtablewidgetitem13 = self.table_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"DESCRICAO", None));
        ___qtablewidgetitem14 = self.table_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem15 = self.table_produtos.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"PRECO DE CUSTO", None));
        ___qtablewidgetitem16 = self.table_produtos.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"PRECO DE VENDA", None));
        ___qtablewidgetitem17 = self.table_produtos.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"CATEGORIA", None));
        ___qtablewidgetitem18 = self.table_produtos.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"UNIDADE DE MEDIDA", None));
        ___qtablewidgetitem19 = self.table_produtos.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None));
        self.btn_excel_produto.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_produto.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_produto.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tb_cad_produto.setTabText(self.tb_cad_produto.indexOf(self.pg_list_produto), QCoreApplication.translate("MainWindow", u"Lista de Produtos", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CADASTRAR PRODUTO</span></p></body></html>", None))
        self.txt_forn_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None))
        self.txt_desc_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None))
        self.txt_quant_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
        self.txt_custo_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O DE CUSTO", None))
        self.txt_venda_prod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O DE VENDA", None))
        self.txt_cat_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CATEGORIA", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PRODUTO</span></p></body></html>", None))
        self.btn_cad_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cb_unid_produto.setItemText(0, QCoreApplication.translate("MainWindow", u"UNIDADE", None))
        self.cb_unid_produto.setItemText(1, QCoreApplication.translate("MainWindow", u"CAIXA", None))
        self.cb_unid_produto.setItemText(2, QCoreApplication.translate("MainWindow", u"LITROS", None))

        self.txt_nome_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME E MARCA DO PRODUTO", None))
        self.tb_cad_produto.setTabText(self.tb_cad_produto.indexOf(self.pg_cad_produtos), QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CADASTRAR CLIENTE</span></p></body></html>", None))
        self.txt_nome_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_cpf_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_cep_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_endereco_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.txt_complemento_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_num_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_bairro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_municipio_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_uf_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_telefone_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CLIENTE</span></p></body></html>", None))
        self.btn_cad_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.txt_email_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_cad_cliente), QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Clientes</span></p></body></html>", None))
        ___qtablewidgetitem20 = self.table_cliente.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem21 = self.table_cliente.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem22 = self.table_cliente.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem23 = self.table_cliente.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem24 = self.table_cliente.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem25 = self.table_cliente.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem26 = self.table_cliente.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem27 = self.table_cliente.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem28 = self.table_cliente.horizontalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem29 = self.table_cliente.horizontalHeaderItem(9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem30 = self.table_cliente.horizontalHeaderItem(10)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem31 = self.table_cliente.horizontalHeaderItem(11)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_excel_cliente.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_cliente.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_cliente.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_list_cliente), QCoreApplication.translate("MainWindow", u"Lista de clientes", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Confirmar Senha:</span></p></body></html>", None))
        self.txt_confirmar.setText("")
        self.label_32.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Perfil:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_31.setText("")
        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_23.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/18014190591582545595-64.png\"/></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Contatos Suporte</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/11968623911579738440-32.png\"/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">(85)99999-9999</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/15743770351574338605-32.png\"/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">suportcad@gmail.com</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Sobre</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">O sistema de cadastro \u00e9 uma solu\u00e7\u00e3o pr\u00e1tica e eficiente para empresas que precisam gerenciar seus usu\u00e1rios, cadastrando seus produtos e fornecedores no banco de dados postgresql de forma segura, centralizada e organizada. </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Com a ajuda da API, a integra\u00e7\u00e3o com outras ferramentas e sistemas \u00e9 facilitada, o que pode trazer ainda mais benef\u00edcios para a empresa.</span></p></body></html>", None))
        self.label_22.setText("")
    # retranslateUi

