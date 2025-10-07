number  ="1 2 3"
numberlist1_str = number.split()
number2 ="4 5 6"
numberlist2_str = number2.split()
numberlist1_int = [int(s) for s in numberlist1_str]
numberlist2_int = [int(s) for s in numberlist2_str]
print(numberlist1_int)
print(numberlist2_int)
dot_product = sum([numberlist1_int[i] * numberlist2_int[i] for i in range(len(numberlist1_int))])
print(dot_product)