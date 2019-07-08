import csv
from collections import Counter


def read_csva(file_name):
    with open(file_name, encoding = 'gbk',mode='r',errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        author =[]
        tag = []
        title = []
        for row in csv_reader:
            #author.append(row[0])
            tag += (row[1].split(','))
            #tag.append(row[1].split(','))
            #title.append(row[2])
    return tag


tag = read_csva('items.csv')
Counter = Counter(tag)
most_occur_5 = Counter.most_common(10)
print(most_occur_5)


