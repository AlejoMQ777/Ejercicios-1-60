l = list(map(int, input().split()))
n = len(l) + 1
print(sum(range(1, n+1)) - sum(l))
