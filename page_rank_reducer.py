#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin
import math
import random

def read_mapper(data, separator):

    graph = {}
    pagerank_list = {}

    for line in data:
        data_list = line.rstrip().split(separator)
        if data_list[0] == 'r':
            pagerank_list[data_list[1]] = {'curr_pagerank': float(data_list[2]), 'new_pagerank': 0.0}
        elif data_list[0] == 'a':
            if data_list[1] in graph.keys():
                graph[data_list[1]].append(data_list[2])
            else:
                graph[data_list[1]] = [data_list[2]]
    
    return graph, pagerank_list

def main():
    separator = '\t'
    max_iterations = 100
    
    
    for _ in range(max_iterations):
        graph, pagerank_list = read_mapper(stdin,separator)
        for node in graph:
            neighbourds = graph[node]
            for neighbourd in neighbourds:
                try:
                    pagerank_list[neighbourd]['curr_pagerank'] += pagerank_list[node]['new_pagerank']    
                except:
                    pass
            
        for paper_id in pagerank_list:
            try:
                w = pagerank_list[paper_id]['curr_pagerank'] / float(len(graph[paper_id]))
            except:
                w = pagerank_list[paper_id]['curr_pagerank']
                
            print (paper_id+separator+str(w))
            

if __name__ == '__main__':
    main()
