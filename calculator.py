import emoji

# Making a calculator where it will perform square root,cube of a number and multiplication ,addition,division,sub of multiple number 
print("Hey user welcome to Sujan's calculator")

def add():
    total_sum = []
    while True:
        num = int(input("Enter a number to add (enter 0 to finish): "))
        total_sum.append(num)
        if num == 0:
            break
    total = sum(total_sum)
    print()
    print (f"The total sum is: {total}")

def mult():
    total=[]
    product=1
    while True:
        number=(input("Enter a number to multiply: "))
        if number == "0":
            return "The value is : ",0
        elif number=="":
            break
        else:
            total.append(number)
    for num in total:
        product*=int(num)
        print()
    print(f"The product is : {product}")

def sub():
    resultant_num=None
    while True:
        number=(input("Enter a number for subtraction: "))
        if number == "":
            break
        elif number.isdigit():
            if resultant_num is None:
                resultant_num=int(number)
            else:
                resultant_num-=int(number)
                print()
                print(f"The resultant number after subtracting is: {resultant_num}")
        else:
            print("Enter a valid number: ")

def div():
    divided_num=None
    while True:
        number=int(input("Enter a number for division: "))
        if number == "":
            break
        else:
            if divided_num is None:
                divided_num=number
            else:
                divided_num=(divided_num/number)
                print()
                print("The number after division is :",divided_num)

def square():
    number=int(input("Enter a number for cubic value: "))
    if number is 0:
        print("The output is #0")
    else:
        print(f"The square root of '{number}' is #{number*number}")   
    
def cube():#we can do the same with lambda function also
    number=int(input("Enter a number for cubic value: "))
    if number is 0:
        print("The output is #0")
    else:
        print(f"The cubic value of '{number}' is #{number*number*number}")   

while True:
   
    print()
    print("---------------------")
    print("Choose your type of calculation")
    print("1.Addition")
    print("2.Multiplication")
    print("3.Subtraction")
    print("4.Division")
    print("5.Square")
    print("6.Cube")
    print("7.Quit")
    print("----------------------")
    
    choice=int(input("Enter your choice of calculation: "))

    if choice == 1:
        (add())
    elif choice == 2:
        (mult())
    elif choice == 3:
        sub()
    elif choice == 4:
        div()
    elif choice == 5:
        square()
    elif choice == 6:
        cube()
    
    elif choice == 7:
        break
print("Thank's for using Sujan's calculator")
print("\U0001F609","\U0001F609","\U0001F609")
