s1 = input("Enter a string : ")
for i in s1:
    if i.isalnum():
        pass
    else:
        print("False")
        break    
else:
    print("True")