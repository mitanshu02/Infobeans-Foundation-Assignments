import math

def checkPerfect(num):
    total = 0
    for i in range(1,(num//2)+1):
        if num%i == 0:
            total += i
    
    if total == num:
        return "True"
    else:
        return "False"

def checkPrime(num):
    if num < 2:
        return "Not Prime Number"
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return "Not a Prime Number" 
        else:
            return "Prime Number"

def reverse(num):
    return int(str(num)[::-1])

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i

    return fact

def factors(num):
    factors = []
    for i in range(1,(num//2)+1):
        if num%i == 0:
            factors.append(i)

    return factors

while True:
    print()
    print("========== Menu ===========")
    print()
    print("""
1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
""")
    print()
    
    n = int(input("Select an option: "))

    match n:
        case 1:
            print()
            n = int(input("Enter Number : "))
            print()
            if checkPerfect(n):
                print(f"{n} is a Perfect Number")
            else:
                print(f"{n} is not a Perfect Number")
        
        case 2:
            print()
            n = int(input("Enter Number : "))
            print()
            print(checkPrime(n))
        case 3:
            print()
            n = int(input("Enter Number : "))
            print()
            print("Reverse Number : ",reverse(n))
        case 4:
            print()
            n = int(input("Enter Number : "))
            print()
            print("Factorial : ",factorial(n))
        case 5:
            print()
            n = int(input("Enter Number : "))
            print()
            print("Factors : ",*factors(n))
        case 6:
            print("==================================")
            print("        Terminating Program       ")
            print("==================================")
            break
        case __:
            continue
    
