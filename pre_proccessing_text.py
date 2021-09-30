from vncorenlp import VnCoreNLP
vncorenlp_file = r'.\VnCoreNLP\VnCoreNLP-1.1.1.jar'
vncorenlp = VnCoreNLP(vncorenlp_file)

def create_dictionary_table(text_string):
    #remove stop words
    text_string_tmp = text_string.lower()
    lines = []
    with open(r'./vietnamese-stopwords-dash.txt','r',encoding='utf-8') as f:
         lines = f.read().split('\n')
    stop_words = set(lines)
    words =vncorenlp.tokenize(text_string_tmp.replace('.', ' '))
    vncorenlp.close()
    # reducing words to root word
    # create dictionary for the word frequency table
    frequency_table = dict()
    for wd_st in words:
        print('word:', wd_st )
        for wd in wd_st: 
            if wd in stop_words:
                continue
            if wd in frequency_table:
                frequency_table[wd] += 1
            else:
                frequency_table[wd] = 1    
    return frequency_table

def sent_token(text_content):
    # words =vncorenlp.tokenize(text_content.replace('.', '. '))
    words =vncorenlp.tokenize(text_content)
    vncorenlp.close()
    return words
