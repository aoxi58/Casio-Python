def dec_vers_bin(n):
    somme=""
    while n!=0:
        reste= n%2
        n=n//2
        somme=str(reste)+somme
    return somme

def hex_vers_dec(n):
    nn=str(n)
    Somme=0
    L=len(nn)
    for i in range(L-1,-1,-1):
        
        if nn[i]=='A':
            val="10"
        elif nn[i]=="B":
            val="11"
        elif nn[i]=="C":
            val="12"
        elif nn[i]=="D":
            val="13"
        elif nn[i]=="E":
            val="14"
        elif nn[i]=="F":
            val="15"
        else:
            val=nn[i]
        Res=int(val)*16**(L-1-i)
        Somme=Somme+Res
        
    return Somme


print(dec_vers_bin(hex_vers_dec(input("entre : "))))