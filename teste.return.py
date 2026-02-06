def lin():
    print("=" * 40)
#usando return
def somar(a, b):
    resultado = a + b
    return resultado
soma = somar(5, 3)
print(soma)
lin()

#Quando você não usa return
def somar(a, b):
    resultado = a + b
    print(resultado)
soma = somar(5, 3)
print(soma)
lin()

#Função que só executa (print)
def somar(a, b):
    print(a + b)

x = somar(5, 3)
print("Valor em x:", x)
lin()

#Função que retorna
def somar(a, b):
    return a + b
x = somar(5, 3)
print("Valor em x:", x)
lin()
lin()
