a = int(input("Enter your number: "))
i = 1

while (i<=a):
    count = 0
    if (a%i==0):
        j = 1
        while (j<=i):
            if (i%j==0):
                count+=1
            j+=1
        if (count==2):
            print(i, "is a prime factor of", a)
    i+=1