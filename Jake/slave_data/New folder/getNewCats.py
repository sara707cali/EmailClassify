
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


all_files = []
bus1 = []
bus2 = []
per1 = []
per2 = []
group1 = {}
group2 = {}
correct = {}
group1['b'] = {}
group1['p'] = {}
group2['b'] = {}
group2['p'] = {}
correct['b'] = {}
correct['p'] = {}

    
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
            all_files.append(os.path.join(dirname, filename))
            #print os.path.join(dirname, filename)  

for file in all_files:    
    if 'business1' in file:
        bus1.append(file)
    elif 'business2' in file:
        bus1.append(file)
    elif 'business3' in file:
        bus2.append(file)
    elif 'business4' in file:
        bus2.append(file)
    elif 'personal1' in file:
        per1.append(file)
    elif 'personal2' in file:
        per1.append(file)        
    elif 'personal3' in file:
        per2.append(file)  
    elif 'personal4' in file:
        per2.append(file)            
            
pprint.pprint(bus1)            
pprint.pprint(per2)            
            
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

    



    

