# n = int(input("enter your number"));
# for i in range(0, n):
# 		# inner loop to handle number of columns
# 	print(i+1)	# values changing acc. to outer loop

# 	for j in range(0, n-i):
		
# 			# printing stars
# 		print("* ",end="")
	
# 		# ending line after each row
# 	print("\r")


# n = int(input("enter your number"));
# for i in range(0, n):
# 		# inner loop to handle number of columns
# 	print(i+1)	# values changing acc. to outer loop

# 	for j in range(0, i+1):
		
# 			# printing stars
# 		print("* ",end="")
	
# 		# ending line after each row
# 	print("\r")


# n = int(input("enter your number"));
# for i in range(n, 0, -1):
# 		# inner loop to handle number of columns
# 	print(i+1)	# values changing acc. to outer loop

# 	for j in range(i, 0, -1):
		
# 			# printing stars
# 		print("* ",end="")
	
# 		# ending line after each row
# 	print("\r")

n = int(input("enter your number"));
for i in range (0, n):
	# print(i)
	for j in range (0, n-i):
		for k in range(0, i+1):
			print("* ",end="")
	print("\r")

	