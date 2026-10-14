from models import Movie

m1 = Movie(101, "Dangal", "Drama", 8.4, 250)
m2 = Movie(102, "Jawan", "Action", 7.5, 300)
m3 = Movie(103, "3Idiots", "Drama", 8.4, 200)
m4 = Movie(104, "Bahubali", "Action", 8.1, 350)
m5 = Movie(105, "Pathaan", "Action", 7.0, 320)

movies = [m1, m2, m3, m4, m5]

while True:
    print("""
1. Display all movies.
2. Display movies having rating greater than 8.
3. Display all Action movies.
4. Find the highest-rated movie.
5. Search a movie using Movie ID.
6. Calculate average movie rating.
7. Display movies having ticket price greater than 300.
8. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Movie Information ----")
        print()

        for mov in movies:
            mov.display()

    elif n == 2:
        print("---- Movies With Rating Greater Than 8 ----")
        print()

        for mov in movies:
            if mov.rating > 8:
                print(f"{mov.movie_name:15}|{mov.rating}")

    elif n == 3:
        print("---- Action Movies ----")
        print()

        for mov in movies:
            if mov.genre.lower() == "action":
                print(mov.movie_name)

    elif n == 4:
        highest = 0
        movId = None

        for mov in movies:
            if mov.rating > highest:
                highest = mov.rating
                movId = mov.movie_id

        for mov in movies:
            if mov.movie_id == movId:
                print("---- Highest Rated Movie ----")
                print(f"{mov.movie_name} = {mov.rating}")
                break

    elif n == 5:
        movId = int(input("Enter Movie ID: "))

        for mov in movies:
            if mov.movie_id == movId:
                print("---- Movie Found ----")
                mov.display()
                break
        else:
            print("[ Movie Not Found ]")

    elif n == 6:
        total = 0

        for mov in movies:
            total += mov.rating

        average = total / len(movies)

        print("Average Movie Rating:", round(average, 2))

    elif n == 7:
        print("---- Movies With Ticket Price Greater Than 300 ----")
        print()

        for mov in movies:
            if mov.ticket_price > 300:
                print(f"{mov.movie_name:15}|{mov.ticket_price}")

    elif n == 8:
        print("[ Exiting Program ]")
        break

    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue