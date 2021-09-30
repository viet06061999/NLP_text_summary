def calculate_sentence_scores(sentences, frequency_table) ->dict:
    sentence_weight = dict()
    print("freq table:", frequency_table)
    for sentence in sentences:
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]      
        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words            
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
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= threshold:
            article_summary += " " + sentence
            sentence_counter +=1

    return article_summary        

                
            
        
    