def calculate_sentence_scores(sentences, frequency_table) ->dict:
    sentence_weight = dict()
    print("freq table:", frequency_table)
    for sentence in sentences:
        sentence_wordcount_without_stop_words = 0
        for word_stc in sentence:
            if word_stc.lower() in frequency_table:
                sentence_wordcount_without_stop_words += 1
                sent_title = ''.join(sentence[:7])
                if sent_title in sentence_weight:
                    sentence_weight[sent_title] += frequency_table[ word_stc.lower()]
                else:
                    sentence_weight[sent_title] = frequency_table[ word_stc.lower()]      
        sentence_weight[sent_title] = sentence_weight[sent_title] / sentence_wordcount_without_stop_words            
    return sentence_weight

def calculate_average_score(sentence_weight) -> int:
     sum_values = 0
     for entry in sentence_weight:
         sum_values += sentence_weight[entry]
     average_score = (sum_values/ len(sentence_weight))
     return average_score    

def get_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''
    for sentence in sentences:
        sent_title = ''.join(sentence[:7])
        if sent_title in sentence_weight and sentence_weight[sent_title] >= threshold:
            article_summary += ''.join(str(x)+" " for x in sentence)
            sentence_counter +=1
    return  article_summary.replace('_', ' ')      

                
            
        
    