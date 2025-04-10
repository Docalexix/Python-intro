# the diameter of a circle is 10cm, write a Python code that
# will calculate the area of the circle and the circumference of
# the circle. Finally, add the area and perimeter together and
# print the final result.
# if Pie=3.142

diameter=10
radius=diameter/2
pie=3.142
area=pie*radius*radius
print(area)

circumference=2*pie*radius
print(circumference)

result=area+circumference
print("this is the final result" ,result)
