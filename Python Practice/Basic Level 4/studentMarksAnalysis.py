s1,s2,s3,s4,s5 = map(int, input("Enter the marks = ").split(","))
total = s1+s2+s3+s4+s5

print(f"Total = {total}")
print(f"Average = {total/5}")
print(f"Percentage = {(total/5)}%")