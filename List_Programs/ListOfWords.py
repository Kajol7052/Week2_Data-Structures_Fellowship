# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 19:13:54
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 10:05:54
# @Title: Program to find the list of words that are longer than n from a given list of words

class WordList:
    def __init__(self,words,n):
        self.words = words
        self.n = n
        
    def is_longer(self):
        long_words = []
        for word in self.words:
            if len(word) > self.n:
                long_words.append(word)
        return long_words


my_list = ['bat', 'fat', 'apple', 'pineapple', 'bags', 'chair', 'apartment']
wordList = WordList(my_list,3)
print(wordList.is_longer())