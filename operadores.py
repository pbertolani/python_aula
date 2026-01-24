print(1 + 1)

print(10 - 2)

print(4 * 3)

print(12 / 4)

print(12 // 4)

print( 10 % 3)

print(2 ** 3)

print(10 - 5 *2)

print((10 - 5) * 2)

print(10 ** 2 * 2)

print(10 ** (2 * 2))

print(10 / 2 * 4)

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 * produto_2)
print(produto_1 ** produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)

x = 10 + 5 * 4
print(x)

y = (10 + 5) * 4
print(y)

z = 10 / 2 + 25 + 2 - 100 ** 2
print(z)

a = (10 / 2) + (25 + 2) - (100 ** 2)
print(a)

#comparação

#igualdade

saldo = 450
saque = 200

print(saldo == saque)

print(saldo > saque)
print(saldo >= saque)

print(saldo < saque)
print(saldo <= saque)

#atribuição

saldo = 200
print(saldo)

saldo = 200
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo /= 2
print(saldo)

saldo //= 2
print(saldo)

saldo *= 10
print(saldo)

saldo %= 3
print(saldo)

saldo **= 2
print(saldo)

#lógicos

saldo = 1000
saque = 200
limite = 100

saldo >= saque

saque <= limite

saldo >= saque and saque <= limite

saldo >= saque or saque <= limite

#operador negação

contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500"

not ""

#Parenteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

#identidade

curso = "Curso de Python"

nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite

####

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

#Associação

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso

"maçã" not in frutas

200 in saques