# 'dataset' holds the input data for this script
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#load in the sentiment analyzer
sia=SentimentIntensityAnalyzer()

#apply the analyzer over each comment
dataset['Tweets'] =dataset['text'].apply(lambda x: sia.polarity_scores(x)['compound'])
