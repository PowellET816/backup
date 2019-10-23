print("Welcome to the To Do List")
todolist = []
while True:
	print("Enter A to add item")
	print("Enter R to remove an item")
	print("Enter P to print list")
	print("Enter Q to quick")
	choice = input("Make your choice: ")

	if choice == "q":
		break

	elif choice == "a":
		
		todolist.append(input("What do you want to add?: "))
		



	elif choice == "r":
		todolist.remove(input("What do you want to remove?: "))



	elif choice == "p":

		print(todolist)

	else:
		print("This is not a choice ")

		
		

	

