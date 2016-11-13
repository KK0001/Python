for a in range(1,10):
    for b in range(1,10):
        print("{0:3d}".format(a*b), end='')
    print()

#「"{0:3d}".format(a*b)」は、Cでの「""%3d",a*b」と同じ。
