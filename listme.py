listfruit=["orange","orange","orange","apple","apple","apple","apple","apple","apple","banana","pineapple","mango","pawpaw","groundnut"]
listme=["orange","yam","chiz","chiz","pineapple","pineapple","mango","pawpaw","groundnut"]

for i in listfruit:
    if i=="orange":
        #print(i)
        listfruit.remove(i)
    else:
        continue  
print(listfruit)        
        
        
del listme[0]
#print(listme)       
        
        
        
item_list = ['item', 5, 'foo', 3.14, True]
item_list.remove('item')
item_list.remove('foo') 
#print(item_list)


#to check for duplicatee item and print them out ignore the extensions
listme1=["orange.txt","yam.txt","chiz.mb","chiz.mb","chiz.mb","pineapple.jpg","pineapple.jpg","mango.mb","pawpaw.doc","groundnut.jpg"]
opt=[]
duplicateitem=[]

for item in listme1:
    opt.append(item)
    if opt.count(item)>1:
       
        duplicateitem.append(item)
    else:
        continue  
#print("Dublicate items found but stored anyway")       
#print(duplicateitem) 

# write a python function