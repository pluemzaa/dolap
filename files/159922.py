num_index = []
nur = int(input("Enter a number (enter 0 to stop): "))

while nur != 0:
  num_index.append(nur)
  nur = int(input("Enter a number (enter 0 to stop): "))
if num_index == []:
  print("No numbers entered.")
else:
  print("Average:", sum(num_index) / len(num_index))