# kwargs

# def hello(**kwargs):
#     #print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello",end=" ")

def hello(**names):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")

hello(first = "mass", middle = "py", last = "channel")

