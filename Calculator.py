import goto
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def req():
    ch=input("If you want to continue Press 'y' or if you don't Press 'n':")
    if(ch=='y'):
        return
    elif(ch=='n'):
        quit()
    else:
        print("Please choose between 'y' or 'n'")
while True:
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\nPress 5 for exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("Addition result is ",add(num1,num2))
        print("*************************************")
        req()
    elif(ch==2):
        print("Subtraction result is ",sub(num1,num2))
        print("*************************************")
        req()
    elif(ch==3):
        print("Multiplication result is ",mul(num1,num2))
        print("*************************************")
        req()
    elif(ch==4):
        print("Division result is ",div(num1,num2))
        print("*************************************")
        req()
    elif(ch==5):
        quit()
        print("*************************************")
        req()
    else:
        print("Wrong Input!!!!")
        print("*************************************")
        req()
    
