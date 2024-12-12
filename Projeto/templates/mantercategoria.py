import streamlit as st
import pandas as pd
from views import View
import time

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    def listar():
        clientes = View.categoria_listar()
        if len(Categorias) == 0: 
            st.write("Nenhuma categoria cadastrado")
        else:    
            #for obj in clientes: st.write(obj)
            dic = []
            for obj in categorias: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        categoria_id = st.text_input("Informe a descrição: ")
        descricao = st.text_input("Informe o preço: ")

        if st.button("Inserir"):
            View.categoria_inserir(categoria_id, descricao)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categoria = View.categoria_listar()
        if len(clientes) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.text_input("Atualização de categoria", Categorias)
            categoria_id = st.text_input("Informe o novo categoria_id do cliente", op.categoria_id)
            descricao = st.text_input("Informe o novo e-mail", op.descricao)
            if st.button("Atualizar"):
                View.categoria_atualizar(op.categoria_id, categoria_id)
                st.success("Categoria atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Produtos = View.produto_listar()
        if len(Produtos) == 0: 
            st.write("Nenhuma categoria cadastrado")
        else:
            op = st.selectbox("Exclusão de categoria", Categorias)
            if st.button("Excluir"):
                View.categoria_excluir(op.categoria_id)
                st.success("Categoria excluído com sucesso")
                time.sleep(2)
                st.rerun()
