from utils import config

class SplashScreen:

    def __init__(self):
        self.created_by =  "Alcides Souza Mergulhão\n"+"Bruno Barbosa Fernandes\n"+"Caio Siquara Nascimento Rodrigues\n"+"Filipe Freitas Alves Rosa\n"+"Pedro Henrique de Souza Almeida"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_documents_count(self, collection_name):
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                 TABELA DE REGISTROS                    
        ########################################################
        #
        #  TOTAL DE REGISTROS:                                    
        #      1 - FUNCIONÁRIOS:        {str(self.get_documents_count(collection_name="FUNCIONÁRIOS")).rjust(5)}
        #      2 - DEPENDENTES:         {str(self.get_documents_count(collection_name="DEPENDENTES")).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """