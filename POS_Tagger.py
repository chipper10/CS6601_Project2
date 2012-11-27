#for dictionary loading
import pickle
#natural language toolkit
import nltk
from nltk.corpus import brown

POS_dict = pickle.load( open( "POSdict.p", "rb" ) )

def get_POS(word):
    if word in POS_dict:
        return POS_dict[word]
    else:
        return 'no POS'

def parse_Sentence(sentence):
    POSs = []
    #tokenize
    words = nltk.word_tokenize(sentence)
    #get POSs (parts of speech)
    for word in words:
        if word == '.':
            POSs.append('x')
        else:
            word = word.lower()
            POSs.append(get_POS(word))
    return POSs


def tagged_Brown():
    tagged_Brown = []
    transformDict = dict()
    transformDict['ABL'] = 'D'
    transformDict['ABN'] = 'D'
    transformDict['ABX'] = 'D'
    transformDict['AP'] = 'D'
    transformDict['AP$'] = 'D'
    transformDict['AP+AP'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['BE'] = 'D'
    transformDict['BED'] = 'D'
    transformDict['BED*'] = 'D'
    transformDict['BEDZ'] = 'D'
    transformDict['BEDZ*'] = 'D'
    transformDict['BEG'] = 'D'
    transformDict['BEM'] = 'D'
    transformDict['BEM*'] = 'D'
    transformDict['BEN'] = 'D'
    transformDict['BER'] = 'D'
    transformDict['BER*'] = 'D'
    transformDict['BEZ'] = 'D'
    transformDict['BEZ*'] = 'D'
    transformDict['CC'] = 'D'
    transformDict['CD'] = 'D'
    transformDict['CD$'] = 'D'
    transformDict['CS'] = 'D'
    transformDict['DO'] = 'D'
    transformDict['DO*'] = 'D'
    transformDict['DO+PPSS'] = 'D'
    transformDict['DOD'] = 'D'
    transformDict['DOD*'] = 'D'
    transformDict['DOZ'] = 'D'
    transformDict['DOZ*'] = 'D'
    transformDict['DT'] = 'D'
    transformDict['DTS'] = 'D'
    transformDict['DT+BEZ'] = 'D'
    transformDict['DT+MD'] = 'D'
    transformDict['DTI'] = 'D'
    transformDict['DTS'] = 'D'
    transformDict['DTS+BEZ'] = 'D'
    transformDict['DT+MD'] = 'D'
    transformDict['DTI'] = 'D'
    transformDict['DTS'] = 'D'
    transformDict['DTS+BEZ'] = 'D'
    transformDict['DTX'] = 'D'
    transformDict['EX'] = 'D'
    transformDict['EX+BEZ'] = 'D'
    transformDict['EX+HVD'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['AT'] = 'D'
    
    for tag in brown.tagged_words():
        tagNew = [0, 0]
        tagNew[0] = tag[0]
        tagNew[1] = tag[1]
        if tagNew[1] == 'AT':
            tagNew[1] = 'D'
        elif tagNew[1] == 'AT':
            tagNew[1] = 'D'
        tagged_Brown.append(tagNew)
    return tagged_Brown
        
        
        
