x = float(input("enter bill amount :"))
y = float(input("enter amount of people :"))
z = float(input("enter tips amount(%) :"))
xz = (z/100)*x
xyz = (x/y)+xz
print("tip per person is" , xz ,end=" and " )
print("total per person" , xyz)