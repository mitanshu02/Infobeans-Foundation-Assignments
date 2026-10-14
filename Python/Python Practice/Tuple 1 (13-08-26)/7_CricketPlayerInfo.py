'''
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
'''
players = []

n = int(input("Enter no. of players you want to enter: "))

for i in range(n):
    print(f"Enter details of player {i+1}")
    p_id = input("Enter player id: ")
    p_name = input("Enter player name: ")
    runs = int(input("Enter runs: "))
     
    players.append((p_id,p_name,runs))
    print()

print("All Players Detail: ")
for p in players:
    print(p)

total = 0
highest = players[0][2]
h_idx = 0
lowest = float("inf")
l_idx = 0

for i in range(n):
    total = total + players[i][2]
    
    if players[i][2] > highest:
        highest = players[i][2]
        h_idx = i
    
    if players[i][2] < lowest:
        lowest = players[i][2]
        l_idx = i

print()
print("Highest Scorer: ")
print(players[h_idx])

print()

print("Lowest Scorer: ")
print(players[l_idx])

print()

print("Total Runs: ")
print(total)

print()

print("Average Runs: ")
print(total/n)

print()

print("Player Scored above 50 Runs: ")
for p in players:
    if p[2] > 50:
        print(p) 
