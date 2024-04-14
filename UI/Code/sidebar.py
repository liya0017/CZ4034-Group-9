import streamlit as st
from datetime import datetime


#To set up thw sidebar and filter functions in it

def get_sidebar_values():
    
    st.sidebar.title('Filter Options')

    # Filtering Options
    num_rows = st.sidebar.slider('Number of posts to display', min_value=1, max_value=3000, value=100)
    
    sentiment_options = ["All", "Positive", "Negative", "Neutral"]
    sentiment = st.sidebar.selectbox('Select Sentiment', sentiment_options)
    
    start_date = st.sidebar.date_input("Start Date", value=datetime(2021, 1, 1))
    end_date = st.sidebar.date_input("End Date", value=datetime(2021, 12, 31))
    
    sort_options = ["Date Ascending", "Date Descending", "Retweet Count Ascending", "Retweet Count Descending"]
    sort_by = st.sidebar.selectbox('Sort By', sort_options)
    # Sort mapping
    sort_mapping = {
        "Date Ascending": "Date asc",
        "Date Descending": "Date desc",
        "Retweet Count Ascending": "Retweet_Count asc",
        "Retweet Count Descending": "Retweet_Count desc"
    }

    #return the filter functions to query solr
    return num_rows, sentiment, start_date, end_date, sort_by, sort_mapping
