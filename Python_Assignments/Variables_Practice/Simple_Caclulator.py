print("This will be a simple 1st grade math")


Number_1 = input("Enter first number: ")
Operation = input("Enter operation(+,-,*,/): ")
Number_2 = input("Enter second number: ")

num1 = int(Number_1)
num2 = int(Number_2)
Error = " "
Solution = 0

if Operation == "+":
    Solution = num1 + num2
    print(Solution)
elif Operation == "-":
    Solution = num1 - num2
    print(Solution)
elif Operation == "*":
    Solution = num1 * num2
    print(Solution)
elif Operation == "/":
  if num2 == 0:
    print("Error")
  else:
    Solution = num1 / num2
    print(Solution)    

  
