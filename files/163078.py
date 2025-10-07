stick = int(input())
balls = int(input())
balls_per_bag = int(input())

answer = (stick*balls)/balls_per_bag

if stick == 0 and balls%balls_per_bag == 0:
    print("%.0f" %balls/balls_per_bag)

elif stick == 0:
    temp = (balls/balls_per_bag)+1
    print("%.0f" %temp)

elif (stick*balls)%balls_per_bag == 0:
    print("%.0f" %answer)

else:
    answer +=1
    print("%.0f" %answer)