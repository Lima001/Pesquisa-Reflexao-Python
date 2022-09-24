# Exemplo similar ao apresentado em exemplo_02.py, porém dessa vez
# cria-se objetos de uma classe que realiza a verificação dos tipos
# ao instanciar um objeto - conforme exemplo_01.py. Ao final do exemplo
# espera-se que seja possível observar que o objeto com tipos incorretos
# não foi criado, e o programa foi finalizado - conforme definição de exemplo
# utilizada na definição da ClasseA.

from exemplo_01 import *

# Objeto intanciado com os tipos corretos/esperados
obja1 = ClasseA(1, "hello")
print(obja1.attr1, obja1.attr2)

# Objeto intanciado com os tipos incorretos, divergindo do esperado
obja2 = ClasseA("hello", "hello")
print(obja2.attr1, obja2.attr2)