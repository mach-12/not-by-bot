import asyncio
import streamlit as st
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import pickle
import string
import re
nltk.download('punkt')
nltk.download('stopwords')

class TextSpamService:
    @staticmethod
    async def evaluate_spam_message(message_content: str) -> str:
        sd = SpamDetection()
        return sd.predict(message_content)    

class SpamDetection():
    pipe = None
    model = None    

    def __init__(self) -> None:
        pipe_file = open("ai/model_exports/pipe.pkl",'rb')
        self.pipe = pickle.load(pipe_file)
        pipe_file.close()

        model_file = open("ai/model_exports/model.pkl",'rb')
        self.model = pickle.load(model_file)
        model_file.close()

    @staticmethod
    def basic_clean(x):
        ps = PorterStemmer()

        words = word_tokenize(x.lower())
        final = []
        
        for word in words:     
            if word.isalnum():
                final.append(word)
        words = final[:]
        final = []
        stop_words = set(stopwords.words('english'))

        for i in words:
            if i not in stop_words and i not in string.punctuation:
                final.append(i)
        words = final[:]
        final = []
        
        for i in words:
            final.append(ps.stem(i))
        words = final[:]
        final = []
        return ' '.join(words)

    def predict(self, text):
        if self.model is None:
            return 0
        
        # preprocess
        transformed_text = self.basic_clean(text)
        print(transformed_text)

        # vectorize
        vector_input = self.pipe.transform([transformed_text])
        
        # predict
        result = self.model.predict_proba(vector_input)[0][1] 
        return str(result)


def main():
    st.title("Not-By-Bot App")

    content = st.text_area("Enter your content:")

    if st.button("Check"):
        with st.spinner("Checking..."):
            probability = asyncio.run(TextSpamService.evaluate_spam_message(content))

        if float(probability)>0.5:
            st.markdown(f'<p style="color:red">AI Generated</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:green">Human Content</p>', unsafe_allow_html=True)

        st.write(f"Probability: {probability}")

if __name__ == "__main__":
    main()
