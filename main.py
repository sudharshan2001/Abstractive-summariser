import streamlit as st
from bs4 import BeautifulSoup
import requests
import numpy as np
from models.pegasus_custom import get_custom_model
from models.pegasus import get_pegasus
# function to get unique values

custom = True
def unique(list1):
    x = np.array(list1)
    print(np.unique(x))

selectbox = st.sidebar.selectbox(
    "Input type",
    ("URL", "Text")
)
``
if selectbox=='Text':
    text = st.text_area("Paste the sentence that needs to be summarized")

    summary = text
    with st.expander("Input text"):
        if custom:
            summary = get_custom_model(summary)
            st.write(summary)
        else:
            summary = get_pegasus(summary)
            st.write(summary)
    
else:
    url = st.text_input('Enter the URL here')

    if url:

        response = requests.get(url) 
        soup = BeautifulSoup(response.text, "html.parser") 

        News_article = soup.find_all(['p'])
        # print(unique([tag.name for tag in soup.find_all()]))

        news_body_b = ""
        for fd in News_article:
            find1 = fd.getText()
            news_body_b += find1
            
        news_body = " ".join(news_body_b.split())

        print(len(news_body))

        with st.container():
            if custom:
                summary = get_custom_model(news_body)
                st.write(summary)
            else:
                summary = get_pegasus(news_body)
                st.write(summary)
