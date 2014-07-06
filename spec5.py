# coding: utf-8

import sys

class Title(object):
    def __init__(self):
        self.titles = {}
        self.number = 1

    def register(self):
        with open("title.txt") as f:
            for line in f:
                self.titles[self.number] = line.rstrip('\n')
                self.number += 1

    def cat(self):
        for key,value in self.titles.items():
            print "%d: %s" % (key, value)


    def search(self):
        argv = sys.argv
        print "%s" % (self.titles[int(argv[1])])



if __name__ == "__main__":
    title = Title()
    title.register()
    #title.cat()
    title.search()








