# coding: utf-8

# helper functions for distant reading marx: das kapital, (poetics and narrative of numbers in marx: kapital)

import string
import json

def count(text):
    '''
    count the number of numbers in a text and return the percentage of numbers (every numeral is counted, so 1842 is four numbers)
    '''
    count = len([char for char in text if char in string.digits]) # count the number of digitis in the text
    percentage = float(count) / float(len(text)) * 100  # compute the percentage
    return percentage
