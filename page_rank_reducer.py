#!/usr/bin/python3
#coding: utf-8

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
    max_iterations = 10
    d = 0.85
    d_complement = 1 - d
    
    graph, pagerank_list = read_mapper(stdin,separator)
    for _ in range(max_iterations):
        
        for node in graph:
            neighbourds = graph[node]

            for neighbourd in neighbourds:
                if neighbourd in pagerank_list.keys() and node in graph.keys() and len(graph[node])>0:
                    pagerank_list[neighbourd]['new_pagerank'] += (pagerank_list[node]['curr_pagerank']/(len(graph[node])))
                else:
                    pagerank_list[neighbourd] = {'curr_pagerank': random.uniform(0,1), 'new_pagerank': 0.0}
            
        
        for paper_id in pagerank_list:
            if paper_id in graph.keys():
                pagerank_list[paper_id]['new_pagerank'] = d_complement + d*pagerank_list[paper_id]['new_pagerank']
            else:
                pagerank_list[paper_id] = {'curr_pagerank': random.uniform(0,1), 'new_pagerank': 0.0}
    
        for paper_id in pagerank_list:
            if pagerank_list[paper_id]['new_pagerank'] != 0.0:
                pagerank_list[paper_id]['curr_pagerank'] = pagerank_list[paper_id]['new_pagerank']
            
    
    for paper_id in pagerank_list:
        rank = math.floor(pagerank_list[paper_id]['curr_pagerank'] * 1000)/1000.0
        if rank > 1.000:
            rank = 1.000
        print(paper_id+separator+str(rank)) 

if __name__ == '__main__':
    main()
