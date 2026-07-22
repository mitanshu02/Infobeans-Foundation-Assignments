import random,time

# user variables 

user_name = "Guest"
user_age = 0
difficulty_tier = "Rookie"
base_time_limit = 15.0

#Analytics Variables

total_games_played = 0
total_questions_attempted = 0
total_questions_correct = 0
total_time_spent = 0.0      
total_math_coins = 0

#Subject wise Matrices
#attempted
sum_product_attempted = 0
algebra_attempted = 0
roots_attempted = 0
percent_attempted = 0
fin_attempted = 0

#correct
sum_product_correct = 0
algebra_correct = 0
roots_correct = 0
percent_correct = 0
fin_correct = 0

#inventory and store variables
owned_shields = 0
badge_ninja_unlocked = False

while True:
    print("\n==================================================")
    print("        NUMIGO: ADVANCED MATH VANGUARD OS         ")
    print("==================================================")
    print(f" PROFILE: {user_name} ({user_age} yrs) | TIER: {difficulty_tier}")
    print(f" WALLET: 🪙  {total_math_coins} Coins")
    print("==================================================")
    print("1. -> Initialize/Update User Profile 👤")
    print("2. -> Enter Gameplay Arena 🎮 (Infinite, Blitz, Bomb)")
    print("3. -> Visit Reward Vault & Shop 💰")
    print("4. -> View Live Performance Analytics 📊")
    print("5. -> Shutdown System 🚪")
    print("==================================================")


    choice = int(input("Select a system module (1-5): "))
    
    match choice:
        case 1:
            print("\n==================================================")
            print("          USER PROFILE INITIALIZATION DESK         ")
            print("==================================================")
            
            user_name = input("Enter player name: ")
            user_age = int(input("Enter player age: "))
            
            print("\nChoose Your Mathematical Starting Tier:")
            print("1. Rookie       (Ages 6-9: Friendly ranges, longer clocks)")
            print("2. Challenger   (Ages 10-13: Advanced variables, standard pacing)")
            print("3. Grandmaster  (Ages 14+: Squares, roots, hyper-speed processing)")
            print("--------------------------------------------------")
            
            tier_choice = int(input("Select tier (1-3): "))
            
            match tier_choice:
                case 1:
                    difficulty_tier = "Rookie"
                    base_time_limit = 20.0
                case 2:
                    difficulty_tier = "Challenger"
                    base_time_limit = 15.0
                case 3:
                    difficulty_tier = "Grandmaster"
                    base_time_limit = 10.0
                case _:
                    print("\n[INVALID SELECTION] Defaulting to Rookie tier boundaries.")
                    difficulty_tier = "Rookie"
                    base_time_limit = 20.0
            
            print(f"\n[SUCCESS] Profile synced! Welcome Commander {user_name}.")
            print(f"Your operational response limit is locked at {base_time_limit} seconds.")

        case 2:
            while True:
                print("\n==================================================")
                print("             NUMIGO: GAMEPLAY ARENA               ")
                print("==================================================")
                print("1. The Infinite Tower Climb 🧗‍♂️ (Endless Survival)")
                print("2. The 60-Second Blitz ⚡      (Time Attack)")
                print("3. The 5-Task Bomb Defusal 🚨   (High-Stakes Racing)")
                print("4. Return to Main Dashboard 🚪")
                print("==================================================")
                
                arena_choice = int(input("Select an arena challenge (1-4): "))
                
                match arena_choice:
                    case 1:
                        print("\n[LAUNCHING] Entering Infinite Tower Climb...")
                        
                        #variables 
                        lives = 3
                        current_score = 0
                        streak = 0
                    

                        while lives > 0:
                            if difficulty_tier == "Rookie":
                                num_min,num_max = 2,10
                                time_limit = 20.0
                            elif difficulty_tier == "Challenger":
                                num_min,num_max = 5,25
                                time_limit = 15.0
                            elif difficulty_tier == "Grandmaster":
                                num_min,num_max = 10,100
                                time_limit = 10.0
                            else:
                                num_min,num_max = 2,10
                                time_limit = 20.0

                            num_a = random.randint(num_min, num_max)
                            num_b = random.randint(num_min, num_max)

                            correct_answer = num_a + num_b

                            print("\n==================================================")
                            print(f" STREAK: 🔥 {streak} | SCORE: {current_score} | LIVES: {'█ ' * lives}")
                            print("==================================================")
                            print(f" QUESTION: What is {num_a} + {num_b}?")
                            print("==================================================")

                            start_time = time.time()
                            user_input = input("Enter your answer: ")
                            end_time = time.time()    

                            time_taken = end_time - start_time
                            print(f"⏱️ Speed: {time_taken:.2f} seconds")

                            total_questions_attempted += 1
                            sum_product_attempted += 1
                            total_time_spent += time_taken

                            if user_input.isdigit():
                                player_ans = int(user_input)
                            else:
                                player_ans = -9999

                            if time_taken > time_limit:
                                print()
                                print("==================================================")
                                print(f"[FAILED] you took {time_taken} s | Time Limit: {time_limit} s")
                                if owned_shields > 0:
                                    owned_shields = owned_shields - 1
                                    print("==================================================")
                                    print(f"[SHIELD USED] Now you have {owned_shields} left")
                                else:
                                    lives = lives - 1
                                    streak = 0

                            elif player_ans == correct_answer:
                                total_questions_correct += 1
                                sum_product_correct += 1
                                streak += 1

                                if time_taken <= 4.0:
                                    points_earned = 200
                                    coins_earned = 5
                                    print("==================================================")
                                    print("⚡ [LIGHTNING] Speed Bonus! Double points and +5 Coins!")
                                else:
                                    points_earned = 100
                                    coins_earned = 2
                                    print("✅ [CORRECT] Solid computation! +2 Coins.")
                                
                                current_score += points_earned
                                total_math_coins += coins_earned

                            else:
                                print(f"❌ [WRONG] Incorrect! The accurate answer was {correct_answer}.")
                                if owned_shields > 0:
                                    owned_shields -= 1
                                    print("🛡️ [SHIELD CHARM CONSUMED] Your life count was protected!")
                                else:
                                    lives -= 1
                                streak = 0

                        total_games_played += 1
                        print("\n==================================================")
                        print("              💥 G A M E   O V E R 💥              ")
                        print("==================================================")
                        print(f" Final Score Cleared: {current_score}")
                        print(f" Total Math Coins in Wallet: 🪙  {total_math_coins}")
                        print("==================================================")
                            
                        input("\nPress Enter to return to Arena Menu...")
                        
                    case 2:
                        print("==================================================")
                        print("\n[LAUNCHING] Entering 60-Second Blitz...")
                        print("==================================================")

                        blitz_score = 0
                        questions_answered = 0
                        total_questions_attempted += 1
                        blitz_start = time.time()
                        total_duration = 60.0

                        while (time.time() - blitz_start) < total_duration:
                            time_remaining = total_duration - (time.time() - blitz_start)
                            
                            print("\n============================================================")
                            print(f"       ⌛ T I M E   L E F T : {int(time_remaining)} s | SCORE: {blitz_score} ⌛")
                            print("============================================================")

                            if difficulty_tier == "Rookie":
                                num_min, num_max = 2, 10
                            elif difficulty_tier == "Challenger":
                                num_min, num_max = 5, 25
                            elif difficulty_tier == "Grandmaster":
                                num_min, num_max = 10, 100
                            else:
                                num_min, num_max = 2, 10

                            operators = ["+", "-", "*", "/"]
                            hidden_sign = random.choice(operators)
                            num_b = random.randint(num_min, num_max)
                            
                            if hidden_sign == "/":
                                multiplier = random.randint(2, 5)
                                num_a = num_b * multiplier
                            else:
                                num_a = random.randint(num_min, num_max)
                                
                            if hidden_sign == "-" and num_a < num_b:
                                num_a, num_b = num_b, num_a

                            match hidden_sign:
                                case "+": correct_result = num_a + num_b
                                case "-": correct_result = num_a - num_b
                                case "*": correct_result = num_a * num_b
                                case "/": correct_result = num_a // num_b

                            print(f"What sign goes here?  {num_a} [ ? ] {num_b} = {correct_result}")
                            
                            q_start = time.time()
                            user_input = input("Enter operator (+, -, *, /): ").strip()
                            q_end = time.time()
                            
                            time_taken = q_end - q_start
                            questions_answered += 1
                            
                            if (time.time() - blitz_start) >= total_duration:
                                print("\n⏰ Time ran out before input was processed!")
                                break

                            if user_input == hidden_sign:
                                print(f"✅ CORRECT! Processed in {time_taken:.2f}s.")
                                if time_taken <= 2.0:
                                    blitz_score += 200
                                    blitz_start += 2.0
                                    print("⚡ LIGHTNING SPEED! +200 pts and +2s added to your clock!")
                                else:
                                    blitz_score += 100
                                    print("+100 Points added.")
                            else:
                                blitz_start -= 3.0
                                print(f"❌ WRONG! The correct sign was '{hidden_sign}'.")
                                print("⚠️ Penalty: 3 seconds slashed from your clock!")

                        total_games_played += 1
                        coins_earned = blitz_score // 10
                        total_math_coins += coins_earned
                        
                        print("\n==================================================")
                        print("              ⏰ T I M E ' S   U P ! ⏰            ")
                        print("==================================================")
                        print(f" Total Questions Tackled: {questions_answered}")
                        print(f" Final Blitz Score:       {blitz_score} pts")
                        print(f" Earnings Looted:        🪙 +{coins_earned} Math Coins!")
                        print("==================================================")
                        input("\nPress Enter to return to Arena Menu...")
                        
                    case 3:
                        print("\n==================================================")
                        print("      🚨 BOMB DEFUSAL MODE: RED ALERT 🚨          ")
                        print("==================================================")
                        
                        stability = 100
                        sequences_cleared = 0
                        target_sequences = 5
                        total_questions_attempted += 1
                        
                        print("A dangerous math bomb has been turned on!")
                        print(f"Status: STABILITY {stability}% | CORRECT ANSWERS NEEDED: {target_sequences}")
                        input("Press Enter to start defusing the bomb...")

                        while stability > 0 and sequences_cleared < target_sequences:
                            print("\n==================================================")
                            print(f" BOMB STABILITY: {stability}% [{'█' * (stability // 10):<10}]")
                            print(f" PROGRESS: {sequences_cleared}/{target_sequences} Tasks Done")
                            print("==================================================")

                            if difficulty_tier == "Rookie":
                                num_min, num_max = 2, 10
                            elif difficulty_tier == "Challenger":
                                num_min, num_max = 5, 20
                            elif difficulty_tier == "Grandmaster":
                                num_min, num_max = 10, 50
                            else:
                                num_min, num_max = 2, 10

                            # Mix up the math signs randomly every turn
                            operators = ["+", "-", "*"]
                            current_op = random.choice(operators)
                            
                            num_a = random.randint(num_min, num_max)
                            num_b = random.randint(num_min, num_max)

                            if current_op == "-" and num_a < num_b:
                                num_a, num_b = num_b, num_a

                            match current_op:
                                case "+": correct_result = num_a + num_b
                                case "-": correct_result = num_a - num_b
                                case "*": correct_result = num_a * num_b

                            print(f"⚡ DEFUSE CODE: Solve this fast -> {num_a} {current_op} {num_b} = ?")
                            
                            q_start = time.time()
                            user_input = input("Your Answer: ").strip()
                            q_end = time.time()
                            
                            time_taken = q_end - q_start

                            try:
                                player_ans = int(user_input)
                            except ValueError:
                                player_ans = -9999

                        
                            if player_ans == correct_result and time_taken <= base_time_limit:
                                sequences_cleared += 1
                                print(f"🔓 CODE ACCEPTED! Solved in {time_taken:.2f} seconds.")
                            else:
                                stability -= 25
                                print("\n💥 [WARNING] THE BOMB TICKED FASTER!")
                                if time_taken > base_time_limit:
                                    print(f"Reason: You took too long! ({time_taken:.2f}s / Max time: {base_time_limit}s)")
                                else:
                                    print(f"Reason: Wrong number! The correct answer was {correct_result}.")

                        total_games_played += 1

                        if sequences_cleared == target_sequences:
                            coins_earned = 40
                            total_math_coins += coins_earned
                            print("\n==================================================")
                            print("     🎉 SUCCESS! THE BOMB IS DEFUSED! 🎉           ")
                            print("==================================================")
                            print(f" Reward Bounty: 🪙 +{coins_earned} Math Coins!")
                            print("==================================================")
                        else:
                            print("\n==================================================")
                            print("          💥 💥 K A - B O O M ! 💥 💥             ")
                            print("==================================================")
                            print(" Stability hit 0%. The bomb exploded!")
                            print("==================================================")

                        input("\nPress Enter to return to Arena Menu...")
                        
                    case 4:
                        print("\nExiting Arena... Returning to Main Dashboard.")
                        break 
                        
                    case _:
                        print("\n[ERROR] Choice invalid. Please pick a battle arena (1-4).")

        case 3:
            while True:
                print("\n==================================================")
                print("             💰 THE REWARD VAULT & SHOP 💰          ")
                print("==================================================")
                print(f" Your Current Balance: 🪙 {total_math_coins} Math Coins")
                print("==================================================")
                print("1. Safety Shield (Cost: 50 Coins) 🛡️")
                print("   -> Protects your life count if you make a mistake.")
                print(f"      [You own: {owned_shields}]")
                print("\n2. Premium Title: 'Number Ninja' (Cost: 150 Coins) 🥷")
                print("   -> Permanently displays this badge on your main menu.")
                print(f"      [Unlocked: {badge_ninja_unlocked}]")
                print("\n3. Return to Main Dashboard 🚪")
                print("==================================================")
                
                shop_choice = input("Select an item to buy (1-3): ").strip()
                
                match shop_choice:
                    case "1":
                        if total_math_coins >= 50:
                            total_math_coins -= 50
                            owned_shields += 1
                            print("\n🎉 SUCCESS! You bought 1 Safety Shield.")
                        else:
                            print("\n❌ DENIED! You do not have enough Math Coins.")
                            
                    case "2":
                        if badge_ninja_unlocked:
                            print("\n You have already unlocked the 'Number Ninja' title!")
                        elif total_math_coins >= 150:
                            total_math_coins -= 150
                            badge_ninja_unlocked = True
                            print("\n🎉 SUCCESS! You are now a certified Number Ninja.")
                        else:
                            print("\n❌ DENIED! You do not have enough Math Coins.")
                            
                    case "3":
                        print("\nExiting shop... Returning to main menu.")
                        break
                        
                    case _:
                        print("\n[ERROR] Invalid choice. Please pick 1, 2, or 3.")
                        
                input("\nPress Enter to update terminal...")

        case 4:
            print("\n========================================================")
            print("│            📊 LIVE PERFORMANCE REPORT CARD 📊          │")
            print("==========================================================")
            print(f"  👤 Player Profile:  {user_name}                        ")
            print(f"  ⚙️  Difficulty Tier: {difficulty_tier}                 ")
            print("===========================================================")
            print(f"  🕹️  Total Games Played:  {total_games_played}          ")
            print(f"  ⚔️  Questions Attempted: {total_questions_attempted}   ")
            print(f"  🎯  Questions Correct:   {total_questions_correct}     ")
            
        
            if total_questions_attempted > 0:
                accuracy = (total_questions_correct / total_questions_attempted) * 100
                print(f"  🔥  Overall Accuracy:    {accuracy:.1f}% ")
            else:
                print("  🔥  Overall Accuracy:    0.0% ")
                
            print(f"  ⏱️  Total Time Spent:    {total_time_spent:<6.1f} seconds ")
            print("===========================================================")
            print("  🌟 TOPIC BREAKDOWN                                    ")
            print(f"  🔸 Sums & Products Attempted: {sum_product_attempted} ")
            print(f"  🔸 Sums & Products Correct:   {sum_product_correct}  ")
            print("===========================================================")
            
            input("\nPress Enter to return to Main Dashboard...")

        case 5:
            print()
            print("==================================================")
            print("       🚪 SHUTTING DOWN NUMIGO ENGINE")
            print("==================================================")
            break