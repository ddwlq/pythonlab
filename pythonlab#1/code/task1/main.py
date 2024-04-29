a = input("enter value a: ")
b = input("enter value b: ")

try:
    a = int(a)
    b = int(b)
except ValueError:
  print("Invalid input: Please enter numbers only.")

if 101 > a > 0 and 101 > b > 0:
    if a > b:
         x = a / b + 1
    if a < b:
         x = (a - b) / a
    else:
         x = -2
    print ("value x:", x)
    
else:
    print("Error^ a and b exceed their limit of permissible values")