k=[]
l=input("enter any string:")
#        print("the string is palodrome")
#else:
 #   print("not a palidrome")
for k in l.split():
    
    if l==l[::-1]:
        l.append(l)    

print("Total  number of palindrome words in a sentence: ",len(k))
