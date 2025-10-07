def strToInt(data_list):
    data_list = data_list.split(',')
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list
    
def min_max(data_list):
    temp_min = data_list[0]
    temp_max = data_list[0]
    for i in data_list:
        if i < temp_min:
            temp_min = i
        if i > temp_max:
            temp_max = i
    return temp_min,temp_max
    
def Normalized(data_list):
    min,max = min_max(data_list)
    print("Normalized values:")
    for i in range(len(data_list)):
        print(f"{(data_list[i]-min)/(max-min):.2f}")
        # data_list[i] = (data_list[i]-min)/(max-min)
    # print(data_list)
data = strToInt(input("Enter a series of numbers separated by commas: "))
# print(data)
print(Normalized(data))
# Enter a series of numbers separated by commas: 10,20,30,40,50
# Normalized values:
# 0.00
# 0.25
# 0.50
# 0.75
# 1.00