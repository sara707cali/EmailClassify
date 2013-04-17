'''
Created on Mar 20, 2013

@author: ongnathan
'''

import os

emailAddresses = {}
ENRON_WITH_CAT = 'enron_with_categories'
EMAIL_LIST_FILE = 'email from list.txt'

def getAllEmailAddresses():
    for dirpath, dirnames, filenames in os.walk(ENRON_WITH_CAT): #first and third elements only
        for filename in filenames:
            if '.txt' in filename:
                findAndAddEmailAddress(os.path.join(dirpath, filename))

def findAndAddEmailAddress(filename):
    addressesInEmail = []   #Only want to add the email address once per address
    email = open(filename, 'r')
    for line in email.readlines():
        if 'X-' in line:
            break;
        elif 'Subject' in line:
            continue
        elif 'From:' in line:
            addressLine = line[5:]
            for address in splitAddresses(addressLine):
                addAddressToList(addressesInEmail, address)
        elif 'Bcc:' in line:    #Must be first.  If not, "Cc" catches first due to case insensitivity
            addressLine = line[4:] #remove "Bcc:"
            for address in splitAddresses(addressLine):
                addAddressToList(addressesInEmail, address)
        elif 'To:' or 'Cc:' in line:
            addressLine = line[3:] #remove 'To:' or 'Cc:'
            for address in splitAddresses(addressLine):
                addAddressToList(addressesInEmail, address)
        elif line.startsWith('\t'):  #Still has addresses to count
            addressLine = line
            for address in splitAddresses(addressLine):
                addAddressToList(addressesInEmail, address)
        
    for address in addressesInEmail:
        if address not in emailAddresses:
            emailAddresses[address] = 1
        else:
            emailAddresses[address] += 1
    
    email.close()

#line is a string
def splitAddresses(line):
    return line.split(', ')

#addressList is a list
def addAddressToList(addressList, address):
    address = trim(address)
    if ('@enron.com' in address) and not (address in addressList):
        addressList.append(address)
        
def trim(string):
    if string.startswith(' ') or string.startswith('\t') or string.startswith('\n'):
        string = string[1:]
    if string.endswith(' ') or string.endswith('\t') or string.endswith('\n'):
        string = string[:-1]
    if '<' in string:
        string = string[string.index('<')+1:string.index('>')]
    return string
    
def writeEmailAddresses():
    emailListFile = open(EMAIL_LIST_FILE, 'w')
#     for address in sorted(emailAddresses):
#         emailListFile.write(address + ' ' + str(emailAddresses[address]) + '\n')
    numbersEmailList = {}
    for address in emailAddresses:
        if emailAddresses[address] not in numbersEmailList:
            numbersEmailList[emailAddresses[address]] = [address]
        else:
            numbersEmailList[emailAddresses[address]].append(address)
    
    numbers = sorted(numbersEmailList)
    numbers.reverse()
    for number in numbers:
        for address in sorted(numbersEmailList[number]):
            emailListFile.write(str(number) + ' ' + address + '\n')
            
    emailListFile.flush()
    emailListFile.close()

def main():
    getAllEmailAddresses()
    writeEmailAddresses()

if __name__ == "__main__":
    main()
