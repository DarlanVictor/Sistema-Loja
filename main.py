from PySide6.QtWidgets import(QApplication,QMainWindow,QWidget,QMessageBox,QTableWidgetItem)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import DataBase
from ui_funcoes import consulta_cnpj
import psycopg2
import pandas as pd



class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.checkLogin)
    

    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.checarUsuario(self.txt_user.text().upper(), self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "usuário":
            self.w= MainWindow(autenticado.lower())
            self.w.show()
            self.close()
        else:
            self.label_2.setText("Dados inválidos")



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro")

        if user.lower() == "usuário":
            self.btn_pg_cadastro.setVisible(False)

        # paginas do sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_fornecedores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_fornecedores))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_produtos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cad_produto))
        self.btn_clientes.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_cliente))


        self.btn_cadastrar.clicked.connect(self.adicionarUsuario)

        #preencher automaticamente os dados cnpj
        self.txt_cnpj_contr.editingFinished.connect(self.consultarApi)

        self.btn_cadforn.clicked.connect(self.cadastrarFornecedor)

        self.btn_alterar_for.clicked.connect(self.atualizarFornecedor)

        self.btn_excluir_for.clicked.connect(self.deletarFornecedor)

        self.btn_gerar_excel.clicked.connect(self.gerar_excel_fornecedor)

        #
        self.btn_cad_cliente.clicked.connect(self.adicionarCliente)

        self.btn_alterar_cliente.clicked.connect(self.atualizarCliente)

        self.btn_excluir_cliente.clicked.connect(self.deletarCliente)

        self.btn_excel_cliente.clicked.connect(self.gerar_excel_cliente)
        #

        self.btn_cad_produto.clicked.connect(self.adicionarPoduto)

        self.btn_alterar_produto.clicked.connect(self.atualizarProduto)

        self.btn_excluir_produto.clicked.connect(self.deletarProduto)

        self.btn_excel_produto.clicked.connect(self.gerar_excel_produto)

        
        self.buscarFornecedor()
        self.buscarCliente()
        self.buscarProduto()

        # checar as senhas e inserir o usuário
    def adicionarUsuario(self):
        if self.txt_senha.text() != self.txt_confirmar.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senha divergente")
            msg.setText("Senha inválida")
            msg.exec()
            return None
        
        nome = self.txt_nome.text()
        username = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.inserirUsuario(nome,username,password,access)
        db.close_connection()
        #QMessageBox faz a janela de mensagens
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()
        # zera as caixas de texto
        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_confirmar.setText("")

    def consultarApi(self):
        campos = consulta_cnpj(self.txt_cnpj_contr.text())

        self.txt_nome_contr.setText(campos[0])
        self.txt_logradouro_contr.setText(campos[1])
        self.txt_num_contr.setText(campos[2])
        self.txt_complemento_contr.setText(campos[3])
        self.txt_bairro_contr.setText(campos[4])
        self.txt_municipio_contr.setText(campos[5])
        self.txt_uf_contr.setText(campos[6])
        self.txt_cep_contr.setText(campos[7].replace('.', '').replace('-',''))
        self.txt_telefone_contr.setText(campos[8].replace('(', '').replace('-', '').replace(')',''))
        self.txt_email_contr.setText(campos[9])

    def cadastrarFornecedor(self):
        db = DataBase()
        db.conecta()

        cnpj = self.txt_cnpj_contr.text()
        nome, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email = consulta_cnpj(cnpj)

        fullDataSet = (cnpj, nome, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email)

    # cadastrar no banco de dados
        resp = db.registrarFornecedor(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro realizado com sucesso!")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
            db.close_connection()
            return
        
    def buscarFornecedor(self):
        db = DataBase()
        db.conecta()
        result = db.verFornecedores()
        self.table_fornec.clearContents()
        self.table_fornec.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.table_fornec.setItem(row, column,QTableWidgetItem(str(data)))

        db.close_connection()

    def atualizarFornecedor(self):

        dados = []
        update_dados = []

        for row in range(self.table_fornec.rowCount()):
            for column in range(self.table_fornec.columnCount()):
                dados.append(self.table_fornec.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #ATUALIZAR DADOS NO BANCO
        db = DataBase()
        db.conecta() 

        for emp in update_dados:
            db.atualizar_Fornecedor(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.table_fornec.reset()
        self.buscarFornecedor()

    def deletarFornecedor(self):

        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.table_fornec.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.removerFornecedor(cnpj)
            self.buscarFornecedor()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("FORNECEDORES")
            msg.setText(result)
            msg.exec()

        db.close_connection()


    def gerar_excel_fornecedor(self):

        cnx = psycopg2.connect(dbname="system", user="postgres", password="postgres", host="localhost", port="5432")


        empresas = pd.read_sql_query("""SELECT * FROM Fornecedores""", cnx)

        empresas.to_excel("Fornecedores.xlsx", sheet_name='fornecedores', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def adicionarCliente(self):
        cpf = self.txt_cpf_cliente.text()
        nome = self.txt_nome_cliente.text()
        endereco = self.txt_endereco_cliente.text()
        numero = self.txt_num_cliente.text()
        complemento = self.txt_complemento_cliente.text()
        bairro = self.txt_bairro_cliente.text()
        municipio = self.txt_municipio_cliente.text()
        uf = self.txt_uf_cliente.text()
        cep = self.txt_cep_cliente.text()
        telefone = self.txt_telefone_cliente.text()
        email = self.txt_email_cliente.text()

        db = DataBase()
        db.conecta()
        db.inserirCliente(cpf,nome,endereco,numero,complemento,bairro,municipio,uf,cep,telefone,email)
        db.close_connection()
        #QMessageBox faz a janela de mensagens
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Cadastro de Cliente")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()
        # zera as caixas de texto
        self.txt_cpf_cliente.setText("")
        self.txt_nome_cliente.setText("")
        self.txt_endereco_cliente.setText("")
        self.txt_num_cliente.setText("")
        self.txt_complemento_cliente.setText("")
        self.txt_bairro_cliente.setText("")
        self.txt_municipio_cliente.setText("")
        self.txt_uf_cliente.setText("")
        self.txt_cep_cliente.setText("")
        self.txt_telefone_cliente.setText("")
        self.txt_email_cliente.setText("")
        

    def buscarCliente(self):
        db = DataBase()
        db.conecta()
        result = db.verClientes()
        self.table_cliente.clearContents()
        self.table_cliente.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.table_cliente.setItem(row, column,QTableWidgetItem(str(data)))

        db.close_connection()

    def atualizarCliente(self):

        dados = []
        update_dados = []

        for row in range(self.table_cliente.rowCount()):
            for column in range(self.table_cliente.columnCount()):
                dados.append(self.table_cliente.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #ATUALIZAR DADOS NO BANCO
        db = DataBase()
        db.conecta() 

        for i in update_dados:
            db.atualizar_Cliente(tuple(i))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.table_cliente.reset()
        self.buscarCliente()

    def deletarCliente(self):

        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.table_cliente.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.remover_Cliente(id)
            self.buscarCliente()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("CLIENTES")
            msg.setText(result)
            msg.exec()

        db.close_connection()

    def gerar_excel_cliente(self):

        cnx = psycopg2.connect(dbname="system", user="postgres", password="postgres", host="localhost", port="5432")


        clientes = pd.read_sql_query("""SELECT * FROM Clientes""", cnx)

        clientes.to_excel("Clientes.xlsx", sheet_name='clientes', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def adicionarPoduto(self):
        nome_marca = self.txt_nome_produto.text()
        descricao = self.txt_desc_produto.text()
        quantidade = self.txt_quant_produto.text()
        preco_custo = self.txt_custo_produto.text()
        preco_venda = self.txt_venda_prod.text()
        categoria = self.txt_cat_produto.text()
        unidade_medida = self.cb_unid_produto.currentText()
        fornecedor = self.txt_forn_produto.text()


        db = DataBase()
        db.conecta()
        db.inserir_Produto(nome_marca,descricao,quantidade,preco_custo,preco_venda,categoria,unidade_medida,fornecedor)
        db.close_connection()
        #QMessageBox faz a janela de mensagens
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Cadastro de Produto")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()
        # zera as caixas de texto
        
        self.txt_nome_produto.setText("")
        self.txt_desc_produto.setText("")
        self.txt_quant_produto.setText("")
        self.txt_custo_produto.setText("")
        self.txt_venda_prod.setText("")
        self.txt_cat_produto.setText("")
        self.txt_forn_produto.setText("")


    def buscarProduto(self):
        db = DataBase()
        db.conecta()
        result = db.ver_Produto()
        self.table_produtos.clearContents()
        self.table_produtos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.table_produtos.setItem(row, column,QTableWidgetItem(str(data)))

        db.close_connection()

    def atualizarProduto(self):

        dados = []
        update_dados = []

        for row in range(self.table_produtos.rowCount()):
            for column in range(self.table_produtos.columnCount()):
                dados.append(self.table_produtos.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #ATUALIZAR DADOS NO BANCO
        db = DataBase()
        db.conecta() 

        for i in update_dados:
            db.atualizar_Produto(tuple(i))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.table_produtos.reset()
        self.buscarProduto()

    def deletarProduto(self):

        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.table_produtos.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.remover_Produto(codigo)
            self.buscarProduto()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("PRODUTOS")
            msg.setText(result)
            msg.exec()

        db.close_connection()


    def gerar_excel_produto(self):

        cnx = psycopg2.connect(dbname="system", user="postgres", password="postgres", host="localhost", port="5432")


        produtos = pd.read_sql_query("""SELECT * FROM Produtos""", cnx)

        produtos.to_excel("Produtos.xlsx", sheet_name='produtos', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.criarTabelaFornecedores()
    db.close_connection()

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
