experience = int(input())
if experience < 2:
    salary = 25000
elif experience >= 2 and experience <= 5:
    salary = 35000
elif experience >= 6 and experience <= 10:
    salary = 50000
else:  
    salary = 200000
print(salary)