s = input()
print(''.join(chr((ord(c)-97+3)%26+97) if c.isalpha() else c for c in s.lower()))











