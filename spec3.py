# coding: utf-8

def read_title():
    with open('title.txt', "r") as f:
        for line in f:
            print line,



if __name__ == "__main__":
    read_title()
