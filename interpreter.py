a = input("enter equation")
x,y,z= a.split()

if y =="+":
    c = float(x)+float(z)
if y =="-":
    c = float(x)-float(z)
if y =="/":
    c = float(x)/float(z)
if y =="*":
    c = float(x)*float(z)
print(c)
