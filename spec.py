# coding: utf-8

import sys

class Title(object):
    def __init__(self):
        self.titles = {}
        self.number = 1
        self.argv = sys.argv
        self.argc = len(self.argv)


    def print_omurice(self):
        print "オムライス"

    def register(self):
        filename = self.argv[1]
        with open(filename) as f:
            for line in f:
                self.titles[self.number] = line.rstrip('\n')
                self.number += 1

    def cat(self):
        for key,value in self.titles.items():
            print "%d: %s" % (key, value)


    def search(self):
        search_number = self.argv[2]
        print "%s" % (self.titles[int(search_number)])

    def print_user(self):
        user = argv[3]
        print "%s" % user
        


if __name__ == "__main__":
    title = Title()
    if(title.argc == 1):
        title.print_omurice()
        
    if(title.argc == 2):
        title.register()
        title.cat()

    if(title.argc == 3):
        title.register()
        title.search()





