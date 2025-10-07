number = ['0','1','2','3','4','5','6','7','8','9']
text_n = 0
text_s = 0
text_b = 0

while text_n == 0 or text_s == 0 or text_b == 0:
	text_n,text_s,text_b = 0,0,0
	password = input('Enter a password: ')
	
	if len(password) <= 8 :
		print('Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.')
		
	elif len(password) > 8 :
		for pass_num in range(len(password)) :
			if password[pass_num].islower() :
				text_s += 1
			elif password[pass_num].isupper() :
				text_b += 1
			for num_in_number in range(0,10) :
				if password[pass_num] == number[num_in_number] :
					text_n += 1
		if text_n != 0 and text_b != 0 and text_s != 0 :
				print('Password is valid.')
				
		else :
				print('Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.')