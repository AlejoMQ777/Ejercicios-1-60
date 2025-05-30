n = int(input())
for i in range(2, n+1):
    if all(i % d != 0 for d in range(2, int(i**0.5)+1)):
        print(i, end=' ')
