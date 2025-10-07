gnum = 42
while True:
  x = int(input('Enter'))
  if x > 42:
    print('Too high!')
  elif x < 42:
    print('Too low!')
  else:
    print('Congratulations! You guessed the number')
    break