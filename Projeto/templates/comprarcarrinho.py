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
                # Corrige objetos aninhados ou strings JSON
                dic = []
                for obj in produtos:
                    if isinstance(obj, str):  # Verifica se é uma string JSON
                        try:
                            obj = json.loads(obj)  # Converte a string em dicionário
                        except json.JSONDecodeError:
                            st.error("Erro ao decodificar JSON.")
                            continue
                    elif hasattr(obj, "__dict__"):  # Caso obj tenha um atributo __dict__
                        obj = obj.__dict__
                    dic.append(obj)

                # Converte para DataFrame
                df = pd.json_normalize(dic)  # Normaliza dados aninhados em colunas
                st.dataframe(df)
            
    @staticmethod
    def inserir():
        try:
            with open('carrinhos.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            st.error("Arquivo 'carrinhos.json' não encontrado.")
            return
        except json.JSONDecodeError:
            st.error("Erro ao ler o arquivo JSON.")
            return


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