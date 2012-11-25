import pickle

POS_dict = pickle.load( open( "POSdict.p", "rb" ) )

def get_POS(word):
    if word in POS_dict:
        return POS_dict[word]
    else:
        return 'no POS'
