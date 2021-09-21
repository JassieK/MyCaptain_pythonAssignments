n = int(input("Enter the limit "))
a = 0
b = 1
s = 0

print(a ," ", b, end = " ")
while b < n :
    s = a+b
    print  (s , end=" ")
    a = b
    b = s

