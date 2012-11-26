#for dictionary loading
import pickle
#natural language toolkit
import nltk

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
        
        
