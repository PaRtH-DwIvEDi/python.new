marks = {}

x = int(input("enter marks of physics:"))
marks.update({"physics" : x})

y = int(input("enter marks of chemistry:"))
marks.update({"chemistry" : y})

z = int(input("enter marks of maths:"))
marks.update({"maths" : z})

print(marks)