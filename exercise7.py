#Adding List Items Using insert() Method
#the insert() method in Python is used to add an element at a specified index (position) within a list, shifting existing elements to accommodate the new one.

#We can add list items using the insert() method by specifying the index position where we want to insert the new item and the item itself within the parentheses,

# like my_list.insert(index, new_item).

#In# this example, we have an original list containing various items. We use the insert() 
#me
list1 = ["Rohan", "Physics", 21, 69.75]

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)