import random
u = input("Tu: ")
c = random.choice(["piedra", "papel", "tijeras"])
print("Compu:", c)
print("Empate" if u == c else "Ganas" if (u, c) in [("piedra", "tijeras"), ("papel", "piedra"), ("tijeras", "papel")] else "Pierdes")
