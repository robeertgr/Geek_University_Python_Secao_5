"""
Estruturas lógicas: and (e), or (ou), not (não) e is (é).

Operadores unários:
    - not
Operadores binários:
    - and, or, is

# Regras de funcionamento
# Para o 'and', ambos os valores precisam ser True
# Para o 'or', um ou outro valor precisa ser True
# Para o 'not', o valor do booleano é invertido
"""

ativo = True
logado = True

"""
if ativo and logado:
    print("Bem vindo usuário.")
else:
    print("Usuário inativo no sistema.")
"""

""""
if not ativo:
    print("Você precisa ativar sua conta.")
else:
    print("Bem vindo usuário.")

print(not True)
"""

if ativo is False:
    print("Você precisa ativar sua conta.")
else:
    print("Bem vindo usuário.")
