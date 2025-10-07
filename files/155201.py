# Enter a series of numbers separated by commas: 10,1,5,1,7
# 10 is the maximum value: True
# 1 is the maximum value: False
# 5 is the maximum value: False
# 1 is the maximum value: False
# 7 is the maximum value: False

def strToInt(data_list):
    data_list = data_list.split(',')
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list
    
    
def isMax(data_list):
    data_list = strToInt(data_list)
    max = data_list[0]
    for i in range(len(data_list)):
        if data_list[i] > max:
            max = data_list[i]
            
    for i in data_list:
        print(f"{i} is the maximum value: {i == max}")
        
string = input("Enter a series of numbers separated by commas: ")
isMax(string)