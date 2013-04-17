'''
Created on Apr 14, 2013

@author: ongnathan
'''

MASTER_LIST_FILE = 'masterlist.txt'
ARFF_FILE = 'emailClassification.arff'
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

def makeARFFHeader(masterListFileName, arffOutputFileName):
    inputMasterList(masterListFileName)
    filename = ARFF_FILE if arffOutputFileName == None else arffOutputFileName
    arffFile = open(filename, 'w')
    arffFile.write('@RELATION emailClassification\n\n')
    for word in masterList:
        arffFile.write('@ATTRIBUTE ' + word + (' NUMERIC' if NUMERIC else ' {y,n}') + '\n')
    arffFile.write('@ATTRIBUTE class {business, personal}\n')
    arffFile.flush()
    arffFile.close()

if __name__ == "__main__":
    makeARFFHeader(None, None)
