# Write a python  code that will add list of numbers together
list1=[1,20,2,4,6,7,9,10,15,16]

#If the  threshold =13
#1. Print the numbers that are  greater than the threshold
#2.#print all the list less than 39
#3. print("All the list less or equal to 29")
basket=[]
threshold=25
for i in list1:
    if i < threshold:
        print(i)
        basket.append(i)

print(basket)
     
        