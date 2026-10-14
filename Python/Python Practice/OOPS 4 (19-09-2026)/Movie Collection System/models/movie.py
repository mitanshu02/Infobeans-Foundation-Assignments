class Movie:
    def __init__(self, movie_id, movie_name, genre, rating, ticket_price):
        self.__movie_id = movie_id
        self.__movie_name = movie_name
        self.__genre = genre
        self.__rating = rating
        self.__ticket_price = ticket_price

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def movie_name(self):
        return self.__movie_name

    @property
    def genre(self):
        return self.__genre

    @property
    def rating(self):
        return self.__rating

    @property
    def ticket_price(self):
        return self.__ticket_price

    def display(self):
        print(f"{self.__movie_id:10}|{self.__movie_name:15}|{self.__genre:15}|{self.__rating:10}|{self.__ticket_price:10}")