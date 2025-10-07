def strToInt(data_list):
    data_list = data_list.split(',')
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list
    
    
def isMax(data_list):
    data_list = strToInt(data_list)
    max = data_list[0]
    for i in range(len(data_list)):
        if i > max:
            max = i
            
    for i in data_list:
        print(f"{i} is the maximum value: {i == max}")
        
string = input("Enter a series of numbers separated by commas: ")
isMax(string)