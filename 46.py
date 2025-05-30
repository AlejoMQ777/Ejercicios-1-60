asientos = [0]*10
i = int(input("Elige asiento 0-9: "))
if asientos[i] == 0:
    asientos[i] = 1
    print("Reservado")
else:
    print("Ocupado")
