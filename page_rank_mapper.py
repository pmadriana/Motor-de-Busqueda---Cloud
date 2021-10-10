#!/usr/bin/env python3

from sys import stdin
import json
import random

graph = {}

def process_data(input, graph):
    
    for line in input:
        article = json.loads(line)
        if 'abstract' in article.keys() and 'references' in article.keys():
            curr_pagerank_value = random.uniform(0,1)
            yield (article['id'], curr_pagerank_value)
            references_articles = list(article['references'])
            
            graph[article['id']] = references_articles


def main():
    separator = '\t'
    
    data = process_data(stdin,graph)

    for article_id, pagerank in data:
        print('r'+separator+article_id+separator+str(pagerank))
    
    # print(graph)
    for node in graph:
        for relation in graph[node]:
            print('a'+separator+node+separator+relation)
    
if __name__ == '__main__':
    main()

