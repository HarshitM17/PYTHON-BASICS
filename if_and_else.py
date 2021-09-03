#CALCULATOR FOR POSITIVE VALUES 

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

if abs(int(num1))and abs(int(num2)):
    c = input("Choose =>  + , - , * , / :")
    if c =='+':
        print(abs(add(num1,num2)))
    elif c == '-':
        if num1>num2:
            print(abs(sub(num1,num2)))
        else:
            print(abs(sub(num2,num1)))
    elif c == '*':
        print(abs(mul(num1,num2)))
    elif c == '/':
        print(abs(div(num1,num2)))
    else:
        print("Mistake!!!!!!!")
else:
    print("Your input is not integer")