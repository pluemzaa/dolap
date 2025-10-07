_1 = input("Enter item 1 :")
_1W = float(input("Enter weight 1 :"))
_2 = input("Enter item 2 :")
_2W = float(input("Enter weight 2 :"))
_3 = input("Enter item 3 :")
_3W = float(input("Enter weight 3 :"))
_4 = input("Enter item 4 :")
_4W = float(input("Enter weight 4 :"))
_1W = "%.2f" % _1W
_2W = "%.2f" % _2W
_3W = "%.2f" % _3W
_4W = "%.2f" % _4W
total = _1W + _2W + _3W + _4W
total = "%.2f" % total
print(_1,"           ",_1W)
print(_2,"           ",_2W)
print(_3,"           ",_3W)
print(_4,"           ",_4W)
print("---------------------------")
print("total            ",total)