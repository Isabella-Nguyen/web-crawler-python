#COURSE PROJECT WEB CRAWLER

import webdev
import os
import matmult
import math

def getTitle(contents, dir_name): #extract the title
    start_title=contents.find("<title>")+len("<title>") 
    end_title=contents.find("</title>")
    title=contents[start_title:end_title]
    
    if not os.path.isdir(dir_name): #Check if the directory exists.
        os.makedirs(dir_name)
    
    file_path=os.path.join(dir_name,"title.txt")
    file=open(file_path,"w")
    file.write(title)
    file.close()
    
def getPara(contents): #Extract the paragraph into a list
    num=contents.count("<p>") #Check how many <p> tags there are just in case there is more than one
    startPara=0
    endPara=0
    para=[]
    
    for i in range (num):
        startPara=contents.find("<p>", endPara)+len("<p>")+len("\n") #This assumes that there will be a "\n" before and after every paragraph.
        endPara=contents.find("</p>", startPara)-len("\n")
        words=contents[startPara:endPara].lower().split("\n") #make everything lowercase as well
        para+=words #add the words to the paragraph
        
    return para

def getAbsURL(seed):
    endIndex=0
    for i in range(len(seed)-1,0,-1):
        if seed[i]=="/":
            endIndex=i
            break
    absoluteLink=seed[:endIndex] #Get the absolute link so we can add it to the relative URLs
    return absoluteLink

def getRelativeName(seed, absURL): #This is for the seed at the start so that dirNameDic is initialized
    start=len(absURL)+1
    end=seed.find(".html")
    return seed[start:end]

def getLinks(contents, queue, queueDic, dirNameDic, absoluteLink): #Get the links and add it to the queue if it hasn't been read or if it's not already in the queue
    links=[]
    startLink=contents.find("href=\".")+len("href=\".")
    start=0
    while start!=-1:
        endLink=contents.find("\"",startLink)
        links.append(contents[startLink:endLink]) #list of all links found in this URL
        start=contents.find("href=\".",endLink)
        startLink=start+len("href=\".")
    
    allLinks={}
    
    for index in range(len(links)):
        relativeURL=links[index]
        absLink=absoluteLink+relativeURL #Add the absolute URL to the relative URL
        
        endhtml=relativeURL.find(".html")
        dir_name="url"+relativeURL[1:endhtml] #start from 1 because there is a '/' at the start
        
        allLinks[absLink]= dir_name #keep track of all outgoing links
        
        if (absLink not in queueDic) and not os.path.isdir(dir_name):
            queue.append(absLink) #Add to queue
            queueDic[absLink]=1
            dirNameDic[absLink]=dir_name #keep track of what directory name corresponds with what link
            os.makedirs(dir_name) #Make a directory for each URL
    
    return allLinks

def dequeue(queue, queueDic):
    if len(queue)==0:
        return None
    pop=queue.pop(0)
    del queueDic[pop]
    return pop

def getFreq(dic, words): 
    for word in words:
        if word not in dic: #Count all the frequencies
            dic[word]=0
        dic[word]+=1

def saveWordInfo(dic, dir_name):
    if not os.path.isdir(dir_name): #Check if the directory exists.
        os.makedirs(dir_name)
    
    for word in dic:
        file_path = os.path.join(dir_name, word+".txt")
        fileout = open(file_path, "w") #create a file with the name of the word
        fileout.write(str(dic[word]))
        fileout.close()

def getOutgoing(links, dir_name):
    if not os.path.isdir(dir_name): #Check if the directory exists.
        os.makedirs(dir_name)
    
    file_path=os.path.join(dir_name,"outgoing.txt")
    file=open(file_path,"a")
    for link in links:
        file.write(link+"\n")
    file.close()

def outgoingDic(URL, links, dic):
    outDic={}
    for link in links:
        outDic[link]=1
    dic[URL]=outDic #keep track of all the outgoing links for each page for the page rank algorithm
    return dic

def getIngoing(links, ingoingURL):
    for link in links:
        dir_name=links[link]
        if not os.path.isdir(dir_name): #Make a directory for the outgoing link if it has not created yet
            os.makedirs(dir_name)
        
        file_path=os.path.join(dir_name,"ingoing.txt") #Open/create a file for ingoing links
        file=open(file_path,"a")
        file.write(ingoingURL+"\n") #Add the ingoing link into the outgoing directory
    file.close()

def getURLNums(dirNames):
    count=0
    URLNum={}
    for url in dirNames:
        URLNum[url]=count #Make a dictionary that gives each URL a corresponding number to use in the PageRank algorithm
        count+=1
    return URLNum

def getPageRankVector(N, outList, URLNum):
    adjMatrix=[]
    alpha=0.1
    threshold=1
    tnew=[[]]
    index=0
    
    for page in URLNum:
        adjMatrix.append([]) #add an empty row for page
        tnew[0].append(1/N) #Initialize the first vector for later
    
    for page in URLNum: #Iterate through each page and extract the outgoing links
        outgoing=outList[page]
        numOutgoing=len(outgoing)
        if numOutgoing==0: #if there are no outgoing links, there will be no 1's
            for link in URLNum:
                adjMatrix[URLNum[page]].append(1/N) #instead of adding 0's and then replacing it, just add 1/N in the first place.
            continue
        for link in URLNum: #For each link, check if it's an outgoing link. If it's not, add 0, otherwise add 1.
            if link in outgoing:
                adjMatrix[URLNum[page]].append(1/numOutgoing) #Divide each 1 by number of 1s in the row. This is determined by number of outgoing links
            else:
                adjMatrix[URLNum[page]].append(0)
    
    adjMatrix=matmult.mult_scalar(adjMatrix,1-alpha)
    
    for row in range(len(adjMatrix)):
        for num in range(len(adjMatrix[row])):
            adjMatrix[row][num]+=alpha/N
    
    while threshold>0.0001:
        tprev=tnew
        tnew=matmult.mult_matrix(tprev,adjMatrix) #multiply the matrices
        threshold=matmult.euclidean_dist(tnew,tprev) #calculate the threshold
    
    return tnew

def savePageRank(pageRank, dir_name):
    file_path=os.path.join(dir_name,"pagerank.txt") #Open/create a file for the page rank
    file=open(file_path,"w")
    file.write(str(pageRank)) #Add the page rank into the url's directory
    file.close()

def getIdf(docNum, totalNumDoc):
    idf={}
    for word in docNum:
        numDocWord=docNum[word]
        idf[word]=math.log(totalNumDoc/(1+numDocWord),2)
    return idf

def getTf(URL, freq, totalWords, dir_name):
    tf={}
    for word in freq:
        occurences=freq[word]
        tf[word]=occurences/totalWords
    return tf

def tfDic(link, tf, dic): #keep track of all the tf's to calculate tf-idf at the end
    dic[link]=tf
    return dic

def getTfIdf(tf, idf, url, docNum, dir_name):
    for word in docNum:
        if word not in tf[url]: #check if the word is present in the url
            continue
        tfidf=math.log(1+tf[url][word],2)*idf[word] #calculate tf-idf
        file_path=os.path.join(dir_name,word+".txt") #save tf-idf
        file=open(file_path,"w")
        file.write(str(tfidf))
        file.close()

def storeDic(dic):
    file=open("dirNames.txt","w")
    file.write(str(dic))
    file.close()

def crawl(seed):
    directory = os.listdir() #Delete the directories from the past crawl
    for direct in directory:
        if direct.startswith("url") or direct=="idf":
            files = os.listdir(direct) #Delete the files in the directories
            for file in files:
                if file=="tfidf":
                    path=os.path.join(direct,file)
                    tfidfFiles = os.listdir(path) #Delete the files in the directories
                    for tfidfFile in tfidfFiles: #Delete the files in the tfidf file before deleting the directory tdidf
                        os.remove(os.path.join(path, tfidfFile))
                    os.rmdir(path)
                else:
                    os.remove(os.path.join(direct, file))
            os.rmdir(direct)
    
    absURL=getAbsURL(seed)
    dir_name_seed="url"+getRelativeName(seed, absURL) #The directory name is "url" plus the relative URL without the .html. This is incase there are duplicate titles, but there shouldn't be duplicate URLS.
    
    queue=[seed]
    queueDic={seed:1}
    count=0
    docNum={}
    freq={}
    dirNameDic={seed:dir_name_seed}
    allOutgoing={}
    tfDict={}
    
    while len(queue)>0:
        count+=1 #count total pages
        link=dequeue(queue, queueDic)
        contents = webdev.readurl(link)
        words=getPara(contents)
        outgoing=getLinks(contents, queue, queueDic, dirNameDic, absURL)
        dir_name=dirNameDic[link]
        
        getFreq(freq, words) #frequency of words in the page
        getFreq(docNum,freq) #amount of documents a word appears in
        
        getTitle(contents,dir_name)
        
        getOutgoing(outgoing,dir_name)
        outgoingDic(link, outgoing, allOutgoing) #save all the outgoing links in a dictionary to use for the page rank algorithm
        
        getIngoing(outgoing, link)
        
        tf=getTf(link, freq, len(words), dir_name)
        saveWordInfo(tf,dir_name) #save the tf values into files
        tfDict=tfDic(link, tf, tfDict) #save all the tf values into a dictionary to calculate tf-idf values later
        
        freq={} #Reset the frequency for each link
    
    URLNum=getURLNums(dirNameDic)
    
    idf=getIdf(docNum, count)
    saveWordInfo(idf, "idf") #save idf values into files
    
    pageRankVect=getPageRankVector(count, allOutgoing, URLNum)
    for URL in dirNameDic:
        pageRank=pageRankVect[0][URLNum[URL]] #Extract all the page ranks for each url
        savePageRank(pageRank,dirNameDic[URL]) #Save the page ranks
        
        dir_path=os.path.join(dirNameDic[URL],"tfidf") #make a directory in directory
        os.makedirs(dir_path)
        getTfIdf(tfDict, idf, URL, docNum, dir_path) #get and save tf-idf values
    
    storeDic(dirNameDic)
    
    return count