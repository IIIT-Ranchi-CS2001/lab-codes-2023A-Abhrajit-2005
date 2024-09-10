n = int(input("Enter a number: "))
i = n
c = 0
while i>0:
    j = i%10
    c = c + j
    i = i//10
print("Sum of digits of ",n," is ",c)