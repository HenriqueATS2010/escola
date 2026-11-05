import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaClienteUI:
    @staticmethod
    def main():
        st.header("Agenda do cliente")
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado.")
            return
        cliente = st.selectbox("Selecione o cliente", clientes)
        horarios = Service.cliente_visualizar_servicos(cliente.get_id())
        if len(horarios) == 0:
            st.write("Esse cliente não possui horários na agenda.")
            return
        linhas = []
        for h in horarios:
            servico = Service.servico_listar_id(h.get_id_servico())
            profissional = Service.profissional_listar_id(h.get_id_profissional())
            linhas.append({
                "ID": h.get_id(),
                "Data e hora": h.get_data().strftime("%d/%m/%Y %H:%M"),
                "Profissional": profissional.get_nome() if profissional != None else "-",
                "Serviço": servico.get_descricao() if servico != None else "-"
            })
        st.dataframe(pd.DataFrame(linhas), hide_index = True, use_container_width = True)