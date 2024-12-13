# Printing first n terms of Fibonacci series
n = int(input("Enter the number of terms : "))
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
i = 2
while(i<n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    i+=1