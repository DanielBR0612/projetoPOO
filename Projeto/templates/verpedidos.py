import streamlit as st
import pandas as pd
from views import View
import time
import json

class VerPedidos:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2 = st.tabs(["Pedidos", "Excluir"])
        with tab1: VerPedidos.listar()
        with tab2: VerPedidos.excluir()

    def listar():
        produtos = View.pedido_listar()
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
    @staticmethod
    def inserir():
            with open('pedidos.json', 'r') as f:
                data = json.load(f)
     

    @classmethod
    def excluir(cls):
        produtos = View.pedido_listar()
        if len(produtos) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                View.pedido_excluir(op.id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()