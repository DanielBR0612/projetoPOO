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
        id_produto = st.selectbox("Iforme o produto que deseja comprar", idproduto)

        if st.button("Inserir"):
            View.inserir_carrinho(id_produto)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()
