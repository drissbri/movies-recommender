from movies_recommender.product import Product
from movies_recommender.recording import Recording

class Movie(Product, Recording):
    def __init__(self, idP, name, description, types, idR=None, duration=None, director=None, budget=None):
        Product.__init__(self, idP, name, description)
        Recording.__init__(self, idR, types, duration)
        self.__director = director
        self.__budget = budget
    
    def find_similar_movie(self, movies, nlp):
        max_keyword_count = 0
        most_similar_movie = None
        keywords = nlp.extract_keywords_with_tfidf(self.get_description())
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