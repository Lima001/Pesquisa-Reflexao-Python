# O exemplo em questão demonstra o que acontece quando não utiliza-se
# um mecanismo como o apresentado no exemplo_01.py. Espera-se que ao
# final do exemplo, seja possível observar que ambos os objetos foram
# criados - independetemente dos tipos fornecidos coincidirem com os
# tipos esperados.

# Obs. Esse é o comportamento padrão do Python como uma linguagem dâmicamente tipada.

class ClasseB:

    # Observe que o recurso de anotações, quando não explorado reflexivamente como um metadado
    # serve apenas como mecanismo de documentação.
    def __init__(self, attr1:int, attr2:str):
        self.attr1 = attr1
        self.attr2 = attr2

    def mul_attr1(self):
        self.attr1 *= 2

# Objeto intanciado com os tipos corretos/esperados
objb1 = ClasseB(1, "hello")

# Objeto intanciado com os tipos incorretos, divergindo do esperado
objb2 = ClasseB("hello", 1)

# Invocação de um método que utiliza attr1.
# Observe que da forma que o método foi definido, ele funciona até mesmo
# se o tipo de dado não for conforme o esperado. Isso pode ser um problema!
objb1.mul_attr1()
objb2.mul_attr1()

print(objb1.attr1)
print(objb2.attr1)

    # O que aconteceria se um programador tentasse calcular a média entre os valores
    # armazenados nos atributos attr1 dos dois objetos criados?
    # Caso deseje verificar, descomente a linha abaixo...
    # print((objb1.attr1 + objb2.attr1)/2)

    # Agora imagine um contexto similar, porém para N objetos com N atributos.
    # Um mecanismo que auxilia na verificação de tipos pode ser muito útil e impedir
    # que erros sejam propagados em códigos complexos.