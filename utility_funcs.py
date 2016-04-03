import re
def find_col_idx(file_name, col_name):
    '''
    :return:
    '''
    indexes = []
    pat = re.compile(".*" + col_name + ".*", re.IGNORECASE)
    with open(file_name) as fd:
        header = fd.readline().strip().split(",")
        print(header[619])
        for idx , item in enumerate(header):
            if pat.search(item):
                indexes.append((idx, item))
    return indexes


print(find_col_idx('/Users/vikhyati/Desktop/OSHPD_TEST.csv' , "charlson"))

