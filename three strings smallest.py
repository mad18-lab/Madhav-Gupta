x = str(input("Enter string A: "))
y = str(input("Enter string B: "))
z = str(input("Enter string C: "))

a = len(x)
b = len(y)
c = len(z)

if a <= b and a <= c:
    print(x, "is the smallest")
elif b <= a and b <= c:
    print(y, "is the smallest")
else:
    print(z, "is the smallest")
