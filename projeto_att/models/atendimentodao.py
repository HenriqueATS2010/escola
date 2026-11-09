from models.dao import DAO
from models.atendimento import Atendimento
import json

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__()
        self._arquivo = "atendimentos.json"
        self._abrir()

    def _abrir(self):
        try:
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Atendimento.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Atendimento.to_json, indent = 2)
        arquivo.close()