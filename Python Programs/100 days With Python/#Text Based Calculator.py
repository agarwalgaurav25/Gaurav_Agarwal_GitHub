#Text Based Calculator
import operator

operators ={
    'add': [operator.add,"+"],
    'sub': [operator.sub,"-"],
    'mul': [operator.mul,"*"],
    'div': [operator.truediv,"/"],
    "mod" :[operator.mod,"modulous"]
    }

def calc (first_number,second_number,user_operation):
    print (f'Your Question is {first_number} {operators[user_operation][1]} {second_number}')
    if operation in operators:
            return operators[operation][0](first_number,second_number)
    #if you wanna see hard coded version open below
    #region
    #Hard coding the operations    
        # if operation == "+":
        #     result = num1 + num2
        # if operation == "-":
        #     result = num1 - num2
        # if operation == "/":
        #     result = num1 / num2
        # if operation == "*":
        #     result = num1 * num2

        # print(f'{num1} {operation} {num2} = {result}')
#endregion

    

num1 = float(input("Enter the first Number: "))

should_continue = "Y"
while should_continue == "Y":
    num2 = float(input("Enter the another Number: "))
    print ("List of Operations Available :")

    #Using Loop to print the available operations as per the dictionary operators
    for i in operators:
         print(f'👉 {i} =  {num1} {operators[i][1]} {num2}')
    operation = input("Enter the operation : ").lower()
    #if you wanna see hard coded version open below
    #region


    # Hard coding the aval operations     
        # operation = input(
        #      f'''
        # List of operations available 

        #      👉 add =  {num1} + {num2} 
        #      👉 sub =  {num1} - {num2}
        #      👉 mul = {num1} * {num2}
        #      👉 div = {num1} / {num2}
        #      👉 mod = remainder when {num1} is divided by {num2}

        # Enter the operation : ''')
 #endregion   

    #Printing the user's Question
    result = calc(num1,num2,operation)
    print(f'{num1} {(operators[operation][1])} {num2} = {result}')
    print (f'The result is {result}')
    #Asking if user wants to continue
    should_continue = (input("Press Y if you wanna continue , press N if you dont :")).upper()
    if should_continue == "Y":
         num1 = result
#End the programm once user is done
    elif should_continue == "N":
        print("Thank you for using our calculator")
        break