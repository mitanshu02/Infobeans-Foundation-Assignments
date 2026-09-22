s = input("Enter string: ")

ans = [""]

for ch in s:
    new = []

    for word in ans:
        for i in range(len(word) + 1):
            temp = word[:i] + ch + word[i:]

            if temp not in new:
                new.append(temp)

    ans = new

for word in ans:
    print(word)




s = input("Enter string: ")

ans = [""]

for ch in s:
    new = []

    for word in ans:
        for i in range(len(word) + 1):
            new.append(word[:i] + ch + word[i:])

    ans = new

for word in ans:
    print(word)


n = int(input("Enter N: "))
passwords = input("Enter passwords: ").split()

count = 0

for i in range(n):
    for j in range(i + 1, n):

        common = False

        for ch in passwords[i]:
            if ch in passwords[j]:
                common = True
                break

        if not common:
            count += 1

print(count)




n = int(input("Enter N: "))

players = []

for i in range(n):
    player_id, name, runs = input().split()
    players.append((int(player_id), name, int(runs)))

# Display all records
print("All Players:")
for player in players:
    print(player)

# Highest and lowest
highest = players[0]
lowest = players[0]

total = 0

for player in players:
    total += player[2]

    if player[2] > highest[2]:
        highest = player

    if player[2] < lowest[2]:
        lowest = player

print("Highest:", highest)
print("Lowest:", lowest)

# Total and average
print("Total Runs:", total)
print("Average Runs:", total / n)

# Players scoring > 50
print("Players scoring more than 50:")
for player in players:
    if player[2] > 50:
        print(player)



Diff by 1 char

s1 = input()
s2 = input()

if abs(len(s1) - len(s2)) > 1:
    print(False)

elif len(s1) == len(s2):
    count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    print(count == 1)

else:
    if len(s1) > len(s2):
        long = s1
        short = s2
    else:
        long = s2
        short = s1

    i = 0
    j = 0
    difference = 0

    while i < len(long) and j < len(short):
        if long[i] == short[j]:
            i += 1
            j += 1
        else:
            difference += 1
            i += 1

            if difference > 1:
                break

    if difference <= 1:
        difference += 1

    print(difference == 1)


LPS


s = input()

n = len(s)

for length in range(n - 1, 0, -1):

    prefix = s[:length]
    suffix = s[n-length:]

    if prefix == suffix:
        print(prefix)
        break
else:
    print("Not Found")