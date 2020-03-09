print("Please enter '1' or '2'")
userChoice = input()

while userChoice != '2' and userChoice != '1':
	#nhập userChoice cho đến khi nó == '1' hoặc == '2'
	print("Invalid option, please try again")
	userChoice = input()

if userChoice == "1":
	print("Hello World")
	print("Have a nice day")
else: #userChoice không == 1 thì chắc chắn == 2
	name = input()
	print("Hello", name)

print("Program will exit")

