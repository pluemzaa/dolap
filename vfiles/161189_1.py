cokeCount = 0
cokePrice = 0
pepsiCount = 0
pepsiPrice = 0

while True:
    menu = int(input('Enter menu (1-Coke, 2-Pepsi): '))
    if menu == 1:
        print('You selected Coke!')
        cokePrice = cokePrice + 25
        cokeCount = cokeCount + 1
    elif menu == 2:
        print('You selected Pepsi!')
        pepsiPrice = pepsiPrice + 20
        pepsiCount = pepsiCount + 1
    else:
        print('Invalid item!')

    cont = input('Continue? (y/n): ')
    if cont == 'n':
        break

print("Coke", cokeCount, cokePrice)
print("Pepsi", pepsiCount, pepsiPrice)