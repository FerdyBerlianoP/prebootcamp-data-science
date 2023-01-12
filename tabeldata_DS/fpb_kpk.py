def FPB_KPK(x, y):
    
    def FPB(x, y):
        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small+1):
            if((x % i == 0) and (y % i == 0)):
                gcd = i
        return gcd


    def KPK(x, y):
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

    return FPB(x, y), KPK(x, y)


x = int(input("Ketik angka pertama : "))
y = int(input("Ketik angka kedua   : "))


fpb, kpk = FPB_KPK(x, y)


print("FPB dari", x, "dan", y, "adalah :", fpb)
print("KPK dari", x, "dan", y, "adalah :", kpk)