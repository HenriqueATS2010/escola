import streamlit as st
import pandas as pd
from service import Service
 
class ListarHorariosNaoConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("Horários não confirmados de hoje")
        horarios = Service.horario_listar_nao_confirmados_hoje()
        if len(horarios) == 0:
            st.write("Nenhum horário pendente de confirmação para hoje.")
            return
        linhas = []
        for h in horarios:
            cliente = Service.cliente_listar_id(h.get_id_cliente())
            servico = Service.servico_listar_id(h.get_id_servico())
            profissional = Service.profissional_listar_id(h.get_id_profissional())
            linhas.append({
                "ID": h.get_id(),
                "Data e hora": h.get_data().strftime("%d/%m/%Y %H:%M"),
                "Cliente": cliente.get_nome() if cliente != None else "-",
                "Serviço": servico.get_descricao() if servico != None else "-",
                "Profissional": profissional.get_nome() if profissional != None else "-"
            })
        st.dataframe(pd.DataFrame(linhas), hide_index = True, use_container_width = True)
 