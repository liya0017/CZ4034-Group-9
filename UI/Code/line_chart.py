import streamlit as st
import pandas as pd

# To generate the line graph: Number of tweets per day

def generate_line_chart(search_results):
    st.write('Line Graph:')
    tweet_dates = [result['Date'][0][:10] for result in search_results['response']['docs']]
    tweet_dates_count = pd.Series(tweet_dates).value_counts().sort_index()
    st.line_chart(tweet_dates_count)
