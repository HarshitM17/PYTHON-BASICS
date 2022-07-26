def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def square(a,b):
    print(a**b)
def modulus(a,b):
    print(a%b)

x = int(input("Enter 1st number: \n"))
y = int(input("Enter 2nd number: \n"))

choice = input("Enter your choice(+,-,*,/,**,%): ")
if choice in ('+','-','*','/','**','%'):
    if choice == '+':
        add(x,y)
    elif choice == '-':
        sub(x,y)
    elif choice == '*':
        mult(x,y)
    elif choice == '/':
        div(x,y)
    elif choice == '**':
        square(x,y)
    elif choice == '%':
        modulus(x,y)    
else:
    print("Error wrong input given!! ")
