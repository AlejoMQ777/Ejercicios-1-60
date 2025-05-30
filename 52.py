votos = [input() for _ in range(5)]
print(max(set(votos), key=votos.count))

