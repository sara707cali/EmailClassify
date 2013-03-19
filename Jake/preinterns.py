#!/usr/local/bin/python

## first line allows you to double click the file and run as a script


import re 
## import regular expressions lib
## forget which of these libs come with python by default
## very easy to install new libs using pip command from cmd prompt, just google it
import pprint 
import os.path
## use import in similar manner to import another entire python file or functions
## see python_intro powerpoint


## on my comp have files in folder, at same level as this file, named 'testdata'
## inside folder has files, no extension ranging from 1 to 898
## 'fname_in' is path for testing data... '\' is escape character
fname_in = "testdata\\"
## prob is way to determine range automatically
my_range = 898
## append number to path above in loop below
## later easy to expand to allow for cmd line inputs

fname_out = "outdata\\"
## manually created empty folder to store output files

## check if file exists
def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print "Error: The file '%s' does not exist." % filename
        return False

## return str w/ body of email for a file
def get_email_body(filename):
    if (not file_exists(filename)):
        pass
        
    f = open(filename, 'r')
    body_of_email = False   
    body_regex = r'X-FileName:'
    
    ## body_data = []
    ## storing in an array(or list) would be faster since strings are immutable
    ## but its easier for now to append to a str
    body_data = ""  
   
    for line in f: 
        if not body_of_email:
            if re.search(body_regex, line) != None:
                body_of_email = True
        else:
            #body_data.append(line)  ##to store in array
            body_data += line
            
    f.close()
    return body_data

    
## create a list of filenames ranging from 0 to myrange   
files = [i for i in range(1,my_range)]
errors = []
for filenum in files:
    try:
        data = get_email_body(fname_in + str(filenum))    
        f_out = open(fname_out + str(filenum) + '.txt', 'w')
        f_out.write('\n\nEmail Message:\n\n' + data)
        f_out.close()
    except Exception as error:
        pass
        # errors.append("couldnt open: " + str(filenum))
        # 'file_exists' funct will print out bad file names
        
#pprint.pprint(errors)


    

