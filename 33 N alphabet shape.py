# N alphabet shape - star pattern

for row in range(0,7):
    for col in range(0,7):
        if(col==0 or col==6 or row==col and(col>0)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

