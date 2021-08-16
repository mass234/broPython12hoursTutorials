# scope

name = "Mass" # global scope (available inside & outside functions)


def display_name():
    name = "channel"  # variable "name" is local scope so
    print(name)    # this variable is only available inside this function

# print(name)
display_name()
print(name)