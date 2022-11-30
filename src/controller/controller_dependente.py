import pandas as pd
from model.dependente import Dependente
from conexion.mongo_queries import MongoQueries


class Controller_Dependente:

  def __init__(self):
    self.mongo = MongoQueries()

  def inserir_dependente(self) -> Dependente:

    self.mongo.connect()

    COD_DEPENDENTE = input("Codigo (Novo): ")

    if self.verifica_existencia_dependente(COD_DEPENDENTE):

      COD_DEPENDENTE = input("Codigo (Novo): ")
      funcionario = input("Funcionario (Novo): ")
      CPF_DEPENDENTE = input("CPF (Novo): ")
      NOME_DEPENDENTE = input("Cargo (Novo): ")
      SEXO_DEPENDENTE = input("Sexo (Novo): ")

      self.mongo.db["dependente"].insert_one({
        "COD_DEPENDENTE": COD_DEPENDENTE,
        "funcionario": funcionario,
        "CPF_DEPENDENTE": CPF_DEPENDENTE,
        "NOME_DEPENDENTE": NOME_DEPENDENTE,
        "NOME_DEPENDENTE": NOME_DEPENDENTE
      })

      df_dependente = self.recupera_dependente(COD_DEPENDENTE)

      novo_dependente = Dependente(df_dependente.COD_DEPENDENTE.values[0], df_dependente.funcionario.values[0], df_dependente.CPF_DEPENDENTE.values[0], 
            df_dependente.NOME_DEPENDENTE.values[0],df_dependente.SEXO_DEPENDENTE.values[0])

      print(novo_dependente.to_string())
      self.mongo.close()

      return novo_dependente
    else:
      self.mongo.close()
      print(f"O Código {COD_DEPENDENTE} já está cadastradO.")
      return None

  def atualizar_dependente(self) -> Dependente:

    self.mongo.connect()
    COD_DEPENDENTE = input("Código do dependente que deseja alterar: ")

    if not self.verifica_existencia_dependente(COD_DEPENDENTE):

      novo_COD_DEPENDENTE= input("Matricula (Novo): ")
      novo_CPF_DEPENDENTE= input("CPF (Novo): ")
      novo_NOVO_DEPENDENTE= input("Cargo (Novo): ")
      novo_SEXO_DEPENDENTE = input("Sexo (Novo): ")

      self.mongo.db["Dependentes"].update_one(
        {"COD_DEPENDENTE": f"{COD_DEPENDENTE}"},
        {"$set": {
          "COD_DEPENDENTE": novo_COD_DEPENDENTE
        }}, {"CPF_DEPENDENTE": f"{novo_CPF_DEPENDENTE}"},
        {"$set": {
          "CPF_DEPENDENTE": novo_CPF_DEPENDENTE
        }}, {"NOME_DEPENDENTE": f"{novo_NOVO_DEPENDENTE}"},
        {"$set": {
          "NOME_DEPENDENTE": novo_NOVO_DEPENDENTE
        }}, {"SEXO_DEPENDENTE": f"{novo_SEXO_DEPENDENTE}"},
        {"$set": {
          "SEXO_DEPENDENTE": novo_SEXO_DEPENDENTE
        }})

      df_dependente = self.recupera_dependente(COD_DEPENDENTE)

      dependente_atualizado = Dependente(
        df_dependente.COD_DEPENDENTE.values[0],
        df_dependente.CPF_DEPENDENTE.values[0],
        df_dependente.NOME_DEPENDENTE.values[0],
        df_dependente.SEXO_DEPENDENTE.values[0])

      print(dependente_atualizado.to_string())
      self.mongo.close()

      return dependente_atualizado
    else:
      self.mongo.close()
      print(f"O código {COD_DEPENDENTE} não existe.")
      return None

  def excluir_dependente(self):

    self.mongo.connect()
    COD_DEPENDENTE = input("A matrícula do dependente que deseja excluir: ")
    CPF_DEPENDENTE = input("O CPF do dependente que deseja excluir")
    NOME_DEPENDENTE = input("O Nome do dependente que deseja excluir")
    SEXO_DEPENDENTE = input("O Sexo do dependente que deseja excluir")

    if not self.verifica_existencia_dependente(COD_DEPENDENTE):

      df_dependente = self.recupera_dependente(COD_DEPENDENTE)

      self.mongo.db["dependentes"].delete_one(
        {"COD_DEPENDENTE": f"{COD_DEPENDENTE}"},
        {"CPF_DEPENDENTE": f"{CPF_DEPENDENTE}"},
        {"NOME_DEPENDENTE": f"{NOME_DEPENDENTE}"},
        {"SEXO_DEPENDENTE": f"{SEXO_DEPENDENTE}"})

      dependente_excluido = Dependente(df_dependente.COD_DEPENDENTE.values[0],
                                       df_dependente.CPF_DEPENDENTE.values[0],
                                       df_dependente.NOME_DEPENDENTE.values[0],
                                       df_dependente.SEXO_DEPENDENTE.values[0])
      self.mongo.close()

      print("Dependente excluído com sucesso!")
      print(dependente_excluido.to_string())
    else:
      self.mongo.close()
      print(f"O código{COD_DEPENDENTE} não existe.")

  def verifica_existencia_dependente(self,
                                     COD_DEPENDENTE: int = None,
                                     external: bool = False) -> bool:
    if external:

      self.mongo.connect()

    df_dependente = pd.DataFrame(self.mongo.db["dependente"].find(
      {"COD_DEPENDENTE": f"{COD_DEPENDENTE}"}, {
        "COD_DEPENDENTE": 1,
        "CPF_DEPENDENTE": 1,
        "NOME_DEPENDENTE": 1,
        "SEXO_DEPENDENTE": 1,
        "_id": 0,
      }))

    if external:

      self.mongo.close()

    return df_dependente.empty

  def recupera_dependente(self,
                          COD_DEPENDENTE: int = None,
                          external: bool = False) -> pd.DataFrame:
    if external:

      self.mongo.connect()

    df_dependente = pd.DataFrame(
      list(self.mongo.db["dependentes"].find(
        {"COD_DEPENDENTE": f"{COD_DEPENDENTE}"}, {
          "COD_DEPENDENTE": 1,
          "CPF_DEPENDENTE": 1,
          "NOME_DEPENDENTE": 1,
          "SEXO_DEPENDENTE": 1,
          "_id": 0
        })))

    if external:

      self.mongo.close()

    return df_dependente
