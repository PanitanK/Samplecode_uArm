from re import I


Y = ['Number ID', 'Name', 'Count', 'Status'],[]
Y = list(Y)
Y.append([1,"Rubber",0,"Out of stock" ])
Y.append([2,"Ruler",5,"In stock"])
Y.append([3,"Pencil",1,"In stock"])
Y.append([4,"Pen",10,"In stock"])
Y.append([5,"Colour pencil",5,"In stock"])
Y.append([6,"A4 Paper",0,"Out of stock"])
Y.pop(1)
print(Y)

stock = Y[0].index("Status")
print("\n\n")
i = 1
while i != len(Y):

    if (Y[i][stock]) == "In stock":
        print(Y[i])
    i += 1
print("\n\n")
i = 1
while i != len(Y):

    if (Y[i][stock]) == "Out of stock":
        print(Y[i])
    i += 1

while True : 

    a = input("Purchase list : ")
    b = input("Amount : ")
    i = 1
    while i != len(Y):
        if (Y[i][1]) == a:
            print("There were " + str(Y[i][2]) + a +"(s)")
            (Y[i][2]) -= int(b)
            print("There are now " + str(Y[i][2]) + a +"(s)")
            if Y[i][2] == 0 :
                Y[i][3] = "Out of stock"
                print(Y[i][3])
        i += 1
    print(Y)
    