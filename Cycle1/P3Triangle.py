a = int(input("Enter the First Side:"))
b = int(input("Enter the Second Side:"))
c = int(input("Enter the Third Side:"))
if a==b and b==c :
     print("Equilateral Triangle")
elif a==b or a==c or b==c :
     print("Isosceles Triangle")
else :
     print("Scalene Triangle")