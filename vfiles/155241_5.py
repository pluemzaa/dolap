def strToInt(data_list):
    data_list = data_list.split(',')
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list
banana = strToInt(banana)
banana = input("Enter a series of numbers separated by commas: ")
print(f"{banana[0]} is the maximum value: {banana[0] == max(banana)}")
print(f"{banana[1]} is the maximum value: {banana[1] == max(banana)}")
print(f"{banana[2]} is the maximum value: {banana[2] == max(banana)}")
print(f"{banana[3]} is the maximum value: {banana[3] == max(banana)}")
print(f"{banana[4]} is the maximum value: {banana[4] == max(banana)}")