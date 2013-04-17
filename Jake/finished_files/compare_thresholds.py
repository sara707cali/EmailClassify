import operator
import pprint

masterlist_file = 'masterlist_Original.txt'
complete_vocab = {}

def parse_master_list():
    f = open(masterlist_file, 'r')
    for line in f:
        word_count = line.split(',')
        complete_vocab[word_count[0]] = int(word_count[1].replace("\n",""))
    f.close()  
    
parse_master_list()
sorted_list = sorted(complete_vocab.iteritems(), key=operator.itemgetter(1))

pprint.pprint(sorted_list)
