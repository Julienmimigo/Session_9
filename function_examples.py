def greet():
    """
    Simple function printing hello
    :return: None
    """
    print("Hello!")
    return 0
greet()
x = greet()
print(x)

def greet_improved(name):
    """
    More complex greet that takes a name as a param
    :param name: the name of the person to greet
    :return: None
    """
    print("Hello", name)

greet_improved("John")
greet_improved("Jane")

def custom_op(x = 0 ,y = 0):
    """
    Custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: number, 10x+y
    """
    result = 10*x + y
    return result

print(custom_op(5,8))
x = custom_op(5, 9)
print(f"the result of custom_op is {x}")
x = custom_op(y=5, x=9)
print(f"the result of custom_op is {x}")
print(custom_op(5))
print(custom_op())
print(custom_op(y = 9))

def bond_intro(name):
    print("the name is:", name)

def bond_name(first, last):
    return f"{last}, {first}, {last}"

print(bond_name("Jon", "Jones"))
bond_intro(bond_name("Jon", "Jones"))

