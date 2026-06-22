runs = int(input("Total runs = "))
overs = float(input("Overs = "))

oversConverted = overs*10
balls = oversConverted%10
remOvers = oversConverted//10

totalBalls = (remOvers*6)+balls
 
print(f"Total Balls = {int(totalBalls)}")
print(f"Run Rate = {round((runs/totalBalls)*6, 2)}")
