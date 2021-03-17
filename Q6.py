students = []
for i in range(10):
    students.append(input("Enter student name: "))

regnums = []
for j in range(10):
    regnums.append(input("Enter respective student register numbers: "))

output = []

for a,b in zip(students, regnums):
    output.append(a+" - "+b)

print(output)
output.insert(5, "RAJVEER - 24")
print("List after insertion: ", output)
print(output.pop(8))
print(output[5:8])