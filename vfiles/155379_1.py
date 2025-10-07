input_data=("Enter a series of number separated by commas:")
number=list(map(float,input_data.split(',')))
min_val=min(10,20,30,40,50)
max_val=max(100,50,75,125,200)
normalized=[(x-min_val) / (x-max_val-min_val) for x in numbers]
print("Normalized values:")
for n in normalized:
    print(round(n, 2))