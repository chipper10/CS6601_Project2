import nltk
from nltk import *
from nltk.corpus import brown
import numpy
from numpy import *
import pickle
import time

def tagtest(testcorpus):
    ambclass = pickle.load( open( "ambclass.p", "rb" ) )
    SinglePreviousTag = pickle.load( open( "SinglePreviousTag.p", "rb" ) )
    #DoublePreviousTag = pickle.load( open( "DoublePreviousTag.p", "rb" ) )
    SingleNextTag = pickle.load( open( "SingleNextTag.p", "rb" ) )
    #DoubleNextTag = pickle.load( open( "DoubleNextTag.p", "rb" ) )
    
    mostlikelytag = []
    for i in range(len(testcorpus)):
        w = testcorpus[i]
        if w in ambclass:
            mostlikelytag.append(tuple([w, ambclass[w.lower()][0]]))
        else:
            #mostlikelytag.append(tuple([w, 'N'])
            if '.' in w:
                mostlikelytag.append(tuple([w, 'NUM']))
            elif '-' in w:
                mostlikelytag.append(tuple([w, 'ADJ']))
            elif 'ed' in w[-2:]:
                mostlikelytag.append(tuple([w, 'VD']))
            elif 'ing' in w[-3:]:
                mostlikelytag.append(tuple([w, 'VG']))
            elif 'ly' in w[-2:]:
                mostlikelytag.append(tuple([w, 'ADV']))
            elif 'al' in w[-2:]:
                mostlikelytag.append(tuple([w, 'ADJ']))
            elif '0' in w:
                mostlikelytag.append(tuple([w, 'NUM']))
            elif 'us' in w[-2:]:
                mostlikelytag.append(tuple([w, 'ADJ']))
            elif 'ble' in w[-3:]:
                mostlikelytag.append(tuple([w, 'ADJ']))                
            elif 'ic' in w[-2:]:
                mostlikelytag.append(tuple([w, 'ADJ']))                                     
            elif '1' in w:
                mostlikelytag.append(tuple([w, 'NUM']))
            elif 'ive' in w[-3:]:
                mostlikelytag.append(tuple([w, 'ADJ']))
            elif '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in w[-3:]:
                mostlikelytag.append(tuple([w, 'NUM']))
            else:
                mostlikelytag.append(tuple([w, 'N']))
                                     
            
                                 
    for i in range(0:4):
        mostlikelytag = applyrule_nexttag(SingleNextTag[i][0], SingleNextTag[i][1], SingleNextTag[i][2])
        mostlikelytag = applyrule_previoustag(SinglePreviousTag[i][0], SinglePreviousTag[i][1], SinglePreviousTag[i][2])
        #mostlikelytag = applyrule_twicenexttag(DoubleNextTag[i][0], DoubleNextTag[i][1], DoubleNextTag[i][2])
        #mostlikelytag = applyrule_twiceprevioustag(DoublePreviousTag[i][0], DoublePreviousTag[i][1], DoublePreviousTag[i][2])

    return mostlikelytag
                                     

#####################################

def applyrule_nexttag(from_tag, to_tag, next_tag, oldcorpus):
    i = 0
    newcorpus = []
    for word in oldcorpus:
        if (i==(len(oldcorpus)-1)):
            newcorpus.append(tuple([word[0], word[1]]))
        elif ((oldcorpus[i+1][1] == next_tag) and (word[1] == from_tag)):
            newcorpus.append(tuple([word[0], to_tag]))
        else:
            newcorpus.append(tuple([word[0],word[1]]))
        i=i+1
    return newcorpus                                    

def applyrule_twicenexttag(from_tag, to_tag, next_tag, oldcorpus):
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
                                     
def applyrule_twiceprevioustag(from_tag, to_tag, previous_tag, oldcorpus):
    i = 0
    newcorpus = []
    for word in oldcorpus:
        if (i<2):
            newcorpus.append(tuple([word[0], word[1]]))
        elif ((oldcorpus[i-2][1] == previous_tag) and (word[1] == from_tag)):
            newcorpus.append(tuple([word[0], to_tag]))
            #print 'Orig: ',word, 'New: ',newcorpus[-1]
        else:
            newcorpus.append(tuple([word[0],word[1]]))
        i=i+1
    return newcorpus





