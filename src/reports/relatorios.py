from conexion.mongo_queries import MongoQueries
from pymongo import ASCENDING, DESCENDING
import pandas as pd

class Relatorio:
    def __init__(self):
        pass
 
    def get_relatorio_funcionario(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["funcionario"].find({},
                                                    {"matricula": 1,                                                    
                                                     "cpf_func": 1,
                                                     "cargo": 1,                                              
                                                     "sexo_func": 1,
                                                     }).sort("nome_func", ASCENDING)
        df_funcionario = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_funcionario)
        input("Insira enter para sair do relatório de funcionarios")


    def get_relatorio_dependente_por_funcionario(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db['dependente'].aggregate(
                                                [{
                                                    '$group': {
                                                        'cod_dep': '$matricula', 
                                                        'nome_dep': {
                                                            '$sum': 1
                                                        }
                                                    }
                                                }, {
                                                    '$project': {
                                                        'nome_dep': '$cod_dep', 
                                                        'cpf_dep': 1, 
                                                        'sexo_dep': 0
                                                    }
                                                }, {
                                                    '$lookup': {
                                                        'from': 'dependentes', 
                                                        'localField': 'cod_dep', 
                                                        'foreignField': 'cod_dep', 
                                                        'as': 'funcionarios'
                                                    }
                                                }, {
                                                    '$unwind': {
                                                        'path': '$funcionarios'
                                                    }
                                                }, {
                                                    '$project': {
                                                        'nome_dep': 1, 
                                                        'cpf_dep': 1, 
                                                        'dependentes': '$dependente.cod_dep', 
                                                        'sexo_dep': 0
                                                    }
                                                }, {
                                                    '$lookup': {
                                                        'from': 'funcionario', 
                                                        'localField': 'funcionario', 
                                                        'foreignField': 'matricula', 
                                                        'as': 'funcionario'
                                                    }
                                                }, {
                                                    '$unwind': {
                                                        'path': '$funcionario'
                                                    }
                                                }]
                                                    )




        df_dependente_funcionario = pd.DataFrame(list(query_result))
        # Fecha a conexão com o Mongo
        mongo.close()
        # Exibe o resultado
        print(df_dependente_funcionario[["dependente", "funcionario"]])
        input("Insira enter para sair do Relatório de dependentes por funcionarios")
    
    
    
    
