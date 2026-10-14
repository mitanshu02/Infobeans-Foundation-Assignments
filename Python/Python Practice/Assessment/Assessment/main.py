from string_operations import generate_substring
from list_operations import minimumSub

while True:
    print("""
========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit
""")

    n = int(input("Select an operation: "))
    match n:
        case 1:
            s = input("Enter string: ")

            generate_substring(s)

        case 2:
            arr = []
            n = int(input("Enter number of elements: "))

            for i in range(n):
                arr.append(int(input()))

            target = int(input("Enter target number: "))

            print("Minimum Subarray : ",minimumSub(arr,target))
        case 3:
            print("exiting")
            break