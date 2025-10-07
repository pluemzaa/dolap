code = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
'''
caesar_c = {}
#7,4'11,11,14

key = int(input())
h = (key+7)%26
e = (key+4)%26
l1 = (key+11)%26
l2 = (key+11)%26
o = (key+14)%26

caesar_c += code[h]
caesar_c += code[e]
caesar_c += code[l1]
caesar_c += code[l2]
caesar_c += code[o]

print('Cipher of hello is',caesar_c)
   
#7,4'11,11,14


code_reverse = {n: k for k, n in code.items()}
key = int(input())

for cas in text:
  if cas in code_reverse:
    Caesar_cipher = code_reverse[cas]
    new_Caesar_cipher = ( caesar_cipher + key ) % 26
    result += code[new_Caesar_cipher]
  else:
    result += cas


code_reverse = {v: k for k,v in code.items()}
key = int(input())

text = 'hello'
n_list = []
for a in text:
  index = code_reverse[a]
  n_list.append(index)

nr_list = []
for n in n_list:
  H = (n+key)%26
  nr_list.append(H)

result = ''
for n in nr_list:
  letter = code[n]
  result += letter

print('Cipher of hello is',result)'''


key = int(input("Enterkey",))
q = (7 + key)%26
w = (4 + key)%26
e = (11 + key)%26
r = (11 + key)%26
t = (14 + key)%26

CC = code[q]+code[w]+code[e]+code[r]+code[t]
print('Cipher of hello is',CC)