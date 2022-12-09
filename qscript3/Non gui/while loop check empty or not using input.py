name =input("enter your name: ")
if name:
	print(f"your name is {name}")
else:
		i=0
		while i <=9:
			
			i+=1
			name=input(f"try again\n enter your name{i}: ")
			if name:
				print(f"your name is {name}")
				break
        

