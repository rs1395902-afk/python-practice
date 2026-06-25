# ATM MACHINE
balance = int(10000)
print("WELCOME TO SBI ATM")

# Read a 4-digit PIN from the user and validate it
pin = input("ENTER YOUR PIN : ")
if len(pin) == 4 and pin.isdigit():
	pin = int(pin)
	print("PIN accepted")
else:
	print("Invalid PIN. Please enter a 4-digit numeric PIN.")
y = str(input("CHOOSE D FOR DEPOSIT OR W FOR WITHDRAWL : ")).upper()

if(y== "D") :
	b=int(input(("ENTER YOUR AMOUNT : ")))
	amount = balance+b
	print("BALANCE DEPOSITED")
	print("CURRENT BALANCE :", amount)
elif(y== "W"):
	c = int(input("ENTER YOUR AMOUNT: "))
	if(c>balance):
		print("UNSUFFICIENT VALUE")
	else:
		amount = balance-c
		print("AMOUNT WITHDRAWAL")
		print("CURRENT BALANCE :", amount)
else:
	print("INVAILD CHOICE")
	
	
	