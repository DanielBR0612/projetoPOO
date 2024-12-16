import streamlit as st
import pandas as pd
from views import View
import time
import json

class ComprarCarrinho:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2 = st.tabs(["Listar", "Excluir"])
        with tab1: ComprarCarrinho.listar()
        with tab2: ComprarCarrinho.excluir()

    def listar():
        produtos = View.listar_carrinho()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for obj in produtos:
                if isinstance(obj, str):  
                    try:
                        obj = json.loads(obj)  
                    except json.JSONDecodeError:
                        st.error("Erro ao decodificar JSON.")
                        continue
                elif hasattr(obj, "__dict__"):  
                    obj = obj.__dict__
                dic.append(obj)

           
            df = pd.json_normalize(dic)  
            st.dataframe(df)

            if st.button("Comprar"):
                for obj in produtos:
                    View.pedido_inserir(obj)
                    View.excluir_carrinho(obj)
                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()

                

    @staticmethod
    def inserir():
            with open('carrinhos.json', 'r') as f:
                data = json.load(f)
      
    

    @classmethod
    def excluir(cls):
        produtos = View.listar_carrinho()
        if len(produtos) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                View.excluir_carrinho(op.id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()