n = int(input("Input: "))

s = str(n)
s = s[::-1]
s = int(s)  # reverse

diff = abs(n-s)

diff = str(diff)

l = len(diff)

if int(diff) == 0:
    ans = "Perfect Match"
elif int(diff)%9 == 0:
    ans = "Verified"

print(f"Reverse = {s} Difference = {diff} Digits = {l} {ans}")


