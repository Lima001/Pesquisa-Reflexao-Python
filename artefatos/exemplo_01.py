# Definição de uma classe que utiliza o modelo reflexivo para validação dos dados
# recebidos durante a inicialização de um objeto. No exemplo em questão, a ação
# executada quando os tipos divergem refere-se ao levantamento de uma excessão.
# Essa excessão (quando ocorre )é capturada pela verificação try/except, e implica
# na finalização do programa

class ClasseA:

    # Inicialização do objeto. Observe como os parâmetros possuem seus tipos anotados
    def __init__(self, attr1:int, attr2:str):
        # Verificar se os tipos dos dados recebidos correspodem com os esperados
        try:
            self.__validate__(ClasseA.__init__, attr1, attr2)
        except Exception as erro:
            # Se não correspondem, exibe-se uma mensagem de erro e o programa é finalizado
            print(erro)
            exit()

        self.attr1 = attr1
        self.attr2 = attr2

    # Método reflexivo de validação de tipos
    def __validate__(self, method, *args):
        i = 0
        for key, value in method.__annotations__.items():
            # Quando o valor recebido diverge do esperado, executa uma ação definida pelo programador
            if value != type(args[i]):
                # Ação definida: Levantar uma excessão como uma mensagem de erro identificado a divergência dos tipos
                msg = f"Parâmetro {key}:{value} atribuido com {type(args[i])}"
                raise Exception(msg)    
            i+=1