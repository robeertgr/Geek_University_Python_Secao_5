"""
Estruturas condicionais
if, else e elif
"""

idade = 18

"""
# Estrutura condicional if em C
if (idade < 18){
    printf("Menor de idade");
}
"""

if idade < 18:
    print("Menor de idade")
    print(idade)
elif idade == 18:
    print("Tem 18 anos")
    print(idade)
else:
    print("Maior de idade")
    print(idade)
