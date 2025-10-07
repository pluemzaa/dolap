while True: 
  text = input('enter password: ')
  num = 0
  up = 0
  low = 0
  for i in range(len(text)): 
    if len(text) < 8:
      print("ไม่ปลอดภัย")
      break 
    else:
      if text[i].isdigit():
        num += 1
      elif text[i].isupper():
          up += 1
      else :
        low += 1

  if len(text) >= 8 and num > 0 and up > 0 and low > 0:
    print('pass')
    break
  else:
    print('not pass')