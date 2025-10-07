#10
u= "admin"
p= "password123"
a=0
while a<3 :
    x=input('Enter username:' )
    z=input('Enter password:')
    if u==x and p==z :
        printt('Login successful!')
        break
    else :
        print('Invalid credentials. Try again.')
        a+=1
print('Maximum login attempts reached. Access denied.')