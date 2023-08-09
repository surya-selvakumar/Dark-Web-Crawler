import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Define keywords for each category


# Initialize the Porter stemmer


# Tokenize text, apply stemming and check for keywords
def classify_text(text, stemmer):
    weapons_keywords = ['gun', 'knife', 'bomb', 'weapon']
    drugs_keywords = ['cocaine', 'heroin', 'marijuana', 'meth', 'drug', 'weed']
    fake_id_keywords = ['fake', 'forged', 'false']
    pornography_keywords = ['porn', 'XXX', 'adult']
    words = word_tokenize(text.lower())
    stemmed_words = [stemmer.stem(word) for word in words]
    if any(keyword in stemmed_words for keyword in weapons_keywords):
        return 'Weapons'
    elif any(keyword in stemmed_words for keyword in drugs_keywords):
        return 'Drugs'
    elif any(keyword in stemmed_words for keyword in fake_id_keywords):
        return 'Fake ID'
    elif any(keyword in stemmed_words for keyword in pornography_keywords):
        return 'Pornography'
    else:
        return 'Unknown'

# Test the function
text1 = 'I need a gun for self-defense.'
text2 = 'I smoked some weed last night.'
text3 = 'I want a fake ID to buy alcohol.'
text4 = 'I watched some porn on the internet.'


