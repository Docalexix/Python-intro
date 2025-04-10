# You are given the following 2.56.78.34.23,21 in a list.
# Write a python code that add all the numbers together as total. Check if the total
#is greater than 50 ,if yes divide this result by 20 and add 19 and print final outcome
# Else just add 500 to the initials total and print out outcomes.
list=[2,56,78,34,23,21]
#print(sum(list))
total=0
for i in list:
    #print(i)
    total=total+i
print(total)
if total > 50:
    result=(total/20)+19
    print(result)
else:
    result=total+500
    print(result)    