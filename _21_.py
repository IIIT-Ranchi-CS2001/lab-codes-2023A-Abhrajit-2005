s = input("Enter the string: ")
dic = dict()
for i in s:
    if i==" ":
        pass
    elif i in dic:
        dic[i]+=1
    else:
        dic[i] = 1
print(dic)
