#!/usr/bin/python
# -*- coding: utf-8 -*-


from sys import stdin
import re
import json
import importlib

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def contains_number(value):
    for character in value:
        if character.isdigit():
            return True
    return False

def process_data(input):
    for line in input:
        article = json.loads(line)
        if 'abstract' in article.keys() and 'references' in article.keys():
            title = article['title']
            title = re.sub(r'[^\w\s]', '',title).lower()
            title = title.split()
            title_set = set(title)
            title_list = list(title_set)
            title_stopwords_clean = []
            for word in title_list:
                if word not in stop_words and not contains_number(word):
                    title_stopwords_clean.append(word)

            yield (article['id'],title_stopwords_clean)

def main():
    separator = '\t'
    clean_data = process_data(stdin)
    for paper_id, list_of_words in clean_data:
        for word in list_of_words:
            print(word + separator + paper_id)

if __name__ == '__main__':
    main()
