hrcome = int(input(""))
mincome = int(input(""))
hrout = int(input(""))
minout = int(input(""))
tolhr = hrout - hrcome
tolmin = mincome + minout
toltime = (tolhr * 60) + tolmin
if (toltime <=15) :
    print ("pay:0")
elif (toltime >15) and (toltime <=180):
    print ("pay:10")
if (toltime >=240) and (toltime <=360):
    print ("pay:50")
if (toltime >360) :
    print ("pay:200")