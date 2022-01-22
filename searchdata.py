#COURSE PROJECT DATA REQUIRED FOR SEARCH

import os

dirNames={}

def getDirNames(): #Get the dictionary from the file that contains the directory names that correspond with each absolute URL
    file=open("dirNames.txt","r")
    data=file.read()
    file.close()
    global dirNames
    dirNames=eval(data)
    return dirNames

def initializeDirNames(): #I don't know which function will be called first, so I made this to initialize the dictionary once
    if dirNames=={}:
        getDirNames()

def getInfoList(URL, filename): #reuse code for outgoing and incoming links because they're doing almost the same thing
    dir_name=dirNames[URL]
    file_path=os.path.join(dir_name, filename)
    file=open(file_path,"r")
    data=file.read().split("\n")
    if data[-1]=="": #Sometimes there is an empty value at the end due to the splitting
        data.pop()
    file.close()
    return data

def get_outgoing_links(URL):
    initializeDirNames()
    if URL in dirNames:
        return getInfoList(URL, "outgoing.txt")
    return None

def get_incoming_links(URL):
    initializeDirNames()
    if URL in dirNames:
        return getInfoList(URL,"ingoing.txt")
    return None

def getInfoNum(dir_name, filename): #General function for reading a file in a directory and returning it
    file_path=os.path.join(dir_name, filename)
    if not os.path.isfile(file_path): #check if the file exists (this checks if the word is found in the URL)
        return 0
    file=open(file_path,"r")
    data=float(file.read())
    file.close()
    return data

def get_page_rank(URL):
    initializeDirNames()
    if URL not in dirNames:
        return -1
    
    dir_name=dirNames[URL]
    return getInfoNum(dir_name, "pagerank.txt")
    
def get_idf(word):
    return getInfoNum("idf", word+".txt")

def get_tf(URL, word):
    initializeDirNames()
    if URL not in dirNames: #check if the URL exists
        return 0
    
    dir_name=dirNames[URL]
    return getInfoNum(dir_name, word+".txt")

def get_tf_idf(URL, word):
    initializeDirNames()
    if URL not in dirNames:
        return 0
    dir_name=os.path.join(dirNames[URL],"tfidf")
    return getInfoNum(dir_name, word+".txt")