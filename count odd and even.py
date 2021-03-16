a=int(input("Enter a number N "))
count_even=0
count_odd=0
i=1
while (i<=a):
    if (i%2==0):
        count_even+=1
        i+=1
    else:
        count_odd+=1
        i+=1
print("Even numbers are", count_even)
print("Odd numbers are", count_odd)