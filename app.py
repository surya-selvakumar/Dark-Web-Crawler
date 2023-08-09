import streamlit as st
import os 
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from classify import classify_text

st.title('Dark Web Crawler')

link = st.text_input('paste ".onion" link here')
btn = st.button('crawl')

if link and btn:
    #os.execute('py TorScrape.py')
    with open('sample.txt', 'r') as f:
        data = f.read()
        
    soup = BeautifulSoup(data, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    stemmer = PorterStemmer()
    
    st.warning(classify_text(text, stemmer))
    
    
        
    

    
