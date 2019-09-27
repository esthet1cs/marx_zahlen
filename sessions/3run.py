# coding: utf-8
import json
get_ipython().magic('ls misc')
with open('misc/digits.json', 'r') as f:
    digits = json.loads(f.read())
    
digits
with open('misc/pages.json', 'r') as f:
    pages = json.loads(f.read())
    
len(pages)
pages[0]
pages[1]
pages[2]
pages[3]
pages[5]
pages[9]
pages[4]
pages[6]
# first page of the book pages numbering starts at pages[7], so pagecount = index +7
# get rid of linebreads (change them to spaces)
for page in pages:
    page = page.replace('\n',' ')
    
pages[0]
test = 'hallo 1,2,3'
test.replace(',', ' ')
pages = [page.replace('\n', ' ') for page in pages]
pages[0]
pages2 = []
        
for page in pages:
    for key, val in digits.items():
        pages2.append(page.replace(key, str(val)))
        
        
pages2[0]
count = 0
for page in pages2:
    if 'Million' in page:
        count += 1
        
count
digits
count = 0
for page in pages2:
    if 'drei' in page:
        count += 1
        
count
pages2 = []
for page in pages:
    for word, digit in digits.items():
        page = page.replace(word, str(digit))
    pages2.append(page)
    
len(pages2)
pages2[20]
count = 0
for page in pages2:
    if 'zwei' in page:
        count += 1
        
count
for page in pages2:
    if 'Million' in page:
        count += 1
        
count
for page in pages2:
    if 'drei' in page:
        count += 1
        
count
import re
p = re.compile(r'[0-9]\)')
q = re.compile(r'[0-9] [0-9]')
p.match(pages[0])
p.match(pages[1])
p.match(pages[2])
p.match(pages[3])
p.match(pages[4])
p.match(pages[5])
p.match(pages[10])
print(p.match(pages[22]))
for page in pages2:
    print(p.match(page))
    
for page in pages2:
    print(q.match(page))
    
p = re.compile('[0-9]\)')
for page in pages2:
    if p.match(page) != None:
        print('ya')
        
test = 'hallo 16) ja das ist so'
print(p.match(test))
p = re.compile('[0-9]')
print(p.match(test))
result = p.match(test)
re.match('[0-9]', test)
print(re.match('[0-9]', test))
test
print(re.match('[0-9].', test))
print(re.match('so', test))
p = re.compile('[0-9]\)')
p.search(test)
print(p.search(test))
result = p.search(test)
result.group()
test = '1 000000'
q
result = q.search(test)
result.group()
#replace all spaces between numbers to catch 2 million type of strings
count = 0
import string
string.digits
           
count
count = 0
for page in pages2:
    for i in range(1,len(page)-2):
        if page[i] in string.digits and page[i+1] == ' ' and page[i+2] in string.digits:
            count += 1
            print(page[i-5:i+5])
            
for page in pages2:
    if 'Million' in page:
        print('oops')
        
len(pages2)
count = 0
for page in pages:
    if 'Million' in page:
        count += 1
        
count
test
test = 'hallo'
test = test.replace('a','b')
test
test = 'zwei Millionen euro'
test = test.replace('Millionen', '000000')
test
di = {'Million': '000000'}
for word, digit in di.items():
    test = test.replace(word,digit)
    
test
test = 'zwei Millionen euro'
for word, digit in di.items():
    test = test.replace(word,digit)
    
test
testlist = []
testlist.append(test.replace('zwei','2'))
testlist
digits
digits['Millionen'] = '000000'
digits
del digits['millionen']
digits
del digits['Millionen']
for page in pages:
    if 'zwei' in page:
        print('zwei')
        
for page in pages2:
    if 'zwei' in page:
        print('zwei')
        
pages3 = []
digits
digits[' Millionen'] = '000000'
for page in pages:
    for word, digit in digits.items():
        page = page.replace(word, str(digit))
    pages3.append(page)
    
    
len(pages3)
for page in pages3:
    if 'Million' in page:
        print('oo')
        
digits['einer Million'] = '000000'
for page in pages3:
    if 'Millionen' in page:
        print('oo')
        
pages3 = []
for page in pages:
    for word, digit in digits.items():
        page = page.replace(word, str(digit))
    pages3.append(page)
    
    
for page in pages3:
    if 'Millionen' in page:
        print('oo')
        
for page in pages3:
    if 'Millionen' in page:
        print('oo')
        
for page in pages3:
    if 'Million' in page:
        print('00')
        
digits
for page in pages3:
    if 'Million' in page:
        print(page)
        
        
digits
for page in pages:
    if ' acht ' in page:
        print(8)
        
for page in pages:
    if ' vier ' in page:
        print(4)
        
        
for page in pages:
    if ' elf ' in page:
        print(11)
        
        
        
digits
digits[' acht '] = '8'
del digits['acht']
digits[' vier '] = '4'
del digits['vier']
digits[' elf '] = '11'
del digits['elf']
digits
for number in ['zwei','drei','fünf','sechs','sieben','neun']:
    del digits[number]
    
digits[' zwei '] = 2
digits[' drei '] = 3
digits[' vier '] = 4
digits[' fünf '] = 5
digits[' sechs '] = 6
digits[' sieben '] = 7
digits[' acht '] = 8
digits[ 'neun '] = 9
digits
digits[' neun '] = 9
del digits['neun ']
digits
digs = digits.copy()
digs
        
for key, val in digs.items():
    if val == 0.3333333333333333:
        digits[key] = 0.3
        
        
for key,val in digs.items():
    if val == 0.6666666666666666:
        digits[key] = 0.6
        
digits
pages3 = []
for page in pages:
    for word, digit in digits.items():
        page = page.replace(word, str(digit))
    pages3.append(page)
    
    
len(pages3)
get_ipython().magic('ls ')
import helpers
helpers.count
counts = {}
counts = []
counts = [helpers.count(page) for page in pages3]
len(counts)
import matplotlib.pyplot as plt
plt.plot(counts)
plt.ylabel('Zahlenanteil (%)')
plt.xlabel('Seitenzahl')
plt.suptitle('Anteil Ziffern pro Seite')
plt.show()
for count in range(len(counts)):
    if count > 8:
        print('Page ' + str(count))
        print('\n')
        print(pages3[count])
        print('\n\n\n')
        
for count in range(len(counts)):
    if count > 8:
        print('Page ' + str(count) + ': ' + str(counts[count]) + ' Prozent Zahlen.')
        print('\n')
        print(pages3[count])
        print('\n\n\n')
        
        
for count in range(len(counts)):
    if counts[count] > 8:
        print('Page ' + str(count) + ': ' + str(counts[count]) + ' Prozent Zahlen.')
        print('\n')
        print(pages3[count])
        print('\n\n\n')
        
        
plt.suptitle('Anteil Ziffern pro Seite')
plt.plot(counts)
plt.xlabel('Seitenzahl')
plt.ylabel('Zahlenanteil (%)')
plt.show()
sum(counts)/len(counts)
median(counts)
import statistics
median(counts)
statistics.median(counts)
plt.plot(counts)
plt.ylabel('Zahlenanteil (%)')
plt.xlabel('Seitenzahl')
plt.suptitle('Anteil Ziffern pro Seite')
plt.show()
pages4 = []
for page in pages3:
    for i in range(1,len(page)-1):
        if page[i] == ',' and page[i-1] in string.digits and page[i+1] in string.digits:
            newpage += ''
        else:
            newpage += i
    pages4.append(newpage)
    
for page in pages3:
    newpage = page[0]
    for i in range(1,len(page)-1):
        
        if page[i] == ',' and page[i-1] in string.digits and page[i+1] in string.digits:
            newpage += ''
        else:
            newpage += i
    newpage += page[-1]
    pages4.append(newpage)
    
    
pages4 = []
for page in pages3:
    newpage = page[0]
    for i in range(1,len(page)-1):
        
        if page[i] == ',' and page[i-1] in string.digits and page[i+1] in string.digits:
            newpage += ''
        else:
            newpage += page[i]
    newpage += page[-1]
    pages4.append(newpage)
    
    
pages4[10]
# make a list of all the numbers
numbers = []
def get_numbers(text):
    '''
    extract numbers from a text
    '''
    numbers = []
    number = ''
    for char in text:
        if char in string.digits:
            number += char
        else:
            if number != '':
                numbers.append(number)
            number = ''
    return numbers
numbers
numbers = [get_numbers(page) for page in pages4]
len(numbers)
nums = numbers.copy()
nums = []
for field in numbers:
    for number in field:
        nums.append(number)
        
numbers = list(set(nums))
numbers.sort()
numbers[-1]
numbers[0]
len(numbers)
numbers[-10:]
numbers = [int(number) for number in numbers]
numbers.sort()
numbers[-1]
plt.plot(numbers)
plt.show()
numbers[-1]
count = 0
for page in pages4:
    if 'Milliarde' in page:
        count += 1
        
count
for page in pages4:
    if 'Milliarde' in page:
        count += 1
        print(page)
        
count
count = 0
for page in pages4:
    if '000000' in page:
        count += 1
        
count
for page in pages4:
    if '6000000' in page:
        count += 1
        
count
for page in pages4:
    if '6000000' in page:
        count += 1
        print(page)
        
get_ipython().magic('ls ')
get_ipython().magic('ls sessions')
get_ipython().magic('save sessions/3.py 1-247')
