from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutosUI import ManterProdutoUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.comprarcarrinho import ComprarCarrinho
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.verpedidos import VerPedidos
from views import View
from templates.produtocliente import ProdutoCliente

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
               
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de produtos", "Cadastro de Categorias"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de produtos": ManterProdutoUI.main()
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Comprar Carrinho", "Ver Meus Pedidos"])
        if op == "Listar Produtos": ProdutoCliente.main()
        if op == "Comprar Carrinho": ComprarCarrinho.main()
        if op == "Ver Meus Pedidos": VerPedidos.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()
    
    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.cliente_admin()
        # monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()
