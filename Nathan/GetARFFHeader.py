'''
Created on Apr 14, 2013

@author: ongnathan
'''

from os import listdir

MASTER_LIST_FILE = 'masterlist_names_10count_lem.txt'
ARFF_FILE = 'header_names_10count_lem.arff'
NUMERIC = True
masterList = []

def inputMasterList(masterListFileName):
    global masterList
    filename = MASTER_LIST_FILE if masterListFileName == None else masterListFileName
    masterFile = open(filename, 'r')
    for line in masterFile.readlines():
        word = line.split(',')[0]
        if word not in masterList:
            masterList.append(word)
    masterList = sorted(masterList)
    masterFile.close()

def makeARFFHeader(masterListFileName, arffOutputFileName, isNumeric):
    inputMasterList(masterListFileName)
    filename = ARFF_FILE if arffOutputFileName == None else arffOutputFileName
    arffFile = open(filename, 'w')
    arffFile.write('@RELATION emailClassification\n\n')
    for word in masterList:
        arffFile.write('@ATTRIBUTE ' + word + (' NUMERIC' if isNumeric else ' {y,n}') + '\n')
    arffFile.write('@ATTRIBUTE CLASS_LABEL {business, personal}\n\n@DATA\n')
    arffFile.flush()
    arffFile.close()
    
def makeAllMasterLists():
    for filename in listdir("."):
        if "masterlist" in filename:
            makeARFFHeader(filename, filename[:-3]+"arff", ("count" in filename))

if __name__ == "__main__":
    makeAllMasterLists()
