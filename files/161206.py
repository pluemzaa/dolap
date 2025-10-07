text = list(map(lambda x:float(x) ,input("Enter a series of numbers separated by commas: ").split(',')))
print("Normalized values:")
text_temp = sorted(text)
min_x = text_temp[0]
max_x = text_temp[len(text)-1]
for x in text:
    print(f"{(x-min_x)/(max_x-min_x):.2f}")