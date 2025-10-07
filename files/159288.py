net_income = float(input("Please enter your net income: "))
tax = 0 

if 0 <= net_income <= 150000 : #1 ok 
    tax = 0
elif 150001 <= net_income <= 300000: #2 ok  
    tax = (net_income-150000)*(5/100)
elif 300001 <= net_income <= 500000: #3 ok 
    tax = ((net_income-300000)*(10/100))+7500
elif 500001 <= net_income <= 750000: #4 ok 
    tax = ((net_income-500000)*(15/100)) + 27500
elif 750001 <= net_income <= 1000000: #5 ok
    tax = ((net_income-750000)*(20/100)) + 65000
elif 1000001 <= net_income <= 2000000: #6 ok
    tax = ((net_income-1000000)*(25/100)) + 115000
elif  2000001 <= net_income <= 5000000: #7 ok
    tax = ((net_income-2000000)*(30/100)) + 365000
elif net_income > 5000000 : #8 ok
    tax = ((net_income-5000000)*(35/100)) + 1265000
    
      
print(f"The tax amount you have to pay this year : {tax:.2f}")