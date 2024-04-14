import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from query import query_solr
from sidebar import get_sidebar_values
from line_chart import generate_line_chart
from pie_chart import generate_pie_chart
from print_tweets import display_individual_tweets

# Set title
st.title('Covid Vaccine Tweets')

# Search functionality
query = st.text_input('Enter search query:')

# toggle between tabs
tab1, tab2 = st.tabs(["Tweets", "Graphs"])

num_rows, sentiment, start_date, end_date, sort_by, sort_mapping = get_sidebar_values()

search_results = query_solr(query or "*", num_rows, sentiment, start_date, end_date, sort_mapping.get(sort_by))

if search_results:    
    with tab1:
        display_individual_tweets(search_results,query)
    with tab2:
        generate_line_chart(search_results)
        generate_pie_chart(search_results)
    
else:
    st.write('No results found.')
