h_in = int(input('')) #ชม.เข้า
m_in = int(input('')) #น.เข้า
h_out = int(input('')) #ชม.ออก
m_out = int(input('')) #น.ออก


h_in -= 7
h_out -= 7
price_h = h_out - h_in
price_m = m_out - m_in

if price_m > 0 :
		a = int(price_m / price_m)
else :
		a = 0
	
		
if price_h == 0 and price_m <= 15 :
	date = 0
	
elif price_h >= 0 and price_h <= 3 :
	if (price_h+a) >= 4 and price_h <= 6 :
		date = 30
		b = ((price_h-3)+a)*20
		date = date + b
	else :
		date = (price_h*10)+(int(a*10))
	
else :
	date = 200
	
print(f'pay:{date}')