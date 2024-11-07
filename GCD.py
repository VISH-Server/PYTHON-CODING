def gcd(a, b):
    while b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1==0:
    print(f"The GCD of {num1} and {num2} is {num2}")    
elif num2==0:
    print(f"The GCD of {num1} and {num2} is {num1}")
else:
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}")
