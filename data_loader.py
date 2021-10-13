import json
import os
from pymongo import MongoClient

def upload_page_rank(mongo_collection):
    page_rank_descriptor = open('./data/rank_result.txt','r')
    page_rank_result = []
    for line in page_rank_descriptor:
        page_rank = line.split('\t')
        page_rank_result.append({
            'id': page_rank[0],
            'rank': float(page_rank[1].rstrip('\n'))
        })
    
    mongo_collection.insert_many(page_rank_result)


def upload_inverted_index(mongo_collection):
    inverted_index_descriptor = open('./data/index_result.txt','r')
    inverted_index_result = []
    for line in inverted_index_descriptor:
        inverted_index = line.split('\t')
        papers = inverted_index[1].rstrip('\n').split(',')
        inverted_index_result.append({
            'word': inverted_index[0],
            'papers': papers
        })
    
    mongo_collection.insert_many(inverted_index_result)


def upload_papers(mongo_collection):
    path = './data'

    files = os.listdir(path)
    articles = []
    for f in files:
        file_descriptor = open(f"{path}/{f}","r",encoding='utf-8')
        for line in file_descriptor:
            article = json.loads(line)
            if 'abstract' in article.keys() and 'references' in article.keys():
                id = article['id']
                title = article['title']
                articles.append({
                    'id': id,
                    'title': title
                })
    
    mongo_collection.insert_many(articles)


def main():
    client = MongoClient('kuusack.com', 27017)
    db = client['cloud_db']
    # papers = db['papers']
    # upload_papers(papers)
    # inv_index = db['indexs']
    # upload_inverted_index(inv_index)
    page_rank = db['ranks']
    upload_page_rank(page_rank)




if __name__ == '__main__':
    
    main()