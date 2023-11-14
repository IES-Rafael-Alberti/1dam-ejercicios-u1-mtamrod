def mayor(num1, num2):
    if num1<num2:
        return num2
    elif num2<num1:
        return num1
    elif num1==num2:
        return 0

def main(): 
    numA=int(input("Introduce un número: "))
    numB=int(input("Introduce otro número: "))
    print(mayor(numA, numB))
    
if __name__ == "__main__":
    main()