#!/usr/local/bin/python

## first line allows you to double click the file and run as a script


import re 
import pprint 
import os
import nltk
import string
from nltk import WhitespaceTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


complete_vocab = {}
masterlist_file = 'masterlist.txt'
outfile = 'weka_masterlist.txt'
output = []


    
def parse_master_list():
    f = open('.\\1\\10425.txt', 'r')
    for line in f:
        print line
    f.close()    
    #pprint.pprint(complete_vocab)
    

parse_master_list()


    

