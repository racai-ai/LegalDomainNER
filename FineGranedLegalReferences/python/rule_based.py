import numpy as np
from collections import defaultdict
from arguments import getArguments

def levenstein_distance(string1,string2):
    a=len(string1)
    b=len(string2)
    matrix=np.zeros((a+1,b+1))
    for i in range(0,a):
        for j in range(0,b):
            if string1[i] == string2[j]:
                matrix[i+1][j+1]=matrix[i][j]+1
            if string1[i] != string2[j]:
                matrix[i+1][j+1]=max(matrix[i][j+1],matrix[i+1][j])
    return 2*matrix[a][b]/(a+b)

class Graph:
    def __init__(self, V):
        self.graph=defaultdict(list)
        self.vertices=V
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def TopologicalSortV(self,vertex,visited,stack):
        visited[vertex]=True
        for adjacent in self.graph[vertex]:
            if visited[adjacent] == False:
                self.TopologicalSortV(adjacent,visited,stack)
        stack.append(vertex)
    def TopologicalSort(self):
        visited=[False]*(self.vertices+1)
        stack=[]
        for vertex in range(0,self.vertices):
            if visited[vertex] == False:
                self.TopologicalSortV(vertex,visited,stack)
        return stack  

def load_resources(r1, r2):
    global rank_top,position,types

    # citire cuvinte cheie
    f=open(r1,"r",encoding="utf-8")
    index=0
    types=[]
    en_dictionary={}
    position={}
    for x in f:
        sentence=x.split()
        types.append(sentence[0].lower())
        en_dictionary[sentence[0].lower()]=sentence[1]
        position[sentence[0].lower()]=index
        index=index+1

    #citire relatii(muchii) graf
    graph=Graph(index)
    g=open(r2,"r",encoding="utf-8")
    for line in g:
        sentence=line.split()
        sentence[0]=sentence[0].lower()
        sentence[1]=sentence[1].lower()
        graph.addEdge(position[sentence[0]],position[sentence[1]])
    rank=graph.TopologicalSort()
    rank_top={}
    for i in range(0,index):
        rank_top[rank[i]]=i

def choose_type(string):
    global rank_top
    sentence=string.split()
    type_of_annotation=""
    val_max=-1
    for word in sentence:
        if(rank_top[position[word.lower()]] > val_max):
            val_max=rank_top[position[word.lower()]]
            type_of_annotation=word.lower()
    return type_of_annotation

def answerconllup(path):
    global types

    const=0.82
    lemma={}
    list_words=[]
    f=open(path,"r",encoding="utf-8")
    for line in f:
        if line[0] == '#':
            continue
        if len(line) == 0:
            continue
        words=line.split()
        lemma[words[1].lower()]=words[2].lower()
        list_words.append(words[1].lower())
    new_list=[]
    for word in list_words:
           new_word=lemma[word]
           for new_word in types:
                if levenstein_distance(new_word,word) > const:
                    new_list.append(new_word)
    sentence=' '.join(new_list)
    return choose_type(sentence)

args=getArguments()
load_resources(args.keywords,args.rules)
ret=answerconllup(args.conllup)
print(ret)

