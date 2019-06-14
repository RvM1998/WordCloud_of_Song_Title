import pandas as pd
import re

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)

df = pd.read_csv('music.csv')
d=df[['title']].groupby("title")
d.sum().reset_index().to_csv('m.csv',index=False)
text=""
replace_list=['Version','Album','Digital','Remaster','Mix','Remix','featuring','feat','La','LP','De','Live','Time','Le','Song','Blue','de','Explicit','El','Mi','Original']
with open('m.csv','r') as input :
    for r,l in enumerate(input):
        l= re.sub(r'|'.join(map(re.escape, replace_list)), '', l)
        text +=l



    wordcloud = WordCloud(width=800, height=800,
                          stopwords=stopwords,
                          background_color='white',
                          min_font_size=10).generate(text)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()