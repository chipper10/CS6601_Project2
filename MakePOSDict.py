# build the dictionary
import pickle
POS_dict = dict()
for line in open('part-of-speech.txt'):
 # however you process the file
    word,split1 = line.split('	')
    pos,junk = split1.split('\n')

 # put it in the dictionary
    POS_dict[word] = pos

pickle.dump( POS_dict, open( "POSdict.p", "wb" ) )

def get_POS(word):
 # should use english_dict.get(word,'undefined')
    if word in POS_dict:
        return POS_dict[word]
    else:
        return 'no POS'
