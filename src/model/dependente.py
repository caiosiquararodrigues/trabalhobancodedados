from model.funcionario import Funcionario

class Dependente:
    def __init__(self, 
                 COD_DEP:int=None,
                 funcionario:Funcionario= None,
                 CPF_DEP:str=None,
                 NOME_DEP:str=None,
                 SEXO_DEP:str=None,
                ):
        self.set_COD_DEP(COD_DEP)
        self.set_funcionario(funcionario)
        self.set_CPF_DEP(CPF_DEP)
        self.set_NOME_DEP(NOME_DEP)
        self.set_SEXO_DEP(SEXO_DEP)

    def set_COD_DEP(self, COD_DEP:int):
        self.COD_DEPENDENTE = COD_DEP

    def get_COD_DEP(self) -> int:
        return self.COD_DEP

    def set_funcionario(self, funcionario:Funcionario):
        self.funcionario = funcionario

    def get_funcionario(self) -> Funcionario:
        return self.funcionario
      
    def set_CPF_DEP(self, CPF_DEP:str):
        self.CPF_DEP = CPF_DEP

    def get_CPF_DEP(self) -> Funcionario:
        return self.CPF_DEP

    def set_NOME_DEP(self, NOME_DEP:str):
        self.NOME_DEP = NOME_DEP

    def get_NOME_DEP(self) -> str:
        return self.NOME_DEPE

    def set_SEXO_DEP(self, SEXO_DEP:str):
        self.SEXO_DEP = SEXO_DEP

    def get_SEXO_DEP(self) -> str:
        return self.SEXO_DEP

    def to_string(self) -> str:
        return f"Codigo do dependente: {self.get_COD_DEP()} | Funcionario: {self.get_funcionario().get_NOME_FUNC()} | CPF do dependente:  {self.get_CPF_DEP()} | Nome do dependente: {self.get_COD_DEP()} | Sexo do dependente: {self.get_SEXO_DEP()}"
