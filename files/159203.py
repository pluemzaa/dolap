i = float(input('Please enter your net income: '))

if  0  <= i <= 150_000:
  tax = 0

elif 150001 <= i <= 300000:
  tax = (( i - 150000)*(0.05))
elif 300001 <= i <= 500000:
  tax = (( i - 300000)*(0.10))+7500
elif 500001 <= i <= 750000:
  tax = (( i - 500000) *(0.15))+27500
elif 750001<= i <= 1000000:
  tax = (( i - 750000)*(0.20))+65000
elif 1000000 <= i <= 2000000:
  tax = (( i - 1000000)*(0.25))+115000
elif 2000001 <= i <= 5000000:
  tax = ((i - 2000000)*(0.30))+365000
elif i > 5000000:
  tax = ((i - 5000000)*(0.35))+1265000

print(f'The tax amount you have to pay this year : {tax:.2f}')