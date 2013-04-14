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
# fname_in = "testdata\\"
# my_range = 898
fname_out = "outdata"
complete_vocab = {}
complete_bigrams = {}
masterlist_file = 'masterlist.txt'
#bigrams_file = 'bigrams.txt'

## check if file exists
def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print "Error: The file '%s' does not exist." % filename
        return False


def master_list(data):
	previous_word = ""
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
		if(element not in complete_vocab):
			complete_vocab[element] = 1
			##print element
		else:
			complete_vocab[element] = complete_vocab[element] + 1
		#if ((previous_word == "EMAILREPLACED")or(previous_word == "NUMBERREPLACED")):
		#	previous_word = element
		#	continue
		#elif (previous_word == ""):
		#	previous_word = element
		#	continue
		#elif ((element == "EMAILREPLACED")or(element == "NUMBERREPLACED")):
		#	previous_word = element
		#	continue
		#else:
		#	bigram = previous_word+" "+element
		#	bigram = l.lemmatize(bigram)
		#	if(bigram not in complete_bigrams):
		#		complete_bigrams[bigram] = 1
		#	else:
		#		complete_bigrams[bigram] = complete_bigrams[bigram] + 1
	#
## return str w/ body of email for a file

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
        if ('.py' not in filename) and ('.cats' not in filename) and ('masterlist' not in filename):
            all_files.append(os.path.join(dirname, filename))
            #print os.path.join(dirname, filename)    

count = 1    
errors = []        
for file in all_files:
    try:
        data = get_email_body(file)
        master_list(data)
        f_out = open(fname_out + str(count) + '.txt', 'w')
        f_out.write('\n\nEmail Message:\n\n' + data + '\n\nFileName' + file)
        f_out.close()
    except Exception as error:
        errors.append(file)
    count += 1
    print count

print str(len(complete_vocab))+"\n"
print str(len(complete_bigrams))+"\n"
f = open(masterlist_file, 'w')
for word in sorted(complete_vocab.keys()):
	ml_output = word+","+str(complete_vocab[word])
	f.write(ml_output)
	f.write('\n')
f.close()




    

