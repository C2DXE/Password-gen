import random
import os
import base64
from base64 import decode

caracteres = ["+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

longitud = int(input("Cuantos caracteres quieres que tenga la contraseña [Recomendados 8-12]: "))

contraseña = []

for i in range(longitud):
    s = random.choice(caracteres)
    contraseña.append(s)

strpass = ' '.join(contraseña)

print(strpass)

##encoded = strpass.encode("ascii")

##encoded2=encoded

##decoded = encoded.decode("ascii")


with open('passwords.txt', 'w') as f:
    f.write(strpass)