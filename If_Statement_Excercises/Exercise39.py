decibels = float(input())
	
if decibels > 0 and decibels < 40:
    print('smaller than quiet room.')
		
elif decibels == 40:
    print('quiet room.')
	
elif decibels > 40 and decibels < 70:
    print('between quiet room and alarm clock.')
elif decibels == 70:
    print('alarm clock')
		
elif decibels > 70 and decibels < 106:
    print('between alarm clock and lawn mower')
	
elif decibels == 106:
    ('lawn mower')
	
elif decibels > 106 and decibels < 130:
    print("between lawn mower and jackhammer")
		
elif decibels == 130:
    print('jackhammer')
		
elif decibels > 130:
    print('larger than the jackhammer')
else:
    print("Enter a number greater than 0")
		
