data = input("Data = ")
DATA = int(data.replace("GB",""))

print(f"In MB = {DATA*1024}")
print(f"In KB = {DATA*1024*1024}")