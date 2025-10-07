ชั่วโมงเข้า = int(input()) 
นาทีเข้า = int(input())    
ชั่วโมงออก = int(input())    
นาทีออก = int(input()) 
timein = ชั่วโมงเข้า * 60 + นาทีเข้า
timeout = ชั่วโมงออก * 60 + นาทีออก
if timein < 7 * 60 or timeout > 23 * 60 or timeout <= timein:
    print("หมดเวลาบริการ")
else:
    เวลาทั้งหมด = timeout - timein  
    if เวลาทั้งหมด <= 15:
        pay = 0
    else:
        hours = (เวลาทั้งหมด + 59) // 60
        if hours <= 3:
            pay = hours * 10
        elif hours <= 6:
            เวลาเกิน = hours - 3
            pay = 30 + เวลาเกิน * 20
        else:
            pay = 200

    print("Pay:{}".format(pay))