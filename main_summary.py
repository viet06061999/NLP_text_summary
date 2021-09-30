import fetch_content
import pre_proccessing_text
import proccessing

def run_summary(text_content):
    frequency_table = pre_proccessing_text.create_dictionary_table(text_content)
    
    sentences = pre_proccessing_text.sent_token(text_content)
    print('******SENTENCES****')
    print(sentences)
    sentence_scores = proccessing.calculate_sentence_scores(sentences, frequency_table)
    print('******SENTENCES CORES****')
    print(sentence_scores)
    threshold = proccessing.calculate_average_score(sentence_scores)
    print('******THRESHOLD****')
    print(threshold)
    text_summary= proccessing.get_summary(sentences, sentence_scores, 1.1 * threshold)

    return text_summary

if __name__ == '__main__':
    text_content = fetch_content.fetch_data('https://vnexpress.net/cac-co-so-y-te-tai-tp-hcm-hoat-dong-tro-lai-4364538.html')
    summary_results = run_summary(text_content)
    print('**********SUMMARY*************')
    print(summary_results)
