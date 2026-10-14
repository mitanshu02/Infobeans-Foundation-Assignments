'''
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.

'''
alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

sentence = ""

while True:
    print("""
Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit
""")

    n = int(input("Select an option: "))

    match n:
        case 1:
            sentence = set(input("Enter a sentence: ").lower().replace(" ",""))
        case 2:
            print("Missing Alphabets: ",end = " ")
            print(alpha - sentence)
        case 3:
            print("Count of Missing Alphabet: ",len(alpha - sentence))
        case 4:
            print("Exiting...")
            break
        case _:
            continue