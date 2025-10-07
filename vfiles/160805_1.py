Word = input("Enter input:")
A = ""
i = len(Word) - 1
while i >= 0:
  A = A + Word[i]
  i = i-1
print(A)