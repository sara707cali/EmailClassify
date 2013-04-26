'''
Created on Apr 17, 2013

@author: ongnathan
'''

import pprint

weightToWord = {}
SVM_WEIGHT_FILE = "svmWeights.txt"
SVM_SORTED_FILE = "svmSorted.txt"
SVM_PPRINT_FILE = "svmPPRINT.py"

def getFromFile(filename):
    svmWeightFile = open(filename, 'r')
    for line in svmWeightFile.readlines():
#         print line[9:15]
        weight = abs(float(line[9:15]))
        word = line[31:-1]
        if weight not in weightToWord:
            weightToWord[weight] = [word]
        else:
            weightToWord[weight].append(word)
    for key in weightToWord.keys():
        weightToWord[key] = sorted(weightToWord[key])
    svmWeightFile.flush()
    svmWeightFile.close()

def storeToFile(printFilename, pprintFilename):
    svmSortedFile = open(printFilename, 'w')
    svmPPrintFile = open(pprintFilename, 'w')
    for weight in sorted(weightToWord.keys()):
        svmSortedFile.write(str(weight) + "," + str(weightToWord[weight]) + '\n');
    pprint.pprint(weightToWord, svmPPrintFile)
#     print(weightToWord, svmSortedFile)
    svmSortedFile.flush()
    svmPPrintFile.flush()
    svmSortedFile.close()
    svmPPrintFile.close()

def main():
    getFromFile(SVM_WEIGHT_FILE)
    storeToFile(SVM_SORTED_FILE, SVM_PPRINT_FILE)

if __name__ == "__main__":
    main()