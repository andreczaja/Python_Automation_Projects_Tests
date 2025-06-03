from tkinter import *
from tkinter import ttk
import sqlite3
import os

os.system('cls')

root = Tk()

class Funcs():
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.select_clientes()
    def conecta_bd(self):
        self.conn = sqlite3.connect("bd.clientes")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def MontaTabela(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_clientes(
            cod INTEGER PRIMARY KEY,
            nome CHAR(50) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(30))
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    def select_clientes(self):
        self.treeview.delete(*self.treeview.get_children())
        self.conecta_bd()
        linhas_bd = self.cursor.execute("""SELECT cod, nome, telefone, cidade FROM table_clientes
                                             ORDER BY nome ASC""")
        for i in linhas_bd:
            self.treeview.insert("",END, values=i)
        self.desconecta_bd()

    def filtrar_clientes(self):
        self.variaveis()
        # Limpa o Treeview
        self.treeview.delete(*self.treeview.get_children())
        
        # Conecta ao banco de dados
        self.conecta_bd()
        
        # Base da consulta e lista para armazenar parâmetros
        query = "SELECT cod, nome, telefone, cidade FROM table_clientes WHERE 1=1"
        parametros = []

        if self.nome.strip():
            query += " AND nome LIKE ?"
            parametros.append(f"%{self.nome.strip()}%")
        if self.telefone.strip():
            query += " AND telefone LIKE ?"
            parametros.append(f"%{self.telefone.strip()}%")
        if self.cidade.strip():
            query += " AND cidade LIKE ?"
            parametros.append(f"%{self.cidade.strip()}%")

        # Ordena os resultados pelo nome
        query += " ORDER BY nome ASC"
        
        # Executa a consulta com os parâmetros
        linhas_filtradas = self.cursor.execute(query, parametros)
        
        # Insere os resultados no Treeview
        for i in linhas_filtradas:
            self.treeview.insert("", "end", values=i)

        # Desconecta do banco de dados
        self.desconecta_bd()


    def add_cliente(self):
        self.variaveis()
        if self.nome != "":
            self.conecta_bd()
            self.cursor.execute("""
            INSERT INTO table_clientes (nome, telefone, cidade) VALUES (?, ?, ?)""", (self.nome, self.telefone,self.cidade))
            self.conn.commit()
            self.desconecta_bd()
            self.select_clientes()
            self.limpa_tela()
    
    def DoubleClick_cliente(self, event):
        self.limpa_tela()
        for i in self.treeview.selection():
            print(self.treeview.item(i,'values'))
            col1,col2,col3,col4 = self.treeview.item(i,'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        print(self.codigo)
        self.cursor.execute("DELETE FROM table_clientes WHERE cod = ?", (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_clientes()

    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        print(self.codigo)
        self.cursor.execute("UPDATE table_clientes SET nome = ?, telefone = ?, cidade = ? WHERE cod = ?", (self.nome,self.telefone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_clientes()

    
        
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame_1()
        self.lista_frame_2()
        self.MontaTabela()
        self.select_clientes()
        self.Menus()
        self.root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Itens")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(False, False)
    def frames(self):
        self.frame_1 = Frame(self.root, bd=40, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_1.place(relx= 0.05, rely=0.05, relwidth=0.9, relheight=0.45)
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx= 0.05, rely=0.525, relwidth=0.9, relheight=0.45)
    
    def widgets_frame_1(self):
        # botões
        self.btn_limpar = Button(self.frame_1, text="Limpar", bd=2, bg= '#107db2', fg='white', font = ('verdana', 8 ,'bold'), command= self.limpa_tela)
        self.btn_limpar.place(relx=0.17, rely=0.05, relheight=0.15, relwidth=0.1)
        self.btn_buscar = Button(self.frame_1, text="Buscar", bd=2, bg= '#107db2', fg='white', font = ('verdana', 8 ,'bold'), command= self.filtrar_clientes)
        self.btn_buscar.place(relx=0.276, rely=0.05, relheight=0.15, relwidth=0.1)
        self.btn_cadastrar_novo = Button(self.frame_1, text="Novo", bd=2, bg= '#107db2', fg='white', font = ('verdana', 8 ,'bold'), command=self.add_cliente)
        self.btn_cadastrar_novo.place(relx=0.64, rely=0.05, relheight=0.15, relwidth=0.12)
        self.btn_alterar = Button(self.frame_1, text="Alterar", bd=2, bg= '#107db2', fg='white', font = ('verdana', 8 ,'bold'),  command=self.alterar_cliente)
        self.btn_alterar.place(relx=0.77, rely=0.05, relheight=0.15, relwidth=0.1)
        self.btn_apagar = Button(self.frame_1, text="Apagar", bd=2, bg= '#107db2', fg='white', font = ('verdana', 8 ,'bold'), command=self.deleta_cliente)
        self.btn_apagar.place(relx=0.88, rely=0.05, relheight=0.15, relwidth=0.1)

        # labels
        self.lb_codigo = Label(self.frame_1, text="Código", bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=-0.048, rely=-0.12, relheight=0.17, relwidth=0.12)
        self.lb_nome = Label(self.frame_1, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=-0.048, rely=0.45, relheight=0.17, relwidth=0.12)
        self.lb_telefone = Label(self.frame_1, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=-0.04, rely=0.83, relheight=0.17, relwidth=0.12)
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.56, rely=0.83, relheight=0.17, relwidth=0.12)

        # entries
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=-0.025, rely=0.07, relheight=0.17, relwidth=0.12)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=-0.025, rely=0.60, relheight=0.17, relwidth=1)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=-0.025, rely=0.98, relheight=0.17, relwidth=0.40)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.58, rely=0.98, relheight=0.17, relwidth=0.40)

    def lista_frame_2(self):
        self.treeview = ttk.Treeview(self.frame_2, height=3, column=("col1","col2","col3","col4"))
        self.treeview.heading("#0", text="")
        self.treeview.heading("#1", text="Codigo")
        self.treeview.heading("#2", text="Nome")
        self.treeview.heading("#3", text="Telefone")
        self.treeview.heading("#4", text="Cidade")
        self.treeview.place(relx=0,rely=0.05, relwidth=0.95, relheight=0.9)

        self.treeview.column("#0", width=1)
        self.treeview.column("#1", width=50)
        self.treeview.column("#2", width=200)
        self.treeview.column("#3", width=50)
        self.treeview.column("#4", width=100)

        self.scroollist = Scrollbar(self.frame_2, orient='vertical')
        self.treeview.configure(yscroll=self.scroollist.set)
        self.scroollist.place(relx= 0.95, rely= 0.05, relwidth=0.03, relheight=0.9)
        self.treeview.bind("<Double-1>",self.DoubleClick_cliente)
    
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu=filemenu)
        menubar.add_cascade(label= "Sobre", menu=filemenu2)

        menubar.after_idle

        filemenu.add_command(label="Sair", command= Quit)
        filemenu2.add_command(label="Limpa Cliente", command= self.limpa_tela)
        

Application()
        





