#The radius of circle is 45cm, if pie =3.142. ,Write a python code 
#that will calculate the area of the circle and the circumference 
#of the circle. Add the area and the circumference together and print it out

def circle():
    pie=3.142
    radius=45
    area=pie*radius*radius
    print(area)
    circumference=2*pie*radius
    print(circumference)
    total=area+circumference
    print(total)
circle()    