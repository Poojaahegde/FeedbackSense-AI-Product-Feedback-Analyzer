import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from textblob import TextBlob
import matplotlib.pyplot as plt

st.title("FeedbackSense 💬")
st.write("Analyze user feedback and group insights using AI clustering and sentiment analysis.")

uploaded = st.file_uploader("Upload a CSV with a 'feedback' column")
if uploaded:
    df = pd.read_csv(uploaded)
    feedbacks = df['feedback'].astype(str)
    sentiments = [TextBlob(text).sentiment.polarity for text in feedbacks]
    df['sentiment'] = sentiments

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(feedbacks)
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    st.subheader("Clustered Insights")
    st.write(df[['feedback', 'cluster', 'sentiment']])

    st.subheader("Sentiment Distribution")
    plt.hist(df['sentiment'], bins=20)
    st.pyplot(plt)
