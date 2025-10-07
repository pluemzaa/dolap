h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())

# คำนวณเวลาจอดรวมเป็นนาที
duration = (h_out * 60 + m_out) - (h_in * 60 + m_in)

if duration <= 15:
    pay = 0
elif duration <= 180:
    hours = (duration + 59) // 60
    pay = hours * 10
elif duration <= 360:
    hours = (duration + 59) // 60
    # คิด 3 ชั่วโมงแรกชั่วโมงละ 10 บาท, ที่เกินคิด 20 บาท/ชั่วโมง
    pay = 3 * 10 + (hours - 3) * 20
else:
    pay = 200

print(f"Pay:{pay}")