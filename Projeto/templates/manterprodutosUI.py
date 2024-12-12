import streamlit as st
import pandas as pd
from views import View
from templates.mantercategoriaUI import ManterCategoriaUI
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produto = View.produto_listar()
        if len(produto) == 0: 
            st.write("Nenhum produto cadastrado")
        else:    
            #for obj in produto: st.write(obj)
            dic = []
            for obj in produto: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição: ")
        preco = st.text_input("Informe o preço: ")
        estoque = st.text_input("Informe o estoque: ")
        id_categoria = st.selectbox("Informe o id da categoria", id_categoria)

        if st.button("Inserir"):
            View.produto_inserir(descricao, preco, estoque, categoria)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produto = View.cliente_listar()
        if len(produto) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.text_input("Atualização de produto", Produtos)
            descricao = st.text_input("Informe o novo descricao do cliente", op.descricao)
            preco = st.text_input("Informe o novo e-mail", op.preco)
            estoque = st.text_input("Informe o novo estoque", op.estoque)
            categoria = st.selectbox("Informe a nova categoria", op.categoria)
            if st.button("Atualizar"):
                View.cliente_atualizar(op.id, descricao, preco, estoque, categoria)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Produtos = View.produto_listar()
        if len(Produtos) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", Produtos)
            if st.button("Excluir"):
                View.produto_excluir(op.id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
