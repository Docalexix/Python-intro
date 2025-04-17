# Write a python  code that will add list of numbers together
list1=[1,20,2,4,6,7,9,1,5,6]
threshold=3000
total=1
for i in list1:
    total=total*i
print(total)
if total > threshold:
    print("yes is greater than the threshold")
else:
    print("no is less than the threshold")    
        
     