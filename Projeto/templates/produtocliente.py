import streamlit as st
import pandas as pd
from views import View
import time

class ProdutoCliente:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1: ProdutoCliente.listar()
        with tab2: ProdutoCliente.inserir()

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
        idproduto = View.produto_listar()
        id_produto = st.selectbox("Informe o id da categoria", idproduto)

        if st.button("Inserir"):
            View.inserir_carrinho(idproduto)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        idcategoria = View.categoria_listar()
        produto = View.produto_listar()
        if len(produto) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de produto", produto)
            descricao = st.text_input("Informe o novo descricao do cliente", op.descricao)
            preco = st.text_input("Informe o novo e-mail", op.preco)
            estoque = st.text_input("Informe o novo estoque", op.estoque)
            categoria = st.selectbox("Informe a nova categoria", idcategoria)
            if st.button("Atualizar"):
                View.produto_atualizar(op.id, descricao, preco, estoque, categoria.id)
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