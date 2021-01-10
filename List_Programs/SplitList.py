# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-08 13:42:34
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-09 00:04:04
# @Title: Program to split a list based on first character of word

class ListSplitter:
    def __init__(self):
        self.word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
    def split_list(self):
        self.word_list.sort()
        print(self.word_list[0][0])
        print(self.word_list[0])
        for i in range(1,len(self.word_list)):
            if self.word_list[i][0] == self.word_list[i-1][0]:
                print(self.word_list[i])
            else:
                print("-------------")
                print(self.word_list[i][0])
                print(self.word_list[i])
listSplitter = ListSplitter()
listSplitter.split_list()