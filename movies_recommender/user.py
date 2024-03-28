from random import choice

class User:
    def __init__(self, idU, login, passw):
        self.__idU = idU
        self.__login = login
        self.__pass = passw
        self.__liked_movies = []
        self.__disliked_movies = []
    
    def get_idU(self):
        return self.__idU
    
    def get_login(self):
        return self.__login
        
    def add_liked_movie(self, movie):
        self.__liked_movies.append(movie)

    def add_disliked_movie(self, movie):
        self.__disliked_movies.append(movie)

    def recommend_movie(self, movies, nlp):
        # Dictionary to hold recommended movies and their scores
        recommendation_scores = {}
        rated_movies = self.__liked_movies + self.__disliked_movies
        # Iterate over liked movies to find similar ones
        for movie in self.__liked_movies:
            similar_movie = movie.find_similar_movie(movies, nlp)
            if similar_movie and (similar_movie not in rated_movies):
                if similar_movie in recommendation_scores:
                    recommendation_scores[similar_movie] += 1
                else:
                    recommendation_scores[similar_movie] = 1

        # Find the movie with the highest score
        most_recommended = None
        highest_score = 0
        if recommendation_scores:
            for movie, score in recommendation_scores.items():
                if score > highest_score:
                    most_recommended = movie
                    highest_score = score
        else:
            most_recommended = choice([movie for movie in movies if (movie not in rated_movies)])

        return most_recommended
    
    def __str__(self) :
        return f' #{self.get_idU()} |username: {self.get_login()} '