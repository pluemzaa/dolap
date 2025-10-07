Animals = {"Dog": 0,"Cat": 1,"Fish": 2}
Enter = input("Enter your pets: ")
A = text.split(",")
codes = [str(Animals[A[0]]),str(Animals[A[1]]),str(Animals[A[2]]),str(Animals[A[3]]),str(Animals[A[4]])]
print("Code of your pets:", codes[0] + "," + codes[1] + "," + codes[2] + "," + codes[3] + "," + codes[4])