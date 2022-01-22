#COURSE PROJECT SEARCH

import math
import searchdata
import os

def get_query_freq(query):
    freqQuery={}
    for word in query:
        if word not in freqQuery:
            freqQuery[word]=0
        freqQuery[word]+=1
    return freqQuery

def get_tf_query(query, word, totalWords):
    return query[word]/totalWords

def get_tf_idf_query(query,word, totalWords):
    return math.log(1+get_tf_query(query, word, totalWords),2)*searchdata.get_idf(word)

def get_euclidean_norm(vector, index):
    if index==len(vector):
        return 0
    elif index==0:
        return math.sqrt(float((vector[index]**2)+get_euclidean_norm(vector,index+1)))
    return (vector[index]**2)+get_euclidean_norm(vector,index+1)

def get_numerator(vectorA, vectorB, index):
    if index==len(vectorA):
        return 0
    return (vectorA[index]*vectorB[index])+get_numerator(vectorA,vectorB,index+1)

def get_cos_similarity(docVect,queryVect):
    numerator=get_numerator(docVect,queryVect,0)
    leftDenom=get_euclidean_norm(queryVect,0)
    rightDenom=get_euclidean_norm(docVect,0)
    
    if leftDenom==0 or rightDenom==0: #Avoid division by 0
        return 0
    
    return numerator/(leftDenom*rightDenom)

def quicksort(alist, low, high):
    if low<high:
        p=partition(alist, low, high)
        quicksort(alist, low, p)
        quicksort(alist, p+1, high)

def partition(alist, low, high):
    pivot=alist[low]
    ind1=low-1
    ind2=high+1
    
    while True:
        ind1+=1
        ind2-=1
        
        while alist[ind1]>pivot: #sort from highest to lowest not lowest to highest
            ind1+=1
        while alist[ind2]<pivot:
            ind2-=1
        if ind1>=ind2:
            return ind2
            
        temp=alist[ind1]
        alist[ind1]=alist[ind2]
        alist[ind2]=temp

def search(phrase, boost):
    vectors=[]
    queryVect=[]
    cosSimList=[]
    cosSimURL={}
    top10=[]
    #Get the words in the phrase and put them in a list
    query=phrase.lower().split() #convert to lowercase and split the words
    totalWords=len(query)
    queryFreq=get_query_freq(query) #get frequency of the words in the query
    #Get the tf-idfs for those words for all documents
    links=searchdata.getDirNames()
    index=0
    for url in links:
        vectors.append([])
        for word in queryFreq:
            vectors[index].append(searchdata.get_tf_idf(url,word))
        index+=1
    index=0
    #Get tf-idfs for those words in the query
    for word in queryFreq:
        queryVect.append(get_tf_idf_query(queryFreq, word, totalWords))
    #Find cosine similarity
    index=0
    for url in links:
        cosSim=get_cos_similarity(vectors[index],queryVect)
        cosSimList.append(cosSim)
        index+=1
    #Update the list if boost is true
    index=0
    if boost:
        for url in links:
            pageRank=searchdata.get_page_rank(url)
            cosSimList[index]*=pageRank
            index+=1
    #Keep track of all the urls and their score (using lists as values in case of ties)
    index=0
    for url in links:
        score=cosSimList[index]
        if score not in cosSimURL:
            cosSimURL[score]=[]
        cosSimURL[score].append(url) 
        index+=1
    #Sort the scores
    quicksort(cosSimList,0,len(cosSimList)-1)
    #Get the top 10 scores and output the correct information
    for num in range(10):
        top10.append({})
        score=cosSimList[num]
        URL=cosSimURL[score].pop(0) #Take the first url out of the dictionary that corresponds with the correct score
        top10[num]["url"]=URL #add the url to the top 10 list of scores
        
        dir_name=links[URL]
        file_path=os.path.join(dir_name,"title.txt")
        file=open(file_path,"r")
        title=file.read()
        top10[num]["title"]=title #add the title to the list
        file.close()
        
        top10[num]["score"]=score #add the score to the list
    
    return top10