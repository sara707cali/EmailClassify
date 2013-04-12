
import re 
import pprint 
import os

fname_out = "outdata\\"

## check if file exists
def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print "Error: The file '%s' does not exist." % filename
        return False



bus1 = []
bus2 = []
per1 = []
per2 = []
# group1[b] = {}
# group1[p] = {}
# group2[b] = {}
# group2[p] = {}
# correct[b] = {}
# correct[p] = {}

    
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    # for subdirname in dirnames:
        # print os.path.join(dirname, subdirname)         

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')   
    else:
        print dirname 
    # elif 'business1' or 'business2' in dirnames:
        # bus1.append(filenames)
    # elif 'business3' or 'business4' in dirnames:
        # bus2.append(dirname)
    # elif 'personal1' or 'personal2' in dirnames:
        # per1.append(dirname)
    # elif 'personal3' or 'personal4' in dirnames:
        # per2.append(dirname)   
    
    # print path to all filenames.
    for filename in filenames:
        if ('.py' not in filename) and ('.DS_Store' not in filename):
            pass    
        
        
        
            #all_files.append(os.path.join(dirname, filename))
            #print os.path.join(dirname, filename)    

count = 1    
errors = []        
# for file in all_files:
    # try:
        # data = get_email_body(file)    
        # f_out = open(fname_out + str(count) + '.txt', 'w')
        # f_out.write('\n\nEmail Message:\n\n' + data + '\n\nFileName' + file)
        # f_out.close()
    # except Exception as error:
        # errors.append(file)
    # count += 1

    



    

