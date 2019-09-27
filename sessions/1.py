# coding: utf-8
import string
import seaborn as sns
get_ipython().magic('ls texts')
get_ipython().magic('ls ')
get_ipython().magic('ls text')
with open('text/marx_kapital01_kurz.txt', 'r') as f:
    text = f.read()
    
len(text)
with open('text/marx_kapital01_kurz.txt', 'r') as f:
    text = f.read()
    
len(text)
# see the ratio of numbers and letters per page
# build buckets: put every page in its own list
# count all numbers 
# build the quotient of numbers per total characters
# normalize that count to percent
# make a list of these counts, every count represents a page
# plot the list
pages = text.split('^L')
len(pages)
pages = text.split('\f')
len(pages)
pages[0]
len(pages[0])
# remove all linebreaks
pages[0].remove('\n')
pages[0].replace('\n',' ')
text.replace('\n',' ')
text = text.replace('\n',' ') # change linebreaks to spaces because they just take one character
text = text.replace('  ',' ') # remove double spaces that were inserted by the previous step
len(text)
pages = text.split('\f') # split the text according to the pages (we are analyzing a book).
len(pages)
pages[0]
def count(text):
    '''
    count the number of numbers in a text and return the percentage of numbers (every numeral is counted, so 1842 is four numbers)
    '''
    count = len([char for char in text if char in string.digits]) # count the number of digitis in the text
    percentage = float(count) / float(len(text)) * 100  # compute the percentage
    return percentage
count(pages[0])
count(pages[1])
parts = [count(page) for page in pages]
sns.distplot(parts)
plot = sns.distplot(parts)
plot.show()
import matplotlib as mpl
mpl.plot(percentages)
import matplotlib.pyplot as plt
plt.plot(percentages)
plt.plot(parts)
plt.show()
plt.show()
plt.plot(parts)
plt.ylabel('Zahlenanteil (%)')
plt.xlabel('Seitenzahl')
plt.suptitle('Anteil Zahlen pro Seite')
plt.show()
sns.distplot(parts)
p = sns.distplot(parts)
p.show()
get_ipython().magic('save sessions/1.py 1-55')
