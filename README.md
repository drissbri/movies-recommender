# Simple Movies Recommendation System


## Description

This project is a content-based movie recommendation system that uses natural language processing (NLP) with TFIDF to recommend movies to users based on their comments and preferences. The system utilizes a dataset of movies, including their descriptions and genres, to understand user preferences and suggest similar movies that they might like.

## Features

- Load and preprocess movie data from a CSV file.
- Utilize TF-IDF (Term Frequency-Inverse Document Frequency) for processing movie descriptions.
- Filter out common stopwords to improve the quality of NLP analysis.
- Analyze user comments to determine preferences for positive and negative sentiments in movies.
- Recommend movies based on user likes and dislikes using content similarity.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourgithub/recommendation_system.git
cd recommendation_system
```

2. **Install required libraries**

Ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install pandas scikit-learn
```

3. **Prepare Data**

- Place your `netflix_titles.csv` in the `movie_data` directory.
- Ensure you have `stopwords.txt`, `positif_words.txt`, and `negatif_words.txt` in the `nlp_data` directory.

## Usage

1. **Run the Recommendation System**

```python
python recommendation_system.py
```

2. **Interact with the System**

- The system will process the dataset and user comments to recommend a movie.
- User interactions are simulated in the code with comments and preferences.

## Project Structure

- `recommendation_system.py` - The main script that runs the recommendation system.
- `Nlp.py` - Contains the NLP processing functionality.
- `Movie.py` - Defines the Movie, User, and Comment classes.
- `movie_data/` - Directory containing the movie dataset.
- `nlp_data/` - Directory containing NLP-related data, such as stopwords and sentiment words.

## Contributing

Feel free to fork the project and submit pull requests.
