import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk
from nltk.corpus import stopwords as nltk_stopwords
from io import StringIO

class Recommendation_system:

    def __init__(self):
        self.results = {}

    def initialization_matrix(self,json):
        ds = pd.read_json(json,lines=True)
        # nltk.download()
        stopwords = set(nltk_stopwords.words('russian'))
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words=stopwords)
        tfidf_matrix = tf.fit_transform(ds['text_twit'].values.astype('U'))
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        for idx, row in ds.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-20:-1]
            similar_items = [(cosine_similarities[idx][i], ds['_id'][i]) for i in similar_indices]
            self.results[row['_id']] = similar_items[1:]

    def recommend(self,item_id, num):
        recs = self.results[item_id][:num]
        result_array = []
        for rec in recs:
            result_array.append(rec[1])
        return result_array

