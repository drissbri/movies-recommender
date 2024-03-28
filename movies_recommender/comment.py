from datetime import datetime

class Comment:
    def __init__(self, idC, content, user, movie, nlp,date=datetime.now()):
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
