#24 Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False
# Solution 1 (time complexity : O(n), Space Complexity: O(n))

s = input("Enter String:")

unique = set(s)

if len(unique) == len(s):
    print("True")
else:
    print("False")

# Solution 2 (TC = O(n) , SC = O(n), But can terminate early)

# seen = set()

# for ch in s:
#     if ch in seen:
#         return False
#     seen.add(ch)

# return True