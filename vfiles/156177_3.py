num_alpha = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
code_lub = int(input("Enter key: "))
h = (num_alpha[(7+code_lub)%26]
e = (num_alpha[(4+code_lub)%26]
l_1 = (num_alpha[(11+code_lub)%26]
l_2 = (num_alpha[(11+code_lub)%26]
o = (num_alpha[(14+code_lub)%26]
result_codelub = (h + e + l1 + l2 + o)
print("Cipher of hello is: ",result_codelub)