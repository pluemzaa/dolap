aHOUR = int(input())
aMIN = int(input())
bHOUR = int(input())
bMIN = int(input())

trueMIN = aMIN-bMIN
trueHOUR = bHOUR - aHOUR

if trueMIN < 0:
    trueMIN = trueMIN*-1

if trueMIN <= 15 and trueHOUR == 0 :
    print("Pay:0")
    
if trueMIN > 0 : 
    trueHOUR = trueHOUR + 1

if trueHOUR <= 3:
    pay = trueHOUR * 10
    print(f"Pay:{pay}")
elif trueHOUR > 3 and trueHOUR <= 6 :
    trueHOUR = trueHOUR - 3
    pay = (trueHOUR*20)+30
    print(f"Pay:{pay}")
else:
    print("Pay:200")