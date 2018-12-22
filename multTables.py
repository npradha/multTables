
while True:
	print("\n")
	print("What number do you want the multiplication table of?")
	num = input()
	print("\n")
	for mul in range(13):
		answer = num * mul
		print(str(num) + " x " + str(mul) + " = " + str(answer))
	print("\n")
	print("Do you want to input another number? (y/n)")
	ans = raw_input()
	if ans == 'y':
		continue
	else:
		break
print("\n")
print("Happy Learning!!") 
