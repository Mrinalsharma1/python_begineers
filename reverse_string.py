n = input("enter string")
print("the orizinal string is:",n)
revers_string=""
count=len(n)
while count > 0:
	revers_string=revers_string+n[count-1]
	count=count-1
print("the reverse string is:",revers_string)

