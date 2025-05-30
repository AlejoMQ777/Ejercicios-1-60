s = input()
r = s[0] + ''.join(s[i] for i in range(1, len(s)) if s[i] != s[i-1])
print(r)
