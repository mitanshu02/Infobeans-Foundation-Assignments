'''
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number

'''

pnr = input("Enter PNR: ")

l = len(pnr) 
if l != 12:
    print("Invalid PNR number")
elif pnr[:3] != "PNR":
    print("Invalid PNR number")
else:
    for i in range(3,len(pnr)):
        ch = pnr[i]
        if not '0'<=ch<='9':
            print("Invalid PNR number")
            break
    else:
        print("Valid PNR number")
            
        