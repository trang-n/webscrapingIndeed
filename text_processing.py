import re
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from string import digits



#tokenize a text to list of tokens
def tokenize_text(text, stem=False):

    stop_words = set(stopwords.words('english')) 

    # Replace any non word characters except .+# with space
    text = re.sub("[^\w.+#]", " ", text)
    
    #\d+\.?\d+\s -- any number of digits followed by a space with or without a dot in between 
    #remove number alone not number in words
    text = re.sub("\d+\.?\d+\s|\d+\+", " ", text) 
    tokens = text.lower().split()
    tokens = [token for token in tokens if token not in stop_words]

    #stem tokens
    if stem:
        stemmer = SnowballStemmer("english")
        tokens = [stemmer.stem(i) for i in tokens]
                    
    return tokens 
    
    
    
#check frequency of each given words in list of postingstrings
#parameter: dict to check frequency for, list of strings
#output: frequency count (dict)

def frequency(tocheck_dict, string_list):
    text = ' '.join(string_list).lower() #join strings together and convert to lower
    freq = {}
    for category, skill_list in tocheck_dict.items():
        freq[category] = {}
                     
    #initialize each category as a dictionary
        for skill in skill_list:
            if len(skill) == 1:
                skill_name = ' ' + skill.lower() + ' '
            else:
                skill_name = skill.lower()
            freq[category][skill] = text.count(skill_name) 
            #percentage for interpretability.
            
    return freq
        

        
