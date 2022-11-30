import pandas as pd
from model.funcionario import Funcionario
from conexion.mongo_queries import MongoQueries

class Controller_Funcionario:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_fucionario(self) -> Funcionario:
        self.mongo.connect()

        matricula = input("Matricula (Novo): ")

        if self.verifica_existencia_funcionario(matricula):
            
            matricula = input("Matricula (Novo): ")
            CPF_FUNC = input("CPF (Novo): ")
            NOME_FUNC = input("Nome (Novo): ")
            CARGO = input("Cargo (Novo): ")
            SEXO_FUNC = input("Sexo (Novo): ")

            self.mongo.db["funcionarios"].insert_one({"matricula": matricula, "CPF_FUNC": CPF_FUNC,"NOME_FUNC": NOME_FUNC, "CARGO": CARGO,"SEXO_FUNC": SEXO_FUNC})
            
            df_funcionario = self.recupera_funcionario(matricula)
            
            novo_funcionario = Funcionario(df_funcionario.matricula.values[0], df_funcionario.CPF_FUNC.values[0], df_funcionario.NOME_FUNC.values[0], 
            df_funcionario.CARGO.values[0],df_funcionario.SEXO_FUNC.values[0])
            
            print(novo_funcionario.to_string())
            self.mongo.close()
            
            return novo_funcionario
        else:
            self.mongo.close()
            print(f"A matrícula {matricula} já está cadastrada.")
            return None

    def atualizar_funcionario(self) -> Funcionario:
        
        self.mongo.connect()

       
        matricula = input("Matrícula do funcionário que deseja alterar: ")

        
        if not self.verifica_existencia_funcionario(matricula):
            
            novo_matricula = input("Matricula (Novo): ")
            novo_CPF_FUNC = input("CPF (Novo): ")
            novo_NOME_FUNC = input("Nome (Novo): ")
            novo_CARGO = input("Cargo (Novo): ")
            novo_SEXO_FUNC = input("Sexo (Novo): ")
            
            self.mongo.db["funcionarios"].update_one({"matricula": f"{matricula}"}, {"$set": {"matricula": novo_matricula}}, {"CPF_FUNC": f"{novo_CPF_FUNC}"}, 
            {"$set": {"CPF_FUNC": novo_CPF_FUNC}}, {"NOME_FUNC": f"{novo_NOME_FUNC}"}, {"$set": {"NOME_FUNC": novo_NOME_FUNC}}, {"CARGO": f"{novo_CARGO}"}, 
            {"$set": {"CARGO": novo_CARGO}}, {"SEXO_FUNC": f"{novo_SEXO_FUNC}"}, {"$set": {"SEXO_FUNC": novo_SEXO_FUNC}})
            
            df_funcinario = self.recupera_funcionario(matricula)
            
            funcionario_atualizado = Funcionario(df_funcinario.matricula.values[0], df_funcinario.CPF_FUNC.values[0], df_funcinario.NOME_FUNC.values[0],
            df_funcinario.CARGO.values[0], df_funcinario.SEXO_FUNC.values[0])
           
            print(funcionario_atualizado.to_string())
            self.mongo.close()
            
            return funcionario_atualizado
        else:
            self.mongo.close()
            print(f"A matrícula {matricula} não existe.")
            return None

    def excluir_funcionario(self):
        
        self.mongo.connect()
        matricula = input("A matrícula do funcionário que deseja excluir: ")
        CPF_FUNC = input ("O CPF do funcionário que deseja excluir")
        NOME_FUNC = input ("O Nome do funcionário que deseja excluir")
        CARGO = input ("O Cargo do funcionário que deseja excluir")
        SEXO_FUNC = input ("O Sexo do funcionário que deseja excluir")

        
        if not self.verifica_existencia_funcionario(matricula):            
            
            df_funcionario = self.recupera_funcionario(matricula)
            
            self.mongo.db["funcionarios"].delete_one({"matricula":f"{matricula}"},{"CPF_FUNC":f"{CPF_FUNC}"},{"NOME_FUNC":f"{NOME_FUNC}"},
            {"CARGO":f"{CARGO}"},{"SEXO_FUNC":f"{SEXO_FUNC}"})
            
            funcionario_excluido = Funcionario(df_funcionario.matricula.values[0], df_funcionario.CPF_FUNC.values[0], df_funcionario.NOME_FUNC.values[0], 
            df_funcionario.CARGO.values[0], df_funcionario.SEXO_FUNC.values[0])
            self.mongo.close()
            
            print("Funcionário removido com sucesso!")
            print(funcionario_excluido.to_string())
        else:
            self.mongo.close()
            print(f"A matrícula{matricula} não existe.")

    def verifica_existencia_funcionario(self, matricula:int=None, external:bool=False) -> bool:
        if external:
            
            self.mongo.connect()

        df_funcionario = pd.DataFrame(self.mongo.db["funcionarios"].find({"matricula":f"{matricula}"},{"matricula": 1,"CPF_FUNC": 1, "NOME_FUNC": 1, 
        "CARGO": 1, "SEXO_FUNC": 1, "_id": 0}))

        if external:
            
            self.mongo.close()

        return df_funcionario.empty

    def recupera_funcionario(self, matricula:int=None, external:bool=False) -> pd.DataFrame:
        if external:
           
            self.mongo.connect()

        df_funcionario = pd.DataFrame(list(self.mongo.db["funcionarios"].find({"matricula":f"{matricula}"}, {"matricula": 1, "CPF_FUNC": 1, "NOME_FUNC": 1,
        "CARGO": 1, "SEXO_FUNC": 1, "_id": 0})))
        
        if external:
          
            self.mongo.close()

        return df_funcionario
