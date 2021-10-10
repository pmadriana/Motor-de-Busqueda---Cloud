#!/usr/bin/python3
#coding: utf-8

from sys import stdin
from itertools import groupby
from operator import itemgetter

def read_mapper(data, separator):
    for line in data:
        data_list = line.rstrip().split(separator,1)
        yield data_list

def main():
    separator = '\t'
    mapper_data = read_mapper(stdin, separator)

    for word, word_paperId_list in groupby(mapper_data,itemgetter(0)):
        papers_id = []
        for tuple in word_paperId_list:
            if len(tuple) == 2:
                papers_id.append(tuple[1])
        
        papers_id_string = ''

        for id in papers_id:
            papers_id_string+= str(id)+','
        
        papers_id_string = papers_id_string.rstrip(',')
        print(word+separator+papers_id_string)

if __name__ == '__main__':
    main()
