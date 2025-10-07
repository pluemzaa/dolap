num = int(input("Enter the number of terms: "))
terms_num = [0, 1]
x = 0
while x <= num:
    x = terms_num[len(terms_num) - 1] + terms_num[len(terms_num) - 2]
    terms_num.append(x)
for i in terms_num:
    print(i, end=' ')