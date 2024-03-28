import random
import pandas as pd

from movies_recommender import Nlp, Movie, User, Comment

testing_size = 1000

# Load the dataset of movies
movies_df = pd.read_csv('movie_data/netflix_titles.csv', nrows=testing_size)


#tfidf training dataset
tfidf_dataset = movies_df['description']

#stopwords
with open('nlp_data/stopwords.txt', 'r', encoding='utf-8') as file1:
    stopwords = file1.read().splitlines()

#positif words
with open('nlp_data/positif_words.txt', 'r', encoding='utf-8') as file2:
    positif_words = file2.read().splitlines()

#negative words
with open('nlp_data/negatif_words.txt', 'r',  encoding='utf-8') as file3:
    negatif_words = file3.read().splitlines()


#initialising Nlp
nlp = Nlp(stopwords, negatif_words, positif_words, tfidf_dataset)

# Create Movie instances from the dataset (choosing only first 500)
movies = []
for i in range(testing_size):
    movie = Movie(idP=i, name=movies_df['title'][i], description=movies_df['description'][i], types=movies_df['listed_in'][i].split(', '))
    movies.append(movie)

# Create user instance
user = User(idU=1, login="user", passw="pass")

# commenting on movies: 
comment1 = Comment(idC=1,content="I like this movie it's good",user=user,movie=random.choice(movies), nlp=nlp)
print(f'-Comment 1 :\n{comment1}')

comment2 = Comment(idC=1,content="wow great movie I like it",user=user,movie=random.choice(movies), nlp=nlp)
print(f'-Comment 2 :\n{comment2}')



# testing the algo
recommended_movie = user.recommend_movie(movies, nlp)
if recommended_movie:
    print(f"-Recommended Movie:\n{recommended_movie}")
else:
    print("No recommendation could be made based on the current likes and dislikes.")