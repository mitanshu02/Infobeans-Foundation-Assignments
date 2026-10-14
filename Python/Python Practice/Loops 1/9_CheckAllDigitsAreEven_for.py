n = int(input("Input: "))

isEven = True
for i in range(len(str(n))):
    digit = n%10
    
    if digit % 2 != 0 or digit == 0 :
        isEven = False
         
    n = n//10

if isEven == True:
    print("Output: All Even")
else:
    print("Output: Not All Even")