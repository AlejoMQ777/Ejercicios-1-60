import random
n = random.randint(1, 10)
while int(input("Adivina: ")) != n:
    print("Intenta otra vez")
print("¡Correcto!")
