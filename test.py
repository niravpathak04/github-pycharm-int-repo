print("A simple python code.... to check number is odd or even")

def num_check(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")

num1 = 23
num2 = 46

num_check(num1)
num_check(num2)

print("Another short program to swap nos")

a = 23
b = 56

a,b = b,a

print(a,b)