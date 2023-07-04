# Variables
name = "Anthony"
last_name = 'Looney'
age = 35
price = 12.03
found = False

print(name + " " + last_name)
print(price)
print(str(age) + " years old")

#math operator
#same as JS
print(21 + 21)

# if statements
if (age < 100):
    print("Don't worry, you are young!")
    print("Still inside the if")
    print("Me Too")
elif (age == 100):
    print("Congrats on the century")
else:
    print("Sorry, you are getting old")
print("I'm outside the if")

# functions
def test():
    print("I'm a function")

# call a function
test()
test()
test()