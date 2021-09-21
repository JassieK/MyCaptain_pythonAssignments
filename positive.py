l=[]
l1 =[]
n = int(input("Enter the number of elements "))
print("Now enter ", n , " values")
for i in range(0,n):
    ele = int(input())
    l.append(ele)
for i in l:
    if i>=0:
        l1.append(i)
    
print(l1)
    