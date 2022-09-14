class ClasseA:

    def __init__(self, attr1:int, attr2:str):
        try:
            self.__validate__(ClasseA.__init__, attr1, attr2)
        except Exception as erro:
            print(erro)
            exit()

        self.attr1 = attr1
        self.attr2 = attr2

    def __validate__(self, method, *args):
        i = 0
        for key, value in method.__annotations__.items():
            if value != type(args[i]):
                msg = f"Parâmetro {key}:{value} atribuido com {type(args[i])}"
                raise Exception(msg)    
            i+=1

