# tuple

student = ("mass",21,"yeji")

print(student.count("mass"))
print(student.index("yeji"))

for x in student:
    print(x)

if "mass" in student:
    print("mass is here")