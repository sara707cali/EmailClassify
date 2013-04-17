'''
Created on Mar 31, 2013

@author: ongnathan
'''

import os

emailToCat = {}
ENRON_WITH_CAT = 'enron_with_categories'
CATEGORY_LIST_FILE = 'categories from list.txt'

def classify(line):
    categories = line.split(',')
    if not categories[0] == '1':
        return 'error'
    return {
         '1' : 'business',
         '2' : 'personal',
         '3' : 'personal',
         '4' : 'business',
         '5' : 'business',
         '6' : 'business',
         '7' : 'business', #empty = business
         '8' : 'business' 
    }.get(categories[1], 'error')
    
def setClassification(filename):
    email = open(filename, 'r')
    classification = classify(email.readline())
    emailToCat[filename] = classification
    
    classLabelFile = open(filename.split('.')[0] + '.classlabel', 'w')
    classLabelFile.write(classification)
    classLabelFile.flush()
    classLabelFile.close()
    

def getAllCategories():
    for dirpath, dirnames, filenames in os.walk(ENRON_WITH_CAT): #first and third elements only
        for filename in filenames:
            if '.cat' in filename:
                setClassification(os.path.join(dirpath, filename))

def export():
    classFile = open(CATEGORY_LIST_FILE, 'w')
    emailList = sorted(emailToCat)
    for emailName in emailList:
        classFile.write(emailName + ' ' + emailToCat[emailName] + '\n')
    classFile.flush()
    classFile.close()

if __name__ == '__main__':
    getAllCategories()
    export()
