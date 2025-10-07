x=input("Enter a series of numbers separated by commas:")
l=[int(i)for i in x.split(",")]
m=l[0]
print(f"set the maximum value to  {m}")
for n in l[1:]:
    if n>m:
        m=n
        print(f"set the maximum value to {m}")
print(f"The maximum value is {m}")