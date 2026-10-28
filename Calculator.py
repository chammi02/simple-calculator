while True:
    try:
        num1 = float(input("Enter first number : "))
        op = input("Operator (+ , - , * , /) = ")
        num2 = float(input("Enter second number : "))
    except ValueError:
        print ("Type only numbers!")
        continue

    if op == "+":
        print("Änswer: ", num1 + num2 )
    elif op == "-":
        print("Answer: " , num1 - num2)
    elif op == "*":
        print("Answer: " ,num1 * num2 )
    elif op =="/":
        if num2 == 0:
            print("can't divide by 0 ")
        else:
            print("Answer: ", num1 / num2)
    else :
        print("Invalid Operator")

    again = input ("Do you want calculate again ? (y/n) : ")
    if again.lower() != "y":
        print("Bye!")
        break