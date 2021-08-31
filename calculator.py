def add(e,f):
    return int(e)+int(f)
def sub(e,f):
    return int(e)-int(f)
def mul(e,f):
    return int(e)*int(f)
def div(e,f):
    return float(int(e)/int(f))


num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

if int(num1) and int(num2):
    c = input("Choose =>  + , - , * , / :")
    if c =='+':
        print(add(num1,num2))
    elif c == '-':
        print(sub(num1,num2))
    elif c == '*':
        print(mul(num1,num2))
    elif c == '/':
        print(div(num1,num2))
    else:
        print("Mistake!!!!!!!")
else:
    print("Your input is not integer")
