number = [int(input('Enter a number (enter 0 to stop): '))] #ข้อ3
total = 0
if number[0] == 0:
  print('No numbers entered.')
else:
    while True:
        i = int(input('Enter a number (enter 0 to stop): '))
        number.append(i)
        if i == 0:
            break
    for y in number:
                total += int(y)
print('Average: ',total/(len(number)-1))