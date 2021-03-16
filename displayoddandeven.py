a=int(input("Enter a number N "))
elist=[]
olist=[]
for i in range (0,a):
    if (i%2==0):
        elist.append(i)
    else:
        olist.append(i)
print("Even numbers:", elist)
print("Odd numbers:", olist)