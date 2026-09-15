"""
Assignment 11: File Compression System (String Compression)

Write a recursive Python program to compress a given string by counting consecutive occurrences of each character.

For example:
AAABBCCCCD ? A3B2C4D1

Input:
Enter a String:
AAABBCCCCD

Output:
Compressed String = A3B2C4D1

Sample Input:
WWWWXXYYZ

Sample Output:
Compressed String = W4X2Y2Z1

Sample Input:
AAAAA

Sample Output:
Compressed String = A5
"""
a = input("Enter string to compress: ")

def compressed(a,current = 0,prev = 0,count = 0,ans = ""):
    if current == len(a):
        return ans
    if current < len(a)-1:
        if a[current] == a[prev]:
            count += 1
        else:
            ans = ans + a[prev]+str(count)
            count = 1
    else:

        if a[current] == a[prev]:
            ans = ans+a[prev]+str(count+1)
        else:
            ans = ans + a[prev]+str(count)
            ans = ans+a[current]+str(1)
    current = current + 1
    prev = current -1
    return compressed(a,current,prev,count,ans)

print(compressed(a))