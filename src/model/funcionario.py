class Funcionario:
    def __init__(self, 
                 matricula:int=None,
                 CPF:str=None,
                 NOME_FUNC:str=None,
                 CARGO:str=None,
                 SEXO_FUNC:str=None
                ):
        self.set_matricula(matricula)
        self.set_CPF(CPF)
        self.set_NOME_FUNC(NOME_FUNC)
        self.set_CARGO(CARGO)
        self.set_SEXO_FUNC(SEXO_FUNC)

    def set_matricula(self, matricula:int):
        self.matricula = matricula

    def get_matricula(self) -> int:
        return self.matricula

    def set_CPF(self, CPF:str):
        self.CPF = CPF

    def get_CPF(self) -> str:
        return self.CPF
      
    def set_NOME_FUNC(self, NOME_FUNC:str):
        self.NOME_FUNC = NOME_FUNC

    def get_NOME_FUNC(self) -> str:
        return self.NOME_FUNC

    def set_CARGO(self, CARGO:str):
        self.CARGO = CARGO

    def get_CARGO(self) -> str:
        return self.CARGO

    def set_SEXO_FUNC(self, SEXO_FUNC:str):
        self.SEXO_FUNC = SEXO_FUNC

    def get_SEXO_FUNC(self) -> str:
        return self.SEXO_FUNC

    def to_string(self) -> str:
        return f"Matricula: {self.get_matricula()} | CPF: {self.get_CPF()} | Nome: {self.get_NOME_FUNC()} | Cargo: {self.get_CARGO} | Sexo: {self.get_SEXO_FUNC()}"