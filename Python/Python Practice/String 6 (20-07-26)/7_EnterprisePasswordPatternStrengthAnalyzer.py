'''
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 isUppercase letter
  * 1 isLowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password
'''

p = input("Input: ")

l = len(p)
isUppercase = False
isLowercase = False
isDigit = False
isSpecial = False
isConsecutiveRepeated = False
space = False

for i in range(l):
    ch = p[i]
    if i>=1 and p[i] == p[i-1]:
        isConsecutiveRepeated = True
    if 'A'<=ch<='Z':
        isUppercase = True 
    elif 'a' <= ch <= 'z':
        isLowercase = True
    elif '0'<=ch<='9':
        isDigit = True
    elif ch == " ":
        space = True
    else:
        isSpecial = True

if isUppercase and isLowercase and isDigit and not space and isSpecial and not isConsecutiveRepeated and l>=10:
    print("Strong Password")
else:
    print("Weak Password")