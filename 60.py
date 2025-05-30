a, b, c = map(float, input().split())
d = b**2 - 4*a*c
print("2 soluciones" if d > 0 else "1 solución" if d == 0 else "No reales")
