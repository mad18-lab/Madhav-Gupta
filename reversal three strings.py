a=str(input("Enter your string: "))
b=a[::-1]
print(b)

i=len(a)-1
while (i>=0):
    print (a[i], end="")
    i=i-1

def stringreverse(a):
    a = a[::-1]
    return a
print("\nReverse of string is:", stringreverse(a))