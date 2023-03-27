import psycopg2

class DataBase():
    def __init__(self, name= "system", user="postgres", password="postgres", host="localhost", port=5432):
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def conecta(self):
        self.connection = psycopg2.connect(
            dbname=self.name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def criarTabelaFornecedores(self):
        cursor = self.connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Fornecedores(
            
            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            PRIMARY KEY(CNPJ)
            );
        ''')

    #def registrarFornecedor(self, fullDataSet):
    #    cursor = self.connection.cursor()
    #    try:
    #        cursor.execute('''INSERT INTO Fornecedores VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', fullDataSet)
    #        self.connection.commit()
    #        return "OK"
    #    except:
    #        return "Erro"
    
    def registrarFornecedor(self, fullDataSet):
        campos_tabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qntd = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s")
        cursor = self.connection.cursor()
        try:
            cursor.execute(f'''INSERT INTO Fornecedores ({", ".join(campos_tabela)})
            VALUES({qntd})''', fullDataSet)
            self.connection.commit()
            return "OK"
        except:
            return "Erro"

        
    def verFornecedores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Fornecedores ORDER BY NOME")
            fornecedores = cursor.fetchall()
            return fornecedores
        except:
            pass

    def removerFornecedor(self,id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Fornecedores WHERE CNPJ = '{id}' ")
            self.connection.commit()
            return "Cadastro de fornecedor removido com sucesso!"
        except:
            return "Erro ao excluir registro!"

    def atualizar_Fornecedor(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f'''UPDATE Fornecedores set
            CNPJ = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO = '{fullDataSet[3]}',
            COMPLEMENTO = '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UF = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}'

            WHERE CNPJ = '{fullDataSet[0]}'
        ''')
        self.connection.commit()

    def criarTabelaProdutos(self):
        cursor = self.connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Produtos(
            
            CODIGO INT GENERATED ALWAYS AS IDENTITY,
            NOME_MARCA TEXT,
            DESCRICAO TEXT,
            QUANTIDADE INT,
            PRECO_CUSTO MONEY,
            PRECO_VENDA MONEY,
            CATEGORIA TEXT,
            UNIDADE_MEDIDA TEXT,
            FORNECEDOR TEXT,
            PRIMARY KEY(CODIGO)
            );
        ''')

    def criarTabelaClientes(self):
        cursor = self.connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Clientes(
            
            ID INT GENERATED ALWAYS AS IDENTITY,
            CPF TEXT,
            NOME TEXT,
            ENDERECO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            PRIMARY KEY(ID)
            );
        ''')

    def inserirCliente(self,cpf,nome,endereco,numero,complemento,bairro,municipio,uf,cep,telefone,email):
        try:
            cursor= self.connection.cursor()
            cursor.execute('''
                INSERT INTO Clientes(cpf,nome,endereco,numero,complemento,bairro,municipio,uf,cep,telefone,email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''',(cpf,nome,endereco,numero,complemento,bairro,municipio,uf,cep,telefone,email))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def verClientes(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Clientes ORDER BY ID")
            clientes = cursor.fetchall()
            return clientes
        except:
            pass

    def atualizar_Cliente(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f'''UPDATE Clientes set
            CPF = '{fullDataSet[1]}',
            NOME = '{fullDataSet[2]}',
            ENDERECO = '{fullDataSet[3]}',
            NUMERO = '{fullDataSet[4]}',
            COMPLEMENTO = '{fullDataSet[5]}',
            BAIRRO = '{fullDataSet[6]}',
            MUNICIPIO = '{fullDataSet[7]}',
            UF = '{fullDataSet[8]}',
            CEP = '{fullDataSet[9]}',
            TELEFONE = '{fullDataSet[10]}',
            EMAIL = '{fullDataSet[11]}'
            WHERE ID = '{fullDataSet[0]}'
        ''')
        self.connection.commit()

    def remover_Cliente(self,id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Clientes WHERE ID = '{id}' ")
            self.connection.commit()
            return "Cadastro de cliente removido com sucesso!"
        except:
            return "Erro ao excluir registro!"
        
    def inserir_Produto(self,nome_marca,descricao,quantidade,preco_custo,preco_venda,categoria,unidade_medida,fornecedor):
        try:
            cursor= self.connection.cursor()
            cursor.execute('''
                INSERT INTO Produtos(nome_marca,descricao,quantidade,preco_custo,preco_venda,categoria,unidade_medida,fornecedor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            ''',(nome_marca,descricao,quantidade,preco_custo,preco_venda,categoria,unidade_medida,fornecedor))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def atualizar_Produto(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f'''UPDATE Produtos set

            NOME_MARCA = '{fullDataSet[1]}',
            DESCRICAO = '{fullDataSet[2]}',
            QUANTIDADE = '{fullDataSet[3]}',
            PRECO_CUSTO = '{fullDataSet[4]}',
            PRECO_VENDA = '{fullDataSet[5]}',
            CATEGORIA = '{fullDataSet[6]}',
            UNIDADE_MEDIDA = '{fullDataSet[7]}',
            FORNECEDOR = '{fullDataSet[8]}'
            WHERE CODIGO = '{fullDataSet[0]}'
        ''')
        self.connection.commit()


    def ver_Produto(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos ORDER BY CODIGO")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def remover_Produto(self,codigo):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Produtos WHERE CODIGO = '{codigo}' ")
            self.connection.commit()
            return "Cadastro de produto removido com sucesso!"
        except:
            return "Erro ao excluir registro!"


    def criarTabelaUsuario(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    name TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                );
            ''')
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def inserirUsuario(self,name,username,password,access):
        try:
            cursor= self.connection.cursor()
            cursor.execute('''
                INSERT INTO users(name,username,password,access) VALUES(%s,%s,%s,%s)
            ''',(name,username,password,access))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')
        
    def checarUsuario(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM users;
            
            ''')
            for linha in cursor.fetchall():
                if linha[2].upper() == username.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
                
                elif linha[2].upper() == username.upper() and linha[3] == password and linha[4] == "Usuário":
                    return "Usuário"
                
                else:
                    continue
            return "Sem acesso"
        except:
            pass

