n = int(input("Input: "))

isEven = True
while n>0:
    digit = n%10
    
    if digit % 2 != 0 or digit == 0 :
        isEven = False
         
    n = n//10

if isEven == True:
    print("Output: All Even")
else:
    print("Output: Not All Even")