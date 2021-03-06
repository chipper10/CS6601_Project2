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
    transformDict['.'] = 'x'
    transformDict[','] = ','
    transformDict['('] = '('
    transformDict[')'] = ')'
    transformDict[':'] = ':'
    transformDict['--'] = '--'
    transformDict['*'] = 'v'
    transformDict['ABL'] = 'v'
    transformDict['ABN'] = 'D'
    transformDict['ABX'] = 'D'
    transformDict['AP'] = 'D'
    transformDict['AP$'] = 'D'
    transformDict['AT'] = 'D'
    transformDict['BE'] = 'V'
    transformDict['BED'] = 'V'
    transformDict['BED*'] = 'V'
    transformDict['BEDZ'] = 'V'
    transformDict['BEDZ*'] = 'V'
    transformDict['BEG'] = 'V'
    transformDict['BEM'] = 'V'
    transformDict['BEM*'] = 'V'
    transformDict['BEN'] = 'V'
    transformDict['BER'] = 'V'
    transformDict['BER*'] = 'V'
    transformDict['BEZ'] = 'V'
    transformDict['BEZ*'] = 'V'
    transformDict['CC'] = 'C'
    transformDict['CD'] = 'N'
    transformDict['CD$'] = 'N'
    transformDict['CS'] = 'C'
    transformDict['DO'] = 'V'
    transformDict['DO*'] = 'V'
    transformDict['DO+PPSS'] = 'V'
    transformDict['DOD'] = 'V'
    transformDict['DOD*'] = 'V'
    transformDict['DOZ'] = 'V'
    transformDict['DOZ*'] = 'V'
    transformDict['DT'] = 'r'
    transformDict['DTS'] = 'r'
    transformDict['DT+BEZ'] = 'r'
    transformDict['DT+MD'] = 'r'
    transformDict['DTI'] = 'r'
    transformDict['DTS'] = 'r'
    transformDict['DTS+BEZ'] = 'r'
    transformDict['DT+MD'] = 'r'
    transformDict['DTI'] = 'r'
    transformDict['DTS'] = 'r'
    transformDict['DTS+BEZ'] = 'r'
    transformDict['DTX'] = 'r'
    transformDict['DT-TL'] = 'r'
    transformDict['EX'] = 'v'
    transformDict['EX+BEZ'] = 'v'
    transformDict['EX+HVD'] = 'v'
    transformDict['EX+HVZ'] = 'v'
    transformDict['EX+MD'] = 'v'
    transformDict['HV'] = 'V'
    transformDict['HV*'] = 'V'
    transformDict['HV+TO'] = 'V'
    transformDict['HVD'] = 'V'
    transformDict['HVD*'] = 'V'
    transformDict['HVG'] = 'V'
    transformDict['HVN'] = 'V'
    transformDict['HVZ'] = 'V'
    transformDict['HVZ*'] = 'V'
    transformDict['IN'] = 'P'
    transformDict['IN+IN'] = 'P'
    transformDict['IN+PPO'] = 'P'
    transformDict['IN-TL'] = 'P'
    transformDict['JJ'] = 'A'
    transformDict['JJ$'] = 'A'
    transformDict['JJ+JJ'] = 'A'
    transformDict['JJR'] = 'A'
    transformDict['JJR+CS'] = 'A'
    transformDict['JJS'] = 'A'
    transformDict['JJT'] = 'A'
    transformDict['JJ-TL'] = 'A'
    transformDict['MD'] = 'V'
    transformDict['MD*'] = 'V'
    transformDict['MD+HV'] = 'V'
    transformDict['MD+PPSS'] = 'V'
    transformDict['MD+TO'] = 'V'
    transformDict['MD-TL'] = 'V'
    transformDict['NN'] = 'N'
    transformDict['NN$'] = 'N'
    transformDict['NN+BEZ'] = 'N'
    transformDict['NN+HVD'] = 'N'
    transformDict['NN+HVZ'] = 'N'
    transformDict['NN+IN'] = 'N'
    transformDict['NN+MD'] = 'N'
    transformDict['NN+NN'] = 'N'
    transformDict['NN-TL'] = 'N'
    transformDict['NNS'] = 'N'
    transformDict['NNS$'] = 'N'
    transformDict['NNS+MD'] = 'N'
    transformDict['NP'] = 'N'
    transformDict['NP$'] = 'N'
    transformDict['NP+BEZ'] = 'N'
    transformDict['NP+HVZ'] = 'N'
    transformDict['NP+MD'] = 'N'
    transformDict['NPS'] = 'N'
    transformDict['NPS$'] = 'N'
    transformDict['NR'] = 'N'
    transformDict['NR$'] = 'N'
    transformDict['NR+MD'] = 'N'
    transformDict['NRS'] = 'N'
    transformDict['OD'] = 'A'
    transformDict['PN'] = 'r'
    transformDict['PN$'] = 'r'
    transformDict['PN+BEZ'] = 'r'
    transformDict['PN+HVDT'] = 'r'
    transformDict['PN+HVZ'] = 'r'
    transformDict['PN+MD'] = 'r'
    transformDict['PN-TL'] = 'r'
    transformDict['PP$'] = 'r'
    transformDict['PP$$'] = 'r'
    transformDict['PPL'] = 'r'
    transformDict['PPLS'] = 'r'
    transformDict['PPO'] = 'r'
    transformDict['PPS'] = 'r'
    transformDict['PP-TL'] = 'r'
    transformDict['PPS+BEZ'] = 'r'
    transformDict['PPS+HVD'] = 'r'
    transformDict['PPS+HVZ'] = 'r'
    transformDict['PPS+MD'] = 'r'
    transformDict['PPSS'] = 'r'
    transformDict['PPSS+BEM'] = 'r'
    transformDict['PPSS+BER'] = 'r'
    transformDict['PPSS+BEZ'] = 'r'
    transformDict['PPSS+BEZ*'] = 'r'
    transformDict['PPSS+HV'] = 'r'
    transformDict['PPSS+HVD'] = 'r'
    transformDict['PPSS+MD'] = 'r'
    transformDict['PPSS+VB'] = 'r'
    transformDict['QL'] = 'v'
    transformDict['QLP'] = 'v'
    transformDict['RB'] = 'v'
    transformDict['RB-TL'] = 'v'
    transformDict['RB$'] = 'v'
    transformDict['RB+BEZ'] = 'v'
    transformDict['RB+CS'] = 'v'
    transformDict['RBR'] = 'v'
    transformDict['RBR+CS'] = 'v'
    transformDict['RBT'] = 'v'
    transformDict['RN'] = 'v'
    transformDict['RP'] = 'v'
    transformDict['RP+IN'] = 'v'
    transformDict['TO'] = 'P'
    transformDict['TO+VB'] = 'P'
    transformDict['UH'] = '!'
    transformDict['VB'] = 'V'
    transformDict['VB+AT'] = 'V'
    transformDict['VB-TL'] = 'V'
    transformDict['VB+IN'] = 'V'
    transformDict['VB+JJ'] = 'V'
    transformDict['VB+PPO'] = 'V'
    transformDict['VB+RP'] = 'V'
    transformDict['VB+TO'] = 'V'
    transformDict['VB+VB'] = 'V'
    transformDict['VBD'] = 'V'
    transformDict['VBG'] = 'V'
    transformDict['VBG+TO'] = 'V'
    transformDict['VBZ'] = 'V'
    transformDict['WDT'] = 'D'
    transformDict['WDT+BER'] = 'D'
    transformDict['WDT+BER+PP'] = 'D'
    transformDict['WDT+BEZ'] = 'D'
    transformDict['WDT+DO+PPS'] = 'D'
    transformDict['WDT+DOD'] = 'D'
    transformDict['WDT+HVZ'] = 'D'
    transformDict['WP$'] = 'D'
    transformDict['WPO'] = 'D'
    transformDict['WPS'] = 'D'
    transformDict['WPS+BEZ'] = 'D'
    transformDict['WPS+HVD'] = 'D'
    transformDict['WPS+HVZ'] = 'D'
    transformDict['WPS+MD'] = 'D'
    transformDict['WQL'] = 'D'
    transformDict['WRB'] = 'D'
    transformDict['WRB+BER'] = 'D'
    transformDict['WRB+BEZ'] = 'D'
    transformDict['WRB+DO'] = 'D'
    transformDict['WRB+DOD'] = 'D'
    transformDict['WRB+DOD*'] = 'D'
    transformDict['WRB+DOZ'] = 'D'
    transformDict['WRB+IN'] = 'D'
    transformDict['WRB+MD'] = 'D'
    
    
    
    for tag in brown.tagged_words():
        tagNew = [0, 0]
        tagNew[0] = tag[0]
        tagNew[1] = tag[1]
        if tagNew[1] in transformDict:
            tagNew[1] = transformDict[tagNew[1]]
        else:
            tagNew[1] = 'no POS'
        tagged_Brown.append(tagNew)
    return tagged_Brown

def tagCount(words):
    tagSet = set()
    for i in words:
        tagSet.add(i[1])
    return tagSet

        
        
