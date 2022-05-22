def bin_vers_dec(n):
    nn=str(n)
    Somme=0
    L=len(nn)
    for i in range(L-1,-1,-1):
        Res=int(nn[i])*2**(L-1-i)
        Somme=Somme+Res
    return Somme


print(bin_vers_dec(input("entre : ")))