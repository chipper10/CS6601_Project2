import nltk
from nltk import *
from nltk.corpus import brown
import numpy
from numpy import *
import time


def findmaxtag(good, bad):
    curMax = 0
    curTag = ' '
    for tag in good:
        if(good[tag]-bad[tag] > curMax):
            curMax = good[tag]-bad[tag]
            curTag = tag
    return curTag, curMax


def applyrule_nexttag(from_tag, to_tag, next_tag, oldcorpus):
    i = 0
    newcorpus = []
    for word in oldcorpus:
        if (i==(len(oldcorpus)-2) or i == (len(oldcorpus)-1)):
            newcorpus.append(tuple([word[0], word[1]]))
        elif ((oldcorpus[i+2][1] == next_tag) and (word[1] == from_tag)):
            newcorpus.append(tuple([word[0], to_tag]))
        else:
            newcorpus.append(tuple([word[0],word[1]]))
        i=i+1
    return newcorpus

def comparetags(true,test):
    if(len(true) != len(test)):
        return 'Cant compare....lengths not the same'
    i = 0
    wrong = 0
    for i in range(len(true)):
        if(test[i][1] != true[i][1]):
            wrong += 1
    return (len(true)-wrong)*100.0/len(true)

#####################################
start = time.time()

trainpercent = 50

words = brown.words()
ntotal = len(words)

words = words[:int32(ntotal*trainpercent/100)]
testwords = words[-(ntotal-len(words)):]
t = brown.tagged_words(simplify_tags=True)[:len(words)]

words = [w.lower() for w in words]

tagwords = []
for word in t:
    tagwords.append(tuple([word[0].lower(),word[1]]))

nwords = len(tagwords)


tagSet = []
for word in tagwords:
    tagSet.append(word[1])
tagSet = set(tagSet)
tagSet = list(tagSet)

fdist = FreqDist(words)
fkeys = fdist.keys()
fprob = []
for i in range(0,fdist.B()):
    fprob.append(fdist.freq(fkeys[i]))

tagcfd = ConditionalFreqDist(tagwords)
tagcfdkeys = tagcfd.keys()

mostlikelytag = []
for i in range(nwords):
    w = tagwords[i][0]
    mostlikelytag.append(tuple([w, tagcfd[w].max()]))

##wrong = 0
##for i in range(nwords):
##    if (mostlikelytag[i][1] != tagwords[i][1]):
##        wrong = wrong + 1
accuracy = comparetags(tagwords, mostlikelytag)

elapsed = time.time()-start
print 'Time: ',elapsed,' Accuracy: ',accuracy
#####################################

ambclass = dict()
for word in words:
    if (word not in ambclass):
        tag = tagcfd[word].items()
        tmp = []
        for i in tag:
            tmp.append(i[0])
        ambclass[word] = tmp


#####################################

num_good_T = dict()
num_bad_T = dict()

bestrulelist = []
thresh = 0

startOverall = time.time()
while (True and len(bestrulelist)<5):
    start = time.time()
    maxval = 0
    counter = 0
    for from_tag in tagSet:
        counter+=1
        print counter
        for to_tag in tagSet:
            i = 0
            for itr in tagSet:
                num_good_T[itr] = 0
                num_bad_T[itr] = 0
            itr = 0
            for word in mostlikelytag[:-2]:
                correct_tag = tagwords[i][1]
                taglist = ambclass[word[0]]
                if(correct_tag == to_tag and word[1] == from_tag):
                    num_good_T[mostlikelytag[i+2][1]] += 1
                if(correct_tag == from_tag and word[1] == from_tag):
                    num_bad_T[mostlikelytag[i+2][1]] += 1
                i += 1

            maxtag, val = findmaxtag(num_good_T,num_bad_T)
            if (val>maxval):
                maxval = val
                changefrom_tag = from_tag
                changeto_tag = to_tag
                changenext_tag = maxtag
            
    if (maxval < thresh):
        break
    
    mostlikelytag = applyrule_nexttag(changefrom_tag,changeto_tag,changenext_tag,mostlikelytag) 
    bestrulelist.append([changefrom_tag,changeto_tag,changenext_tag])

    accuracy = comparetags(tagwords, mostlikelytag)
    
    elapsed = time.time()-start
    print 'Time: ',elapsed,' Accuracy of rule: ',accuracy, ' List: ',bestrulelist[-1]
                    
print 'TOTAL TIME: ', time.time()-startOverall






