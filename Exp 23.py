#Write a Python program that functions as a simple phone book manager with a menu-driven interface. The program prompts the user to choose from the following options: Add Contact, Remove Contact ,Display, Quit

pbook = {}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")

	choice = input("Enter choice (1-4): ")
	if choice == '1':
		name = input("Name: ")
		ph = input("Phone number: ")
		pbook[name] = ph
		
	elif choice == '2':
		name = input("Name: ")
		if name in pbook:
			del pbook[name]
		else :
			print("Not found")
			
	elif choice == '3':
		if not pbook:
			print("{}")
		else:
			print(pbook)
		
	elif choice == '4':
		break
	else:
		print("Invalid")
