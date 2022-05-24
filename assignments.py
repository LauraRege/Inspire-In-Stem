#print a diamond of stars and a triangle of stars
#print
rows = int(input("enter number of rows"))
k = 0
for i in range(1,rows +1):
    for space in range(1,(rows-1)+1):
        print(end=" ")
    while k!= (2*i-1):
        print("*",end="")
        k +=1
    k = 0
    print()

#diamond
h = eval(input("enter diamond's height ; "))
for x in range(h) :
    