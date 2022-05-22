def dec_vers_bin(n):
    somme=""
    while n!=0:
        reste= n%2
        n=n//2
        somme=str(reste)+somme
    return somme


print(dec_vers_bin(int(input("entre : "))))