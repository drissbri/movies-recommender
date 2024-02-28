import re
from sklearn.feature_extraction.text import TfidfVectorizer

class Nlp :
    def __init__(self, stopwords, negative_words, positive_words, tfidf_dataset):
        self.stopwords = stopwords
        self.negative_words = negative_words
        self.positive_words = positive_words
        self.tfidf_dataset = tfidf_dataset

    
    def clean_text(self,text):
        text = text.lower()
        text = re.sub(r'\b\d+\b', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def remove_stopwords(self,text):
        return ' '.join([word for word in text.split() if word not in self.stopwords])

    def analyze_sentiment(self,text):
        text = self.clean_text(text)
        text = self.remove_stopwords(text)
        positive_count = sum(word in self.positive_words for word in text.split())
        negative_count = sum(word in self.negative_words for word in text.split())
        if positive_count > negative_count:
            return 1
        elif negative_count > positive_count:
            return 0
        else:
            return None
        
    
    def extract_keywords_with_tfidf(self, text):
        cleaned_text = self.clean_text(text)
        cleaned_text = self.remove_stopwords(cleaned_text)
        
        tfidf_vectorizer = TfidfVectorizer(stop_words=self.stopwords)
        tfidf_vectorizer.fit(self.tfidf_dataset)
        
        response = tfidf_vectorizer.transform([cleaned_text])
        feature_names = tfidf_vectorizer.get_feature_names_out()
        
        scores = zip(feature_names, [val for val in response.toarray()[0]])
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        
        return [word for word, score in sorted_scores if score > 0]

