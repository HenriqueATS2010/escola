from models.dao import DAO
from models.horario import Horario
import json

class HorarioDAO(DAO):
    def __init__(self):
        super().__init__()
        self._arquivo = "horarios.json"
        self._abrir()

    def _abrir(self):
        try:
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Horario.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Horario.to_json, indent = 2)
        arquivo.close()