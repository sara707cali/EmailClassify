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
from copy import deepcopy


complete_vocab = {}
init_to_zero_vocab = {}
masterlist_file = 'masterlist_stopwords_names_10count_lem.txt'
outfile = 'weka_masterlist_stopwords_names_10count_lem.txt'
output = []


## check if file exists
def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print "Error: The file '%s' does not exist." % filename
        return False

def classified_list():
    classified = {}
    f = open('cats.txt', 'r')
    for line in f:
        path_cat = line.split()
        label = path_cat[1]
        subpaths = path_cat[0].split('\\')
        file = subpaths[2]
        file = file.replace('.cats','.txt')
        classified[file] = label
    f.close()    
    return classified
    
def parse_master_list():
    f = open(masterlist_file, 'r')
    for line in f:
        word_count = line.split(',')
        complete_vocab[word_count[0]] = word_count[1]
        init_to_zero_vocab[word_count[0]] = 0
    f.close()    
    #pprint.pprint(complete_vocab)
    
def single_master_list(data):
    my_vocab = deepcopy(init_to_zero_vocab)
    data = data.lower()
    data = re.sub("\S+@\S", " EMAILREPLACED ", data)
    data = re.sub("\d+", " NUMBERREPLACED ", data)
    data = re.sub("\s?http:s?\/\/\w{0,3}\.\w+\.\w{0,3}\S?|w{0,3}\.\w+\.\w{0,3}\S?", " URLREPLACED ", data)
    for punct in string.punctuation:
        data = data.replace(punct," ")
    format_data = data.split()
    no_stop_words = []
    l = WordNetLemmatizer()
    for word in format_data:
        if word not in stopwords.words('english'):
            no_stop_words.append(l.lemmatize(word))
            
    for element in no_stop_words:
        if(element in my_vocab):
            my_vocab[element] += 1

    return my_vocab


def get_email_body(filename):
    if (not file_exists(filename)):
        pass
        
    f = open(filename, 'r')
    body_of_email = False   
    forward_info = False
    body_regex = r'X-FileName:'
    forward_regex = r'-------- Forwarded'
    endHeader_regex = r'Subject:'
    
    body_data = ""  
   
    for line in f: 
        ## set flag for start of forward header data
        if re.search(forward_regex, line) != None:
            forward_info = True  

        ## set 'body_of_email' true after header section
        if not body_of_email:
            if re.search(body_regex, line) != None:
                body_of_email = True  
                
        ## set flag for end of forward header data
        elif forward_info:
            if re.search(endHeader_regex, line) != None:
                forward_info = False            
                
        ## only copy body of email
        elif body_of_email and not forward_info:
            body_data += line
            
    f.close()
    return body_data

all_files = []    

for dirname, dirnames, filenames in os.walk('.'):

    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')    
    
    # print path to all filenames.
    for filename in filenames:
        if ('.py' not in filename) and ('cats' not in filename) and ('masterlist' not in filename):
            all_files.append(os.path.join(dirname, filename))
            #print os.path.join(dirname, filename)    

count = 1    
errors = []        

email_tags = classified_list()
#pprint.pprint(email_tags)
parse_master_list()
# print "all----------------"
# pprint.pprint(all_files)
# print "----------------"

for file in all_files:  
    #print file
    path = file.split('\\')
    #print path
    txt_fname = path[2]
    literal = r'/'
    fix_path_file = file.replace('\\', literal)
    data = get_email_body(file)
    #try:
        
    this_master_list = single_master_list(data)
        
    #pprint.pprint(this_master_list)
    for word in sorted(this_master_list.keys()):
    #print word
        #output[txt_fname] = []
        output.append(str(this_master_list[word]))
    output.append(email_tags[txt_fname]+'\n')
        

    #except Exception as error:
        #errors.append(file+error)
    count += 1
    print count
#print "errors--------------"    
#pprint.pprint(errors)

    
output_str = ",".join(output) 
output_str = output_str.replace("\n,", "\n")
f = open(outfile, 'w')
f.write(output_str)
f.close()







    
# print str(len(complete_vocab))+"\n"
# print str(len(complete_bigrams))+"\n"
# f = open(masterlist_file, 'w')
# for word in sorted(complete_vocab.keys()):
    # ml_output = word+","+str(complete_vocab[word])
    # f.write(ml_output)
    # f.write('\n')
# f.close()




    

