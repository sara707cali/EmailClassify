import pprint

m_lists = [
'weka_masterlist_count_stop_lem.txt',
'weka_masterlist_count_stop_none.txt',
'weka_masterlist_count_nostop_lem.txt',
'weka_masterlist_count_nostop_none.txt'
]

def to_bool_str(file):
    f = open(file, 'r')
    file_content = ""
    for line in f:
        result = ""
        this_line = ""
        line_spilt = line.split(',')
        result = line_spilt.pop(len(line_spilt)-1)
        for number in line_spilt:
            bool_str = ""
            if (number == '0'):
                bool_str = 'n'
            else:
                bool_str = 'y'
            this_line += (bool_str + ',')
        this_line += result
        file_content += this_line
    f.close()  
    return file_content
    
for m_file in m_lists:
    this_list = to_bool_str(m_file)
    f_out =  f = open(m_file.replace("count","bool"), 'w')
    f_out.write(this_list)
    f.close()
    

