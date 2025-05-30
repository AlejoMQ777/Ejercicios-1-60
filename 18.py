l = list(map(int, input().split()))
pares = sum(x % 2 == 0 for x in l)
print("Pares:", pares, "Impares:", len(l) - pares)

