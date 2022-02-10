
cp = int(input("Enter the cost price : "))
sp = int(input("Enter selling price : "))

if cp > sp :
    print("there is a loss of : ", cp - sp)

if sp > cp:
    print("there is a profit of : ", sp - cp)

if sp == cp:
    print("there is no loss no profit")