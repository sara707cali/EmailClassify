#!/usr/local/bin/python

## first line allows you to double click the file and run as a script


import re 
import pprint 
import os

# fname_in = "testdata\\"
# my_range = 898
fname_out = "outdata\\"

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
    # print path to all subdirectories first.
    # for subdirname in dirnames:
        # print os.path.join(dirname, subdirname)         

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')    
    
    # print path to all filenames.
    for filename in filenames:
        if ('.py' not in filename) and ('.txt' not in filename):
            all_files.append(os.path.join(dirname, filename))
            #print os.path.join(dirname, filename)    

count = 1    
errors = []        
for file in all_files:
    try:
        data = get_email_body(file)    
        f_out = open(fname_out + str(count) + '.txt', 'w')
        f_out.write('\n\nEmail Message:\n\n' + data + '\n\nFileName' + file)
        f_out.close()
    except Exception as error:
        errors.append(file)
    count += 1

    
    
    
### old way     
    
## create a list of filenames ranging from 0 to myrange   
# files = [i for i in range(1,my_range)]
# errors = []
# for filenum in files:
    # try:
        # data = get_email_body(fname_in + str(filenum))    
        # f_out = open(fname_out + str(filenum) + '.txt', 'w')
        # f_out.write('\n\nEmail Message:\n\n' + data)
        # f_out.close()
    # except Exception as error:
        # pass
        
        # errors.append("couldnt open: " + str(filenum))
        # 'file_exists' funct will print out bad file names
        
#pprint.pprint(errors)


    

