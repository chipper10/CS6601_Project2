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


def applyrule_previoustag(from_tag, to_tag, previous_tag, oldcorpus):
    i = 0
    newcorpus = []
    for word in oldcorpus:
        if (i==0):
            newcorpus.append(tuple([word[0], word[1]]))
        elif ((oldcorpus[i-1][1] == previous_tag) and (word[1] == from_tag)):
            newcorpus.append(tuple([word[0], to_tag]))
            #print 'Orig: ',word, 'New: ',newcorpus[-1]
        else:
            newcorpus.append(tuple([word[0],word[1]]))
        i=i+1
    return newcorpus

def comparetags(true,test):
    if(len(true) != len(test)):
        return 'Cant compare....lengths not the same'
    i,wrong = 0,0
    wronglist = []
    for i in range(len(true)):
        if(test[i][1] != true[i][1]):
            wrong += 1
    return (len(true)-wrong)*100.0/len(true)

#####################################
start = time.time()

trainpercent = 1

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
while (True and len(bestrulelist) <= 4):
    start = time.time()
    maxval = 0
    counter1 = 0
    for from_tag in tagSet:
        #print counter1
        counter1 += 1
        counter2 = 0
        for to_tag in tagSet:
            #print "     ", counter2
            counter2 += 1
            i = 1
            for itr in tagSet:
                num_good_T[itr] = 0
                num_bad_T[itr] = 0
            itr = 0
            for word in mostlikelytag[1:]:
                correct_tag = tagwords[i][1]
                taglist = ambclass[word[0]]
                if(correct_tag == to_tag and word[1] == from_tag):
                    num_good_T[mostlikelytag[i-1][1]] += 1
                if(correct_tag == from_tag and word[1] == from_tag):
                    num_bad_T[mostlikelytag[i-1][1]] += 1
                i += 1

            maxtag, val = findmaxtag(num_good_T,num_bad_T)
            if (val>maxval):
                #print 'Good ', num_good_T
                #print 'Bad', num_bad_T
                #raw_input("Press enter to exit")
                #print '     Maxtag: ',maxtag,' New max: ',val
                maxval = val
                changefrom_tag = from_tag
                changeto_tag = to_tag
                changeprev_tag = maxtag
                #raw_input("Press enter to exit")
            
    if (maxval < thresh):
        break
##    oldlist = list(mostlikelytag)
    mostlikelytag = applyrule_previoustag(changefrom_tag,changeto_tag,changeprev_tag,mostlikelytag) 
    bestrulelist.append([changefrom_tag,changeto_tag,changeprev_tag])            

##    oldwrongtags, oldaccuracy = comparetags(tagwords, oldlist)
##    newwrongtags, newaccuracy = comparetags(tagwords, mostlikelytag)
##    fold  = FreqDist(oldwrongtags)
##    fnew  = FreqDist(newwrongtags)

##    print fold.items()
##    print
##    print fnew.items()
##    print
##    print 'Maxval: ', maxval
    
    elapsed = time.time()-start
    #print 'Rule List: ',bestrulelist
    newaccuracy = comparetags(tagwords, mostlikelytag)
    print 'Time: ',elapsed,' Accuracy of rule: ',newaccuracy, ' List: ',bestrulelist[-1]
    #raw_input("Press Enter....")
                    
print 'TOTAL TIME: ', time.time()-startOverall, 






