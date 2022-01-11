import random

print("=-=-= Passwords Generator =-=-=")
print()

alph_lower = "abcdefghijklmnopqrstuvxwyz"
alph_upper = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
number = "0123456789"
symbol = "!@#$%*&:;.,*-_"

valor = alph_lower + alph_upper + number + symbol
tamanho = 9
password  = "".join(random.sample(valor, tamanho))
print("A senha que você gerou é: ", password)