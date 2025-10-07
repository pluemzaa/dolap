x = input('Enter a series of numbers separated by commas:')
y = [float(i)for i in x.split(',')]
min = min(y)
max = max(y)

if max > min:
  
    print("Normalized values:")
    for i in y:
        normalized = (i - min) / (max - min)
        print(f"{normalized:.2f}")