#nested loops

rows = int(input("How many rows?: "))
columns = int(input("How many rcolumns?: "))
symbol = (input("How many simbol?: "))

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

