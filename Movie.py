import datetime
import random


class Product:
    def __init__(self, idP, name, description):
        self.__idP = idP
        self.__name = name
        self.__description = description

    def get_description(self):
        return self.__description

    def get_name(self):
        return self.__name
    
    def get_idP(self):
        return self.__idP



class Recording:
    def __init__(self, idR, type, duration):
        self.__idR = idR
        self.__type = type
        self.__duration = duration

    def get_types(self):
        return self.__type



class Movie(Product, Recording):
    def __init__(self, idP, name, description, types, nlp, idR=None, duration=None, director=None, budget=None):
        Product.__init__(self, idP, name, description)
        Recording.__init__(self, idR, types, duration)
        self.__director = director
        self.__budget = budget
        self.__nlp = nlp
    
    def find_similar_movie(self, movies):
        max_keyword_count = 0
        most_similar_movie = None
        keywords = self.__nlp.extract_keywords_with_tfidf(self.get_description())
        self_types = self.get_types()

        for movie in movies:
            if movie.get_name() != self.get_name():
                keyword_count = sum(keyword.lower() in movie.get_description().lower() for keyword in keywords)
                
                type_overlap_count = sum(movie_type in self_types for movie_type in movie.get_types())
                if type_overlap_count > 0:
                    if keyword_count > 0:
                        keyword_count *= (2 ** type_overlap_count)
                    else :
                        keyword_count = type_overlap_count

                if keyword_count > max_keyword_count:
                    max_keyword_count = keyword_count
                    most_similar_movie = movie

        return most_similar_movie

    
    def __str__(self):
        return f' #{self.get_idP()} | name: {self.get_name()} | description: {self.get_description()} | types: {self.get_types()} '



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

    def recommend_movie(self, movies):
        # Dictionary to hold recommended movies and their scores
        recommendation_scores = {}
        rated_movies = self.__liked_movies + self.__disliked_movies
        # Iterate over liked movies to find similar ones
        for movie in self.__liked_movies:
            similar_movie = movie.find_similar_movie(movies)
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
            most_recommended = random.choice([movie for movie in movies if (movie not in rated_movies)])

        return most_recommended
    
    def __str__(self) :
        return f' #{self.get_idU()} |username: {self.get_login()} '



class Comment:
    def __init__(self, idC, content, user, movie, nlp,date=datetime.datetime.now()):
        self.__idC = idC
        self.__content = content
        self.__date = date
        self.__user = user
        self.__movie = movie
        self.__like_dislike = nlp.analyze_sentiment(content)
        
        if self.__like_dislike:
            user.add_liked_movie(movie)
        
        if not self.__like_dislike:
            user.add_disliked_movie(movie)

    def get_user(self):
        return self.__user
    
    def get_idC(self):
        return self.__idC
    
    def get_content(self):
        return self.__content

    def get_movie(self):
        return self.__movie

    def get_likes_dislike(self):
        return self.__like_dislike
    
    def __str__(self):
        return f' #{self.get_idC()} | content: {self.get_content()} \n By: {self.get_user()} \n On: {self.get_movie()} '
