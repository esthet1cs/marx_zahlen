# coding: utf-8
get_ipython().magic('ls misc')
import string
import json
with open('misc/digits.json', 'r') as f:
    digits = json.loads(f.read())
    
digits
# in seiten aufteilen, jede seite eine bag of words
# namen in zahlen umwandeln, seitenweise
# verhältnis berechnen
get_ipython().magic('ls text')
with open('text/02kurz.txt', 'r') as f:
    text = f.read()
    
pages = text.split('\f')
len(pages)
for page in pages:
    page=page.split()
    
len(pages)
len(pages[0])
pages[0]
paragraphs = [page.split('\n\n') for page in pages]
len(paragraphs)
paragraphs[0]
pages[1]
paragraphs[1]
len(paragraphs[1])
len(paragraphs[0])
len(paragraphs[2])
test = 'es war einmal.'
test.split()
type(pages)
pages[0..2]
pages
pages[0]
paragraphs[0]
len(pages)
type(pages)
type(paragraphs)
paragraphs = [liste for liste in paragraph for paragraph in paragraphs]
paragraphs = [[liste for liste in paragraph] for paragraph in paragraphs]
type(paragraphs)
len(paragraphs)
paras = []
for paragraph in paragraphs:
    for liste in paragraph:
        paras.append(liste)
        
len(paras)
paras[0]
paras[1]
paras[2]
paras[3]
paras[4]
paras[5]
with open('misc/paras.json', 'w') as f:
    f.write(json.dumps(paras))
    
with open('misc/pages.json', 'w') as f:
    f.write(json.dumps(pages))
    
get_ipython().magic('save sessions/a.py 1-50')
