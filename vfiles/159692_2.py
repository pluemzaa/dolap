x=int(input('Please enter your net income:')) 
if 0<=x<=150000:
    print('The tax amount you have to pay this year : 0.00')                
elif 150000<x<=300000:
    x=(x-150000)*5/100
    print(f'The tax amount you have to pay this year :{x:.2f}') 
elif 300000<x<=500000:    
    x=(x-300,000)*10/100+7500
    print(f'The tax amount you have to pay this year :{x:.2f}') 
elif 500000<x<=750000:    
    x=(x-500000)*15/100+27500
    print(f'The tax amount you have to pay this year :{x:.2f}') 
elif 750000<x<=1000000:    
    x=(x-750000)*20/100+65000
    print(f'The tax amount you have to pay this year :{x:.2f}') 
elif 1000000<x<=2000000:    
    x=(x-1000000)*25/100+115000
    print(f'The tax amount you have to pay this year :{x:.2f}') 
elif 2000000<x<=5000000:
    x=(x-2000000)*30/100+365000
    print(f'The tax amount you have to pay this year :{x:.2f}') 
elif x>5000000:
    x=(x-5000000)*35/100 +1265000
    print(f'The tax amount you have to pay this year :{x:.2f}') 
else :
    print('')