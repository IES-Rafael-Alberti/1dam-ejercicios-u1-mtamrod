def suma():
    n=int(input("Introduce un número: "))
    nom=str()
    for i in range(n):
        suma=0
        suma=str(n*(n+1)/2)
        n=n-1
        nom+=str(f"{suma}-")
        
    return nom

print(suma())
        
