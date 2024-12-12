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
        Categorias = View.categoria_listar()
        if len(Categorias) == 0: 
            st.write("Nenhuma categoria cadastrado")
        else:    
            
            dic = []
            for obj in Categorias: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição: ")

        if st.button("Inserir"):
            View.categoria_inserir(descricao)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categoria = View.categoria_listar()
        if len(categoria) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de categoria", categoria)
            descricao = st.text_input("Informe a nova descricao", op.descricao)
            if st.button("Atualizar"):
                View.categoria_atualizar(op.id, descricao)
                st.success("Categoria atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Categorias = View.categoria_listar()
        if len(Categorias) == 0: 
            st.write("Nenhuma categoria cadastrado")
        else:
            op = st.selectbox("Exclusão de categoria", Categorias)
            if st.button("Excluir"):
                View.categoria_excluir(op.id)
                st.success("Categoria excluído com sucesso")
                time.sleep(2)
                st.rerun()
