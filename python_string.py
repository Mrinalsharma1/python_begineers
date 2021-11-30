# print character in string
for x in "banana":
    print(x)

# check string lenght
x = "this is mango"
print(len(x))

# check string is there or not
txt = "hey, i am busy now"
print("busy" in txt)

# check string is there or not by condictional statement
txt = "hey, i am busy now"
if "busy" in txt:
    print("this is true")

# use number with text in same line
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
