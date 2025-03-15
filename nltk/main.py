
'''
punkt - tokenisation - break text into individual words / sentences 
wordnet - word relationships 
'''
import nltk
# nltk.download('all')  - got all the pacakges 


from nltk.sentiment import SentimentIntensityAnalyzer

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

analyser = SentimentIntensityAnalyzer()

text1 = ' I am great and like the product'
text2 = ' dont like the product as i cant find the sizes'


print(analyser.polarity_scores(text1))
print(analyser.polarity_scores(text2))

'''
o/p : {'neg': 0.0, 'neu': 0.377, 'pos': 0.623, 'compound': 0.765}
{'neg': 0.209, 'neu': 0.791, 'pos': 0.0, 'compound': -0.2755}
'''

reviews = [
    "The app is amazing! I love the new features.",
    "The battery life is terrible. It drains so quickly.",
    "The user interface is clunky and difficult to navigate.",
    "I'm having issues with crashes. The app keeps freezing.",
    "Overall, it's a good app, but the performance needs improvement.",
    "Great app, works perfectly",
    "This app is the worst. it is so slow",
    "I like the design but it is buggy"
]

# basically pass an array of data -- to figure out the sentiment 

for review in reviews:
    scores = analyser.polarity_scores(review)
    print(f"Review: '{review}'")
    print(f"Sentiment Scores: {scores}")
    if scores['compound'] >= 0.05:
        print("Sentiment: Positive")
    elif scores['compound'] <= -0.05:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")
    print("-" * 20)




# tokenise and remove the common words and puntuncation 

stop_words = set(stopwords.words("english"))

for review in reviews:
    scores = analyser.polarity_scores(review)
    words = word_tokenize(review.lower())
    print(words)
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    keywords = " ".join(filtered_words) #put back into a string for easy printing.

    print(f"Review: '{review}'")
    print(f"Sentiment: {scores['compound']}")
    print(f"Keywords: {keywords}")
    print("-" * 20)


    #  topic modeling - to find themes 
    # recomendation based on total responses 

    #actionale insights of promoters and detractors - what they liked and disliked - need to find theme or pair words here 