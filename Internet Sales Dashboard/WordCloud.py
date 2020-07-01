# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(VADER_Score, text)
# dataset = dataset.drop_duplicates()



# Paste or type your script code here:

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt 

df = dataset[dataset['VADER_Score']=='Positive']

words = ' '.join(df['text'])
cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

stopwords = set(STOPWORDS)
stopwords.add("amp")
stopwords.add("flight")
stopwords.add("united")
stopwords.add("plane")
stopwords.add("now")

wordcloud = WordCloud(stopwords=stopwords,
                      background_color='white',
                      width=3000,
                      height= 2500
                     ).generate(cleaned_word)
type(cleaned_word)
plt.figure(1,figsize=(20, 20))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
