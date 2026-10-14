subscription = input("Subscription = ").lower()
progress = int(input("Progress = "))
score = int(input("Test Score = "))

if subscription == "premium":
    if progress >= 80:
        if score >= 70:
            print("Access Status = Unlock Certificate")
        else:
            print("Access Status = Retry Test")
    else:
        print("Access Status = Complete Course")
elif subscription == "basic":
    if progress >= 50:
        print("Access Status = Limited Access")
    else:
        print("Access Status = Lock Content")
else:
    print("Access Status = Access Denied")