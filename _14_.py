n = int(input("Enter a number: "))
i = n
l = [0,0,0,0,0,0,0,0,0,0]
while(i>0):
    j = i%10
    l[j] = l[j] + 1
    i = i//10
for i in range(0, 10):
    if(l[i]==0):
        continue
    else:
        print(i,"occurs",l[i],"times")