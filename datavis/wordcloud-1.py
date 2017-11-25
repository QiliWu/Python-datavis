from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path

d = path.dirname('__file__')
text = open(path.join(d, '/home/wuqili/datavis/The Count of Monte Cristo.txt')).read()
wordcloud = WordCloud(font_path = '/home/wuqili/datavis/PenguinAttack.ttf',stopwords=STOPWORDS,background_color='#222222',width=1000,height=800).generate(text)

#Open a plot of the generated image.
plt.figure(figsize=(13,13))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()