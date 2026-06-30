a= 25
def x():
    global a
    a= 50
    print(f"Value of a inside function", a)

print(a)
x()