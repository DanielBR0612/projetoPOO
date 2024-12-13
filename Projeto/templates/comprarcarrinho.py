import streamlit as st
import pandas as pd
from views import View
import time

class ComprarCarrinho:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1: ComprarCarrinho.listar()
        with tab2: ComprarCarrinho.inserir()

    def listar():
        produto = View.listar_carrinho()
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
            View.inserir_carrinho(id_produto)
            st.success("Produto inserido com sucesso")
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