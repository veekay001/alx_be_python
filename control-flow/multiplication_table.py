X = int(input("Enter a number to see its multiplication table: "))

for Y in range(1, 11):
    Z = X * Y
    print("%d * %d = %d" % (X, Y, Z))