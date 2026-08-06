n = int(input("Input: "))

m = str(n)
diff = ""
greatest = 0
sum = 0

for i in range(len(m)-1):
    ch = int(m[i])
    next = int(m[i+1])

    d = abs(next - ch)
    sum = sum + d

    if d > greatest:
        greatest = d

    diff += str(d)

print("Step Difference: ",end = "")

for ch in diff:
    print(ch,end = " ")
print()
print(f"Sum = {sum}")
print(f"Largest = {greatest}")

if sum % len(m) == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")

    
    