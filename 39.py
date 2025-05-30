def hanoi(n, a, b, c):
    if n: hanoi(n-1, a, c, b); print(a, '->', c); hanoi(n-1, b, a, c)
hanoi(int(input()), 'A', 'B', 'C')











