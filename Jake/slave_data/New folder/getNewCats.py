
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


all_files = {}
files_classified = {}
files_classified['bus'] = []
files_classified['pers'] = []
files_classified['unknown'] = []
    
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    # for subdirname in dirnames:
        # print os.path.join(dirname, subdirname)         

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')    
    
    for filename in filenames:
        if ('.py' not in filename) and ('.DS_Store' not in filename):
            #all_files.append(os.path.join(dirname, filename))
            if filename not in all_files:
                all_files[filename] = dirname
            else:
                temp_str = "," + dirname
                all_files[filename] += temp_str
            #print os.path.join(dirname, filename)  
            
            

for file, tags in all_files.iteritems():
    list = tags.split(',')
    if (len(list) > 1):
        if ('business' in list[0]) and ('business' in list[1]):
            files_classified['bus'].append(file) 
        elif ('personal' in list[0]) and ('personal' in list[1]):
            files_classified['pers'].append(file)     
        else:
            files_classified['unknown'].append(file)   
    else:
        files_classified['unknown'].append(file)  
           
pprint.pprint(files_classified)
print 'bus', len(files_classified['bus'])
print 'pers', len(files_classified['pers'])
print 'unknown', len(files_classified['unknown'])
           
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

    



    

