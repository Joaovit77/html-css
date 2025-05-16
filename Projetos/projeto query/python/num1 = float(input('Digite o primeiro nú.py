''' num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
resultado = num1 + num2
print(f'A soma de {num1} + {num2} é igual a {resultado}' '''


''' num = int(input('Digite um número:'))
if num % 2 == 0:
    print(f'o número {num} é PAR')
else:
    print(f'O número {num} é Impar') '''


''' import random
numero_secreto = random.randint(1, 10)
tentativa = int(input("Tente adivinhar o número entre 1 e 10:"))
if tentativa == numero_secreto:
    print(f'Parabéns! Você acertou!')
else:
    print(f'Errou! o número correto era {numero_secreto}.') '''

''' num = int(input('Digite um número para ver sua tabuada:'))
for i in range(1,11):
    print(f'{num} x {i} = {num * i}') '''

''' palavra = input("Digite uma palavra:") .lower()
vogais = "aeiou"
contador = sum(1 for letra in palavra if letra in vogais) 
print(f"A palavra '{palavra}' tem {contador} vogais") '''

''' numeros = [1, 2, 3, 4, 5, 6]
resultado = sum(numeros)
print(f'{resultado}') '''

palavra = input("Digite uma palavra:")
print(f'A palavra ao contrário é : {palavra[::-1]}')