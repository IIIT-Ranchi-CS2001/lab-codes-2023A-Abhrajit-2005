# Number of Palindromic words in a sentence
s = input("Enter the sentence : ")
l = s.split()
c = 0
for i in l:
    if(i == i[::-1]):
        c = c+1
print("Number of palindromic words : ",c)