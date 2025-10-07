n1 = input('Enter n1:')
n1 = int(n1)
n2 = input('Enter n2:')
n2 = float(n2)
lang = input("Enter lang:")

a = [n1, n2, "Python"]
b = (n1, n2, "Python")
c = {"num1" : n1 , "num2" : n2, "lang" : "Python"}
print(a)
print(b)
print(c["num1"],c["lang"])