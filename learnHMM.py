import POS_Tagger as pt
import random
import nltk
from nltk import *
import numpy
from  numpy import *
from numpy.linalg import svd


def untagger(vector):
    untagged = []
    for i in vector:
        untagged.append(i[0])
    return untagged

def calcProb(fdist):
    keys = fdist.keys()
    prob = []
    for i in range(fdist.B()):
        prob.append(fdist.freq(keys[i]))
    return numpy.array(prob)

print 'learnHMM'
words = pt.tagged_Brown()[:20]
unwords = untagger(words)
tagSet = pt.tagCount(words)

n = len(words) # number of observations
m = len(tagSet) # number of states

r = random.randint(0,m-2)
x1,x2,x3 = words[r],words[r+1],words[r+2]

P1 = array([[0,0],[0,0]])
P1.resize(n,1)




